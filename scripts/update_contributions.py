#!/usr/bin/env python3
"""Refresh merged-PR counts for every upstream organisation and rewrite the README.

Counts come from the GitHub search API, so they are organisation-wide: every
repository in the org counts, not just the one that happened to be listed by
hand. Each org's bar SVG is regenerated and the contributions table, the
summary badges and the prose totals in README.md are rewritten in place.

Run locally with:  GITHUB_TOKEN=$(gh auth token) python3 scripts/update_contributions.py
"""

import json
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONFIG = os.path.join(ROOT, "scripts", "orgs.json")
README = os.path.join(ROOT, "README.md")
ASSETS = os.path.join(ROOT, "assets")
API = "https://api.github.com/search/issues"

TABLE_START = "<!-- contrib-table:start -->"
TABLE_END = "<!-- contrib-table:end -->"
BADGE_START = "<!-- contrib-badges:start -->"
BADGE_END = "<!-- contrib-badges:end -->"

TRACK_PX = 150.0          # width of a full-length bar
BAR_MIN_PX = 10.0         # keep tiny counts visible as a rounded cap


def search_count(query, token):
    """Total matches for a search query, with a retry for search rate limiting."""
    url = f"{API}?q={urllib.parse.quote(query)}&per_page=1"
    req = urllib.request.Request(url)
    req.add_header("Accept", "application/vnd.github+json")
    req.add_header("User-Agent", "vtushar06-profile-updater")
    if token:
        req.add_header("Authorization", f"Bearer {token}")

    for attempt in range(4):
        try:
            with urllib.request.urlopen(req, timeout=30) as resp:
                return json.load(resp)["total_count"]
        except urllib.error.HTTPError as exc:
            # 403/429 here is the search rate limit (30 req/min authenticated).
            if exc.code in (403, 429) and attempt < 3:
                wait = 20 * (attempt + 1)
                print(f"  rate limited on {query!r}, waiting {wait}s", file=sys.stderr)
                time.sleep(wait)
                continue
            raise
    raise RuntimeError(f"gave up querying {query!r}")


def bar_svg(key, count, width_px, delay, num_delay):
    """A green progress bar, revealed left to right through a translating clip."""
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="210" height="22" viewBox="0 0 210 22" fill="none" role="img" aria-label="{count} merged pull requests">
  <defs>
    <linearGradient id="g{key}" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="#2ea043"/>
      <stop offset="100%" stop-color="#3fb950"/>
    </linearGradient>
    <clipPath id="c{key}">
      <rect class="rev" x="0" y="4" width="{width_px:.1f}" height="14" rx="7"/>
    </clipPath>
    <style>
      @keyframes r{key} {{ from {{ transform: translateX(-{width_px:.1f}px) }} to {{ transform: translateX(0) }} }}
      @keyframes f{key} {{ from {{ opacity: 0 }} to {{ opacity: 1 }} }}
      .rev {{ animation: r{key} 1.4s cubic-bezier(.16,1,.3,1) both; animation-delay: {delay}s; }}
      .num {{ animation: f{key} .5s ease-out both; animation-delay: {num_delay}s; }}
      @media (prefers-reduced-motion: reduce) {{ .rev, .num {{ animation: none; }} }}
    </style>
  </defs>
  <rect x="0" y="4" width="150" height="14" rx="7" fill="#8b949e" fill-opacity=".20"/>
  <g clip-path="url(#c{key})">
    <rect x="0" y="4" width="{width_px:.1f}" height="14" rx="7" fill="url(#g{key})"/>
  </g>
  <text class="num" x="160" y="16" font-family="'JetBrains Mono','Fira Code',ui-monospace,SFMono-Regular,Menlo,monospace"
        font-size="14" font-weight="700" fill="#2ea043">{count}</text>
</svg>
'''


def render_rows(orgs, raw, user):
    rows = []
    for org in orgs:
        logo = org["logo"].replace("{RAW}", raw)
        sub = org.get("sub", "").replace("{RAW}", raw)
        search = f"https://github.com/search?q=author%3A{user}+is%3Apr+is%3Amerged+{urllib.parse.quote(org['query'])}"
        rows.append(
            f'''    <tr>
      <td align="center">
        <a href="{org['link']}">{logo}</a>
        <br><br>
        {sub}
      </td>
      <td align="left">
        {org['work']}
      </td>
      <td align="center">
        <a href="{search}"><img src="{raw}/bar-{org['key']}.svg" width="200" alt="{org['count']} merged" /></a>
      </td>
    </tr>'''
        )
    return "\n".join(rows)


def main():
    token = os.environ.get("GITHUB_TOKEN", "")
    if not token:
        print("warning: no GITHUB_TOKEN, unauthenticated search is heavily rate limited", file=sys.stderr)

    cfg = json.load(open(CONFIG))
    user, raw, orgs = cfg["user"], cfg["raw"], cfg["orgs"]

    print("Querying organisation-wide merged counts...")
    for org in orgs:
        org["count"] = search_count(f"author:{user} is:pr is:merged {org['query']}", token)
        print(f"  {org['name']:<20} {org['count']}")

    totals = {
        "merged": search_count(f"author:{user} is:pr is:merged", token),
        "authored": search_count(f"author:{user} is:pr", token),
        "open": search_count(f"author:{user} is:pr is:open", token),
    }
    print(f"  {'TOTAL':<20} {totals['merged']} merged / {totals['authored']} authored / {totals['open']} open")

    orgs.sort(key=lambda o: o["count"], reverse=True)
    top = max((o["count"] for o in orgs), default=1) or 1

    os.makedirs(ASSETS, exist_ok=True)
    for i, org in enumerate(orgs):
        width = max(BAR_MIN_PX, TRACK_PX * org["count"] / top)
        svg = bar_svg(org["key"], org["count"], width, round(0.10 + i * 0.12, 2), round(0.90 + i * 0.12, 2))
        with open(os.path.join(ASSETS, f"bar-{org['key']}.svg"), "w") as fh:
            fh.write(svg)

    readme = open(README).read()
    original = readme

    # table body
    rows = render_rows(orgs, raw, user)
    readme = re.sub(
        re.escape(TABLE_START) + r".*?" + re.escape(TABLE_END),
        f"{TABLE_START}\n{rows}\n    {TABLE_END}",
        readme,
        flags=re.S,
    )

    # summary badges
    badges = (
        f'  <a href="https://github.com/search?q=author%3A{user}+is%3Apr+is%3Amerged">'
        f'<img src="https://img.shields.io/badge/{totals["merged"]}-Merged_PRs-2ea043?style=for-the-badge&logo=github&logoColor=white" /></a>\n'
        f'  <a href="https://github.com/search?q=author%3A{user}+is%3Apr">'
        f'<img src="https://img.shields.io/badge/{totals["authored"]}-Authored_PRs-6d28d9?style=for-the-badge&logo=github&logoColor=white" /></a>\n'
        f'  <a href="https://github.com/search?q=author%3A{user}+is%3Apr+is%3Aopen">'
        f'<img src="https://img.shields.io/badge/{totals["open"]}-In_Review-5b21b6?style=for-the-badge&logo=github&logoColor=white" /></a>'
    )
    readme = re.sub(
        re.escape(BADGE_START) + r".*?" + re.escape(BADGE_END),
        f"{BADGE_START}\n{badges}\n  {BADGE_END}",
        readme,
        flags=re.S,
    )

    # prose and the typing banner, all keyed off the merged total
    m = totals["merged"]
    n_orgs = len(orgs)
    subs = [
        (r"(\d+)\+Merged\+PRs\+Across", f"{m}+Merged+PRs+Across"),
        (r"<strong>\d+ merged pull requests in \d+\+ upstream organisations</strong>",
         f"<strong>{m} merged pull requests in {n_orgs}+ upstream organisations</strong>"),
        (r'openSource:  "\d+ merged PRs · \d+\+ upstream orgs"',
         f'openSource:  "{m} merged PRs · {n_orgs}+ upstream orgs"'),
        (r"<p>\d+ merged pull requests across", f"<p>{m} merged pull requests across"),
        (r"<strong>\d+ Merged Pull Requests</strong>", f"<strong>{m} Merged Pull Requests</strong>"),
        (r"<sub>Across \d+\+ upstream organisations</sub>", f"<sub>Across {n_orgs}+ upstream organisations</sub>"),
    ]
    for pattern, repl in subs:
        readme = re.sub(pattern, repl, readme)

    if readme != original:
        open(README, "w").write(readme)
        print("README.md updated")
    else:
        print("README.md already current")


if __name__ == "__main__":
    main()

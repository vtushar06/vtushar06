<!--
  ─────────────────────────────────────────────────────────────────────────────
  Tushar Verma · github.com/vtushar06
  Theme: GSoC gold  (#FFD54F · #FBBC04 · #F59E0B on #0d1117)

  The five banners are hand-authored animated SVGs living in ./assets.
  They animate via CSS keyframes + SMIL inside the SVG, which is exactly what
  GitHub's image proxy renders — no JS, no external fetches, no build step.
  Edit the numbers in those files when the PR counts move.
  ─────────────────────────────────────────────────────────────────────────────
-->

<div align="center">

<img src="https://raw.githubusercontent.com/vtushar06/vtushar06/main/assets/hero.svg" width="100%" alt="Tushar Verma — GSoC '26 @ JSON Schema · Podman upstream · New Delhi" />

<br>

<img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=600&size=21&duration=2800&pause=700&color=FBBC04&center=true&vCenter=true&width=820&height=45&lines=Google+Summer+of+Code+'26+%40+JSON+Schema;192+merged+pull+requests+across+10%2B+upstreams;Podman+%C2%B7+Skopeo+%C2%B7+Buildah+%E2%80%94+CI%2C+tests+and+flake+forensics;CTO+%40+Shivam-Info+%C2%B7+Software+Engineer+%40+Mugafi;I+fix+the+tests+nobody+wants+to+look+at." alt="What I do" />

<br>

<a href="https://tushar-portfolio.netlify.app">
  <img src="https://img.shields.io/badge/PORTFOLIO-FBBC04?style=for-the-badge&logo=firefoxbrowser&logoColor=0d1117&labelColor=0d1117&color=FBBC04" alt="Portfolio" /></a>
<a href="https://www.linkedin.com/in/tushar-verma-851a76338/">
  <img src="https://img.shields.io/badge/LINKEDIN-0d1117?style=for-the-badge&logo=linkedin&logoColor=FBBC04&labelColor=0d1117&color=161b22" alt="LinkedIn" /></a>
<a href="mailto:tusharmyself06@gmail.com">
  <img src="https://img.shields.io/badge/EMAIL-0d1117?style=for-the-badge&logo=gmail&logoColor=FBBC04&labelColor=0d1117&color=161b22" alt="Email" /></a>
<a href="https://x.com/TusharV76610577">
  <img src="https://img.shields.io/badge/X-0d1117?style=for-the-badge&logo=x&logoColor=FBBC04&labelColor=0d1117&color=161b22" alt="X" /></a>
<a href="https://holopin.io/@vtushar06">
  <img src="https://img.shields.io/badge/HOLOPIN-0d1117?style=for-the-badge&logo=holopin&logoColor=FBBC04&labelColor=0d1117&color=161b22" alt="Holopin" /></a>
<br>
<img src="https://komarev.com/ghpvc/?username=vtushar06&color=FBBC04&style=for-the-badge&label=PROFILE+VIEWS" alt="Profile views" />
<a href="https://github.com/vtushar06?tab=followers">
  <img src="https://img.shields.io/github/followers/vtushar06?style=for-the-badge&color=FBBC04&labelColor=0d1117&logo=github&logoColor=FBBC04&label=FOLLOWERS" alt="Followers" /></a>

</div>

<img src="https://raw.githubusercontent.com/vtushar06/vtushar06/main/assets/divider.svg" width="100%" alt="" />

## Three tracks, one engineer

<img src="https://raw.githubusercontent.com/vtushar06/vtushar06/main/assets/tracks.svg" width="100%" alt="CTO @ Shivam-Info · GSoC '26 @ JSON Schema · LFX Mentorship, Podman" />

I run engineering at a company, I ship spec-conformance work for a standards body, and I spend my
evenings inside container tooling. Those are not three hobbies — they are the same instinct applied
at three altitudes: **read the spec, reproduce the failure, land the smallest correct patch.**

<img src="https://raw.githubusercontent.com/vtushar06/vtushar06/main/assets/divider.svg" width="100%" alt="" />

## `$ podman inspect tushar`

Described the way I spend most of my week describing things — as a schema.

```jsonc
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id":     "https://github.com/vtushar06",
  "title":   "Tushar Verma",
  "type":    "object",

  "properties": {
    "location":  { "const": "New Delhi, India" },
    "education": { "const": "B.Tech, Computer Science (AI & ML)" },

    "roles": {
      "type": "array",
      "items": { "enum": [
        "CTO @ Shivam-Info",
        "Software Engineer @ Mugafi",
        "Google Summer of Code '26 @ JSON Schema",
        "Upstream contributor — Podman · Skopeo · Buildah · OpenCost · Headlamp"
      ]}
    },

    "workingOn": {
      "type": "array",
      "items": { "enum": [
        "RFC 3986 / 3987 conformance for the JSON Schema Test Suite",
        "CI reliability and flake forensics in containers/*",
        "ci-flake-triage — confirmed flakes from rerun history, zero CI changes"
      ]}
    },

    "reviewStyle": {
      "description": "What a maintainer gets when they assign me an issue",
      "type": "array",
      "items": { "enum": [
        "one concern per pull request",
        "a failing test before the fix",
        "the RFC paragraph quoted in the description",
        "no drive-by refactors in a bug fix"
      ]}
    }
  },

  "required": ["roles", "workingOn", "reviewStyle"],
  "additionalProperties": true   // always more to learn
}
```

<img src="https://raw.githubusercontent.com/vtushar06/vtushar06/main/assets/divider.svg" width="100%" alt="" />

## Upstream, measured

Anyone can list technologies. This is the part that is checkable — every number below links to the
GitHub search that produces it.

<img src="https://raw.githubusercontent.com/vtushar06/vtushar06/main/assets/impact.svg" width="100%" alt="Merged pull requests by upstream organisation" />

<div align="center">

| Upstream | What I work on there | Merged |
|:--|:--|:--:|
| **[JSON Schema](https://github.com/json-schema-org/JSON-Schema-Test-Suite)** | Format-assertion coverage for `uri`, `iri`, `uri-template`, `time` — the cases every validator gets wrong | [![](https://img.shields.io/badge/78-FBBC04?style=flat-square&labelColor=0d1117)](https://github.com/search?q=author%3Avtushar06+is%3Apr+is%3Amerged+org%3Ajson-schema-org) |
| **[sourcemeta/core](https://github.com/sourcemeta/core)** | C++ URI/RFC 3986 production coverage | [![](https://img.shields.io/badge/16-FBBC04?style=flat-square&labelColor=0d1117)](https://github.com/search?q=author%3Avtushar06+is%3Apr+is%3Amerged+repo%3Asourcemeta%2Fcore) |
| **[Learning Equality](https://github.com/learningequality/studio)** | Kolibri Studio + design system | [![](https://img.shields.io/badge/16-FBBC04?style=flat-square&labelColor=0d1117)](https://github.com/search?q=author%3Avtushar06+is%3Apr+is%3Amerged+org%3Alearningequality) |
| **[containers](https://github.com/containers/podman)** *(Podman · Skopeo · Buildah · automation)* | CI plumbing, system-test races, release tooling | [![](https://img.shields.io/badge/14-FBBC04?style=flat-square&labelColor=0d1117)](https://github.com/search?q=author%3Avtushar06+is%3Apr+is%3Amerged+org%3Acontainers) |
| **[OpenCost](https://github.com/opencost/opencost)** *(CNCF)* | Integration tests + contributor onboarding bot | [![](https://img.shields.io/badge/14-FBBC04?style=flat-square&labelColor=0d1117)](https://github.com/search?q=author%3Avtushar06+is%3Apr+is%3Amerged+org%3Aopencost) |
| **[Headlamp](https://github.com/kubernetes-sigs/headlamp)** *(Kubernetes SIGs)* | UI and plugin fixes | [![](https://img.shields.io/badge/6-FBBC04?style=flat-square&labelColor=0d1117)](https://github.com/search?q=author%3Avtushar06+is%3Apr+is%3Amerged+repo%3Akubernetes-sigs%2Fheadlamp) |

<a href="https://github.com/search?q=author%3Avtushar06+is%3Apr+is%3Amerged"><img src="https://img.shields.io/badge/192%20MERGED-FBBC04?style=for-the-badge&labelColor=0d1117&logo=github&logoColor=FBBC04" alt="192 merged" /></a>
<a href="https://github.com/search?q=author%3Avtushar06+is%3Apr"><img src="https://img.shields.io/badge/285%20AUTHORED-0d1117?style=for-the-badge&labelColor=0d1117&color=161b22" alt="285 authored" /></a>
<a href="https://github.com/search?q=author%3Avtushar06+is%3Apr+is%3Aopen"><img src="https://img.shields.io/badge/75%20IN%20REVIEW-0d1117?style=for-the-badge&labelColor=0d1117&color=161b22" alt="75 open" /></a>

</div>

<img src="https://raw.githubusercontent.com/vtushar06/vtushar06/main/assets/divider.svg" width="100%" alt="" />

## Podman & the LFX Mentorship

<!--
  HONEST STATUS LINE — swap this block the day you are selected.
  After selection, replace the paragraph below with:
  > **LFX Mentee — Podman.** Selected for the <TERM> term, working on <PROJECT> with <MENTOR>.
-->

> **Status: applying, and contributing regardless.** I have not been selected for an LFX term yet.
> What is already true is the work: **14 merged pull requests across `containers/*`**, plus open
> patches in Buildah, `container-libs` and `coreos/go-systemd`. The mentorship would formalise
> something I am doing on evenings and weekends anyway.

Where my container work actually lands — CI correctness and test reliability, the unglamorous half
of a release:

- `hack/ci: pass --remote to bud tests` — remote-mode coverage that was silently skipped
- `test/system: fix healthcheck since race` — a real flake, not a retry
- `hack/ci: rename STORAGE_FS to CI_DESIRED_STORAGE and add _PODMAN_CI`
- `ci: add zizmor workflow` (Skopeo) — static analysis for GitHub Actions supply-chain issues
- `release: publish sha256 checksums for the VM images` (automation)
- `chrootuser: do not let one bad line end the lookup` (Buildah)
- `libimage: do not fail disk usage when an image is removed mid-walk` (container-libs)
- `dlopen: report the dlerror from GetHandle` (`coreos/go-systemd`)

### The tool this taught me to build

<img src="https://raw.githubusercontent.com/vtushar06/vtushar06/main/assets/pipeline.svg" width="100%" alt="ci-flake-triage pipeline: scan, extract, classify, match, report" />

**[`ci-flake-triage`](https://github.com/vtushar06/ci-flake-triage)** — chasing Podman flakes by hand
got old, so I made it mechanical. A job that fails on attempt 1 and passes on attempt 2 with the
*same commit* is a flake by construction, so the rerun history is a labelled dataset nobody was
reading. It walks completed runs, diffs attempts, pulls the failing logs, buckets each flake
(test / designed / infra / no-log), and matches it against open issues.

Three rules it learned the hard way, all of them from being wrong first:

1. **Framework markers only.** Grepping for `error` matches assertion text and invents flakes.
2. **Issue matches are candidates, not conclusions.** It states its reasoning and a human decides.
3. **Job logs lie.** Journal artifacts are ground truth — log diffing pulled `read-only file system`
   straight out of a concurrent-rmi flake that the job log framed as something else entirely.

No ML in the hot path, no CI changes required, read-only GitHub access, and it cannot post anything.

<img src="https://raw.githubusercontent.com/vtushar06/vtushar06/main/assets/divider.svg" width="100%" alt="" />

## Things I built

<table>
<tr>
<td width="50%" valign="top">

### [ci-flake-triage](https://github.com/vtushar06/ci-flake-triage)
`Python` · `GitHub Actions` · `gh CLI`

Confirmed CI flakes out of rerun history — classified, matched to issues, reported weekly. Standard
library only, no CI modifications, no write access.

<img src="https://img.shields.io/badge/Python-0d1117?style=flat-square&logo=python&logoColor=FBBC04" />
<img src="https://img.shields.io/badge/GitHub_Actions-0d1117?style=flat-square&logo=githubactions&logoColor=FBBC04" />

</td>
<td width="50%" valign="top">

### [opencost-welcome-bot](https://github.com/vtushar06/opencost-welcome-bot)
`TypeScript` · `Probot`

Onboarding automation for CNCF OpenCost — greets first-time contributors and points them at the
right docs before a maintainer has to.

<img src="https://img.shields.io/badge/TypeScript-0d1117?style=flat-square&logo=typescript&logoColor=FBBC04" />
<img src="https://img.shields.io/badge/CNCF-0d1117?style=flat-square&logo=cncf&logoColor=FBBC04" />

</td>
</tr>
<tr>
<td width="50%" valign="top">

### [Telesana](https://telesana-appoinment-production.up.railway.app/)
`Next.js` · `PostgreSQL`

Doctor-appointment platform — scheduling, availability windows and patient records, deployed and in
use rather than in a demo folder.

<img src="https://img.shields.io/badge/Next.js-0d1117?style=flat-square&logo=nextdotjs&logoColor=FBBC04" />
<img src="https://img.shields.io/badge/PostgreSQL-0d1117?style=flat-square&logo=postgresql&logoColor=FBBC04" />

</td>
<td width="50%" valign="top">

### [NeuraCoin](https://neura-coin-ten.vercel.app/)
`TypeScript` · `React`

Fintech crypto trading simulator — live market data against virtual balances, so the risk model is
real and the money is not.

<img src="https://img.shields.io/badge/TypeScript-0d1117?style=flat-square&logo=typescript&logoColor=FBBC04" />
<img src="https://img.shields.io/badge/React-0d1117?style=flat-square&logo=react&logoColor=FBBC04" />

</td>
</tr>
<tr>
<td width="50%" valign="top">

### [AstroGPT](https://astrogpt-tushar-vermas-projects-f01f3eda.vercel.app/)
`JavaScript` · `LLM APIs`

Conversational astrology companion — chart context fed into a chat model with a memory layer.

<img src="https://img.shields.io/badge/JavaScript-0d1117?style=flat-square&logo=javascript&logoColor=FBBC04" />
<img src="https://img.shields.io/badge/OpenAI-0d1117?style=flat-square&logo=openai&logoColor=FBBC04" />

</td>
<td width="50%" valign="top">

### [NextFlow](https://next-flow-sigma-eight.vercel.app/) · [Sync-Lite](https://sync-lite.onrender.com) · [PowerOn](https://poweron-events.vercel.app)
`TypeScript` · `Node`

Workflow tooling, a lightweight sync service, and an event platform — the side projects that keep
the product half of my brain warm.

<img src="https://img.shields.io/badge/TypeScript-0d1117?style=flat-square&logo=typescript&logoColor=FBBC04" />
<img src="https://img.shields.io/badge/Node.js-0d1117?style=flat-square&logo=nodedotjs&logoColor=FBBC04" />

</td>
</tr>
</table>

<img src="https://raw.githubusercontent.com/vtushar06/vtushar06/main/assets/divider.svg" width="100%" alt="" />

## Tools I actually reach for

<div align="center">

**Languages**

<img src="https://img.shields.io/badge/Python-0d1117?style=for-the-badge&logo=python&logoColor=FBBC04&labelColor=0d1117&color=161b22" />
<img src="https://img.shields.io/badge/Go-0d1117?style=for-the-badge&logo=go&logoColor=FBBC04&labelColor=0d1117&color=161b22" />
<img src="https://img.shields.io/badge/TypeScript-0d1117?style=for-the-badge&logo=typescript&logoColor=FBBC04&labelColor=0d1117&color=161b22" />
<img src="https://img.shields.io/badge/C%2B%2B-0d1117?style=for-the-badge&logo=cplusplus&logoColor=FBBC04&labelColor=0d1117&color=161b22" />
<img src="https://img.shields.io/badge/Bash-0d1117?style=for-the-badge&logo=gnubash&logoColor=FBBC04&labelColor=0d1117&color=161b22" />
<img src="https://img.shields.io/badge/SQL-0d1117?style=for-the-badge&logo=postgresql&logoColor=FBBC04&labelColor=0d1117&color=161b22" />

**Containers, cloud & CI**

<img src="https://img.shields.io/badge/Podman-0d1117?style=for-the-badge&logo=podman&logoColor=FBBC04&labelColor=0d1117&color=161b22" />
<img src="https://img.shields.io/badge/Docker-0d1117?style=for-the-badge&logo=docker&logoColor=FBBC04&labelColor=0d1117&color=161b22" />
<img src="https://img.shields.io/badge/Kubernetes-0d1117?style=for-the-badge&logo=kubernetes&logoColor=FBBC04&labelColor=0d1117&color=161b22" />
<img src="https://img.shields.io/badge/GitHub_Actions-0d1117?style=for-the-badge&logo=githubactions&logoColor=FBBC04&labelColor=0d1117&color=161b22" />
<img src="https://img.shields.io/badge/Linux-0d1117?style=for-the-badge&logo=linux&logoColor=FBBC04&labelColor=0d1117&color=161b22" />
<img src="https://img.shields.io/badge/Git-0d1117?style=for-the-badge&logo=git&logoColor=FBBC04&labelColor=0d1117&color=161b22" />

**Web & data**

<img src="https://img.shields.io/badge/React-0d1117?style=for-the-badge&logo=react&logoColor=FBBC04&labelColor=0d1117&color=161b22" />
<img src="https://img.shields.io/badge/Next.js-0d1117?style=for-the-badge&logo=nextdotjs&logoColor=FBBC04&labelColor=0d1117&color=161b22" />
<img src="https://img.shields.io/badge/Node.js-0d1117?style=for-the-badge&logo=nodedotjs&logoColor=FBBC04&labelColor=0d1117&color=161b22" />
<img src="https://img.shields.io/badge/Django-0d1117?style=for-the-badge&logo=django&logoColor=FBBC04&labelColor=0d1117&color=161b22" />
<img src="https://img.shields.io/badge/Tailwind-0d1117?style=for-the-badge&logo=tailwindcss&logoColor=FBBC04&labelColor=0d1117&color=161b22" />
<img src="https://img.shields.io/badge/PostgreSQL-0d1117?style=for-the-badge&logo=postgresql&logoColor=FBBC04&labelColor=0d1117&color=161b22" />
<img src="https://img.shields.io/badge/MongoDB-0d1117?style=for-the-badge&logo=mongodb&logoColor=FBBC04&labelColor=0d1117&color=161b22" />
<img src="https://img.shields.io/badge/JSON_Schema-0d1117?style=for-the-badge&logo=json&logoColor=FBBC04&labelColor=0d1117&color=161b22" />

</div>

<img src="https://raw.githubusercontent.com/vtushar06/vtushar06/main/assets/divider.svg" width="100%" alt="" />

## Where I've been

<div align="center">

| | Role | Where | What came out of it |
|:--:|:--|:--|:--|
| **`now`** | Software Engineer | **Mugafi** | Product engineering on an AI-first content platform |
| **`now`** | CTO | **Shivam-Info** | Technical direction, architecture and delivery |
| **`'26`** | GSoC Contributor | **JSON Schema** | 78 merged — format assertions and RFC conformance |
| **`ongoing`** | Upstream contributor | **containers · OpenCost · Headlamp · sourcemeta** | CI reliability, tests, release tooling |

</div>

<img src="https://raw.githubusercontent.com/vtushar06/vtushar06/main/assets/divider.svg" width="100%" alt="" />

## The graphs

<div align="center">

<img width="49%" src="https://github-readme-stats.vercel.app/api?username=vtushar06&show_icons=true&hide_border=true&count_private=true&include_all_commits=true&bg_color=0d1117&title_color=FBBC04&icon_color=FFD54F&text_color=c9d1d9&custom_title=GitHub%20Analytics" alt="GitHub stats" />
<img width="49%" src="https://streak-stats.demolab.com?user=vtushar06&hide_border=true&background=0d1117&stroke=FBBC04&ring=FBBC04&fire=F59E0B&currStreakLabel=FBBC04&currStreakNum=FFD54F&sideNums=FFD54F&sideLabels=c9d1d9&dates=8b949e" alt="Streak" />

<img width="49%" src="https://github-readme-stats.vercel.app/api/top-langs/?username=vtushar06&layout=compact&hide_border=true&langs_count=10&bg_color=0d1117&title_color=FBBC04&text_color=c9d1d9&custom_title=Languages" alt="Top languages" />

<br><br>

<picture>
  <source media="(prefers-color-scheme: dark)"  srcset="https://raw.githubusercontent.com/vtushar06/vtushar06/output/github-snake-dark.svg" />
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/vtushar06/vtushar06/output/github-snake.svg" />
  <img src="https://raw.githubusercontent.com/vtushar06/vtushar06/output/github-snake.svg" width="100%" alt="Contribution snake" />
</picture>

<img src="https://github-readme-activity-graph.vercel.app/graph?username=vtushar06&bg_color=0d1117&color=FFD54F&line=FBBC04&point=F59E0B&area=true&area_color=FBBC04&hide_border=true&custom_title=Contribution%20Rhythm" width="100%" alt="Activity graph" />

<img src="https://github-profile-trophy.vercel.app/?username=vtushar06&theme=gruvbox&no-frame=true&no-bg=true&column=7&margin-w=8&margin-h=8" alt="Trophies" />

</div>

<img src="https://raw.githubusercontent.com/vtushar06/vtushar06/main/assets/divider.svg" width="100%" alt="" />

## Say hello

<div align="center">

If you maintain something and you have a flaky test you have stopped trusting, or a spec corner
nobody has written coverage for — that is the message I most want to get.

<br>

<a href="mailto:tusharmyself06@gmail.com">
  <img src="https://img.shields.io/badge/tusharmyself06%40gmail.com-FBBC04?style=for-the-badge&logo=gmail&logoColor=0d1117&labelColor=FBBC04" alt="Email" /></a>
<a href="https://www.linkedin.com/in/tushar-verma-851a76338/">
  <img src="https://img.shields.io/badge/LinkedIn-0d1117?style=for-the-badge&logo=linkedin&logoColor=FBBC04&labelColor=0d1117&color=161b22" alt="LinkedIn" /></a>
<a href="https://tushar-portfolio.netlify.app">
  <img src="https://img.shields.io/badge/Portfolio-0d1117?style=for-the-badge&logo=firefoxbrowser&logoColor=FBBC04&labelColor=0d1117&color=161b22" alt="Portfolio" /></a>
<a href="https://x.com/TusharV76610577">
  <img src="https://img.shields.io/badge/X-0d1117?style=for-the-badge&logo=x&logoColor=FBBC04&labelColor=0d1117&color=161b22" alt="X" /></a>

<br><br>

<a href="https://holopin.io/@vtushar06">
  <img src="https://holopin.me/vtushar06" alt="Holopin badge board" width="70%" />
</a>

<br>

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:F59E0B,50:FBBC04,100:FFD54F&height=140&section=footer" width="100%" alt="" />

<sub><i>Read the spec. Reproduce the failure. Land the smallest correct patch.</i></sub>

</div>

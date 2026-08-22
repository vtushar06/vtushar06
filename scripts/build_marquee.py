#!/usr/bin/env python3
"""Build the sliding upstream-logo marquee shown under the header.

GitHub strips <style> and CSS from README HTML, so a marquee has to be a single
self-contained SVG. Every logo is inlined as a base64 data URI, the strip is
duplicated end to end, and the pair is translated by exactly one strip width so
the loop is seamless. Two variants are emitted because several of these logos
ship dark lettering that vanishes on GitHub's dark theme.
"""

import base64
import os
import re
import xml.etree.ElementTree as ET

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ASSETS = os.path.join(ROOT, "assets")

H = 64          # canvas height
GAP = 62        # space between logos
PAD = 40        # leading pad before the first logo
DUR = "30s"     # one full cycle

# (file_light, file_dark, display_height, label)
LOGOS = [
    ("gsoc-sun.svg", "gsoc-sun.svg", 40, "Google Summer of Code"),
    ("jsonschema-logo.svg", "jsonschema-logo-white.svg", 34, "JSON Schema"),
    ("podman-logo.png", "podman-logo.png", 28, "Podman"),
    ("sourcemeta-logo.png", "sourcemeta-logo.png", 38, "Sourcemeta"),
    ("learningequality-logo.png", "learningequality-logo.png", 40, "Learning Equality"),
    ("opencost-logo.svg", "opencost-logo.svg", 40, "OpenCost"),
    ("headlamp-logo.svg", "headlamp-logo-light.svg", 36, "Headlamp"),
    ("mugafi-logo.jpg", "mugafi-logo.jpg", 38, "Mugafi"),
]

MIME = {".svg": "image/svg+xml", ".png": "image/png", ".jpg": "image/jpeg"}


def intrinsic_size(path):
    ext = os.path.splitext(path)[1].lower()
    if ext == ".svg":
        root = ET.parse(path).getroot()
        vb = root.get("viewBox")
        if vb:
            parts = [float(x) for x in re.split(r"[ ,]+", vb.strip())]
            return parts[2], parts[3]
        w = float(re.sub(r"[^\d.]", "", root.get("width", "100")))
        h = float(re.sub(r"[^\d.]", "", root.get("height", "100")))
        return w, h
    from PIL import Image
    with Image.open(path) as im:
        return float(im.width), float(im.height)


def data_uri(path, disp_h=None):
    """Inline a file as a data URI, downsampling rasters to 2x display height.

    Embedding a 200px logo that renders at 40px triples the file size for no
    visible gain, and this SVG ships in every README view."""
    ext = os.path.splitext(path)[1].lower()
    if ext in (".png", ".jpg") and disp_h:
        import io
        from PIL import Image
        with Image.open(path) as im:
            target = int(disp_h * 2)
            if im.height > target:
                im = im.convert("RGBA" if ext == ".png" else "RGB")
                im = im.resize((max(1, round(im.width * target / im.height)), target), Image.LANCZOS)
                buf = io.BytesIO()
                im.save(buf, format="PNG" if ext == ".png" else "JPEG", optimize=True, quality=88)
                return f"data:{MIME[ext]};base64," + base64.b64encode(buf.getvalue()).decode()
    with open(path, "rb") as fh:
        return f"data:{MIME[ext]};base64," + base64.b64encode(fh.read()).decode()


def build(variant):
    idx = 0 if variant == "light" else 1
    items, x = [], PAD
    for files in LOGOS:
        name = files[idx]
        path = os.path.join(ASSETS, name)
        iw, ih = intrinsic_size(path)
        disp_h = files[2]
        disp_w = iw * (disp_h / ih)
        items.append((data_uri(path, disp_h), x, (H - disp_h) / 2, disp_w, disp_h, files[3]))
        x += disp_w + GAP
    strip = x - GAP + PAD

    def render(offset):
        return "\n".join(
            f'      <image href="{uri}" x="{ix + offset:.1f}" y="{iy:.1f}" '
            f'width="{iwd:.1f}" height="{ihd:.1f}" preserveAspectRatio="xMidYMid meet"><title>{label}</title></image>'
            for uri, ix, iy, iwd, ihd, label in items
        )

    return f'''<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="1000" height="{H}" viewBox="0 0 1000 {H}" fill="none" role="img" aria-label="Upstream organisations: {', '.join(l[3] for l in LOGOS)}">
  <defs>
    <linearGradient id="fade" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="#fff" stop-opacity="0"/>
      <stop offset="7%" stop-color="#fff" stop-opacity="1"/>
      <stop offset="93%" stop-color="#fff" stop-opacity="1"/>
      <stop offset="100%" stop-color="#fff" stop-opacity="0"/>
    </linearGradient>
    <mask id="edges"><rect width="1000" height="{H}" fill="url(#fade)"/></mask>
    <style>
      @keyframes slide {{ from {{ transform: translateX(0) }} to {{ transform: translateX(-{strip:.1f}px) }} }}
      .track {{ animation: slide {DUR} linear infinite; }}
      @media (prefers-reduced-motion: reduce) {{ .track {{ animation: none; }} }}
    </style>
  </defs>
  <g mask="url(#edges)">
    <g class="track">
{render(0)}
{render(strip)}
    </g>
  </g>
</svg>
'''


if __name__ == "__main__":
    for variant in ("light", "dark"):
        out = os.path.join(ASSETS, f"logo-marquee-{variant}.svg")
        with open(out, "w") as fh:
            fh.write(build(variant))
        print(f"{out}  {os.path.getsize(out) // 1024} KB")

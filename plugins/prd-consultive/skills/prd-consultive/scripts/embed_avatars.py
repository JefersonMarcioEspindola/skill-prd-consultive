#!/usr/bin/env python3
"""Embeds the board photos into PRD.html as data URIs.

Usage:
    python scripts/embed_avatars.py path/PRD.html [--board images/folder]

Looks for elements with class="avatar" and data-persona (and data-signal, optional).
For each one, uses the first image found in assets/board/:
    <persona>-<signal>.(webp|png|jpg|jpeg)  then  <persona>-neutral.(...)
If none exists, the initials stay. Running it twice doesn't duplicate anything.
Standard library only; if Pillow is installed, images are shrunk to 256 px.
"""

import argparse
import base64
import html
import io
import re
import sys
from pathlib import Path

EXTENSIONS = ("webp", "png", "jpg", "jpeg")
MIME = {"webp": "image/webp", "png": "image/png", "jpg": "image/jpeg", "jpeg": "image/jpeg"}
NAMES = {"helena": "Helena", "caio": "Caio", "bia": "Bia", "lucas": "Lucas", "teo": "Téo", "lucia": "Dr. Lúcia"}
MAX_SIDE = 256
WARN_KB = 300

AVATAR = re.compile(
    r'(?P<open><(?P<tag>div|span)\b[^>]*\bclass="avatar"[^>]*>)'
    r'(?P<inside>\s*(?:<span>[^<]*</span>|<img\b[^>]*>)\s*)'
    r'(?P<close></(?P=tag)>)'
)


def attribute(open_tag, name):
    m = re.search(rf'\b{name}="([^"]*)"', open_tag)
    return m.group(1) if m else None


def find_image(folder, persona, signal):
    states = [signal, "neutral"] if signal and signal != "neutral" else ["neutral"]
    for state in states:
        for ext in EXTENSIONS:
            path = folder / f"{persona}-{state}.{ext}"
            if path.exists():
                return path
    return None


def data_uri(path, cache):
    if path in cache:
        return cache[path]
    data = path.read_bytes()
    mime = MIME[path.suffix.lstrip(".").lower()]
    try:
        from PIL import Image

        img = Image.open(io.BytesIO(data))
        if max(img.size) > MAX_SIDE:
            img.thumbnail((MAX_SIDE, MAX_SIDE))
            out = io.BytesIO()
            img.save(out, format="WEBP", quality=82)
            data, mime = out.getvalue(), "image/webp"
    except ImportError:
        pass
    except Exception as error:  # odd image: embed it as is
        print(f"warning: couldn't shrink {path.name} ({error})", file=sys.stderr)
    if len(data) > WARN_KB * 1024:
        print(f"warning: {path.name} is {len(data) // 1024} KB; shrink it to ~{MAX_SIDE}px", file=sys.stderr)
    uri = f"data:{mime};base64,{base64.b64encode(data).decode('ascii')}"
    cache[path] = uri
    return uri


def main():
    skill_root = Path(__file__).resolve().parent.parent
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("html", type=Path)
    parser.add_argument("--board", type=Path, default=skill_root / "assets" / "board")
    args = parser.parse_args()

    if not args.html.exists():
        sys.exit(f"error: {args.html} doesn't exist")

    text = args.html.read_text(encoding="utf-8")
    cache, embedded, initials = {}, [], []

    def replace(m):
        persona = attribute(m.group("open"), "data-persona")
        if not persona:
            return m.group(0)
        signal = attribute(m.group("open"), "data-signal")
        image = find_image(args.board, persona, signal)
        label = f"{persona}-{signal or 'neutral'}"
        if image is None:
            initials.append(label)
            return m.group(0)
        embedded.append(f"{label} <- {image.name}")
        alt = html.escape(NAMES.get(persona, persona.capitalize()))
        img = f'<img src="{data_uri(image, cache)}" alt="{alt}">'
        return f'{m.group("open")}{img}{m.group("close")}'

    new = AVATAR.sub(replace, text)
    args.html.write_text(new, encoding="utf-8")

    print(f"{len(embedded)} avatar(s) with a photo, {len(initials)} with initials.")
    for line in embedded:
        print(f"  photo: {line}")
    if initials:
        print(f"  no image in {args.board}: {', '.join(sorted(set(initials)))}")


if __name__ == "__main__":
    main()

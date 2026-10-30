#!/usr/bin/env python3
"""Embute as fotos da banca dentro do PRD.html, como data URI.

Uso:
    python scripts/embutir_avatares.py caminho/PRD.html [--banca pasta/das/imagens]

Procura elementos com class="avatar" e data-persona (e data-sinal, opcional).
Para cada um, usa a primeira imagem que existir em assets/banca/:
    <persona>-<sinal>.(webp|png|jpg|jpeg)  e depois  <persona>-neutro.(...)
Se nenhuma existir, mantém as iniciais. Rodar duas vezes não duplica nada.
Só usa a biblioteca padrão; se o Pillow estiver instalado, reduz as imagens para 256 px.
"""

import argparse
import base64
import html
import io
import re
import sys
from pathlib import Path

EXTENSOES = ("webp", "png", "jpg", "jpeg")
MIME = {"webp": "image/webp", "png": "image/png", "jpg": "image/jpeg", "jpeg": "image/jpeg"}
LADO_MAX = 256
AVISO_KB = 300

AVATAR = re.compile(
    r'(?P<abre><(?P<tag>div|span)\b[^>]*\bclass="avatar"[^>]*>)'
    r'(?P<dentro>\s*(?:<span>[^<]*</span>|<img\b[^>]*>)\s*)'
    r'(?P<fecha></(?P=tag)>)'
)


def atributo(tag_aberta, nome):
    m = re.search(rf'\b{nome}="([^"]*)"', tag_aberta)
    return m.group(1) if m else None


def achar_imagem(pasta, persona, sinal):
    estados = [sinal, "neutro"] if sinal and sinal != "neutro" else ["neutro"]
    for estado in estados:
        for ext in EXTENSOES:
            caminho = pasta / f"{persona}-{estado}.{ext}"
            if caminho.exists():
                return caminho
    return None


def data_uri(caminho, cache):
    if caminho in cache:
        return cache[caminho]
    dados = caminho.read_bytes()
    mime = MIME[caminho.suffix.lstrip(".").lower()]
    try:
        from PIL import Image

        img = Image.open(io.BytesIO(dados))
        if max(img.size) > LADO_MAX:
            img.thumbnail((LADO_MAX, LADO_MAX))
            saida = io.BytesIO()
            img.save(saida, format="WEBP", quality=82)
            dados, mime = saida.getvalue(), "image/webp"
    except ImportError:
        pass
    except Exception as erro:  # imagem estranha: embute como veio
        print(f"aviso: não consegui reduzir {caminho.name} ({erro})", file=sys.stderr)
    if len(dados) > AVISO_KB * 1024:
        print(f"aviso: {caminho.name} tem {len(dados) // 1024} KB; reduza para ~{LADO_MAX}px", file=sys.stderr)
    uri = f"data:{mime};base64,{base64.b64encode(dados).decode('ascii')}"
    cache[caminho] = uri
    return uri


def main():
    raiz_skill = Path(__file__).resolve().parent.parent
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("html", type=Path)
    parser.add_argument("--banca", type=Path, default=raiz_skill / "assets" / "banca")
    args = parser.parse_args()

    if not args.html.exists():
        sys.exit(f"erro: {args.html} não existe")

    texto = args.html.read_text(encoding="utf-8")
    cache, embutidas, iniciais = {}, [], []

    def trocar(m):
        persona = atributo(m.group("abre"), "data-persona")
        if not persona:
            return m.group(0)
        sinal = atributo(m.group("abre"), "data-sinal")
        imagem = achar_imagem(args.banca, persona, sinal)
        rotulo = f"{persona}-{sinal or 'neutro'}"
        if imagem is None:
            iniciais.append(rotulo)
            return m.group(0)
        embutidas.append(f"{rotulo} ← {imagem.name}")
        alt = html.escape(persona.capitalize())
        img = f'<img src="{data_uri(imagem, cache)}" alt="{alt}">'
        return f'{m.group("abre")}{img}{m.group("fecha")}'

    novo = AVATAR.sub(trocar, texto)
    args.html.write_text(novo, encoding="utf-8")

    print(f"{len(embutidas)} avatar(es) com foto, {len(iniciais)} com iniciais.")
    for linha in embutidas:
        print(f"  foto: {linha}")
    if iniciais:
        print(f"  sem imagem em {args.banca}: {', '.join(sorted(set(iniciais)))}")


if __name__ == "__main__":
    main()

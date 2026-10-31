#!/usr/bin/env python3
"""Gera os pacotes da skill em dist/.

    python3 tools/build.py

- dist/prd-consultive.zip: a pasta completa (claude.ai, ChatGPT, Gemini e agentes de código).
- dist/SKILL.md: tudo em um arquivo só, para apps que aceitam apenas um SKILL.md.
  Leva o texto das referências, do perfil e do esqueleto HTML; as fotos ficam pelo link publicado.
"""

import re
import zipfile
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
SKILL = RAIZ / "plugins" / "prd-consultive" / "skills" / "prd-consultive"
DIST = RAIZ / "dist"
ANEXOS = [
    "perfil.md",
    "references/processo.md",
    "references/banca.md",
    "references/entrevista.md",
    "references/stack.md",
    "references/prd-template.md",
    "references/plano-template.md",
    "references/html.md",
    "assets/skeleton.html",
]
AVISO = (
    "\n> **Versão em arquivo único.** Os arquivos que este documento cita (`perfil.md`, `references/...`, "
    "`assets/skeleton.html`) estão anexados no fim, cada um sob o título `Anexo: <caminho>`. "
    "Leia o anexo quando o texto mandar ler o arquivo. O script de fotos não vem nesta versão: "
    "use as fotos pelo link publicado (veja o anexo `references/html.md`).\n"
)


def zip_completo():
    destino = DIST / "prd-consultive.zip"
    with zipfile.ZipFile(destino, "w", zipfile.ZIP_DEFLATED) as z:
        for arquivo in sorted(SKILL.rglob("*")):
            if arquivo.is_file() and arquivo.name != ".DS_Store" and "__pycache__" not in arquivo.parts:
                z.write(arquivo, Path("prd-consultive") / arquivo.relative_to(SKILL))
    return destino


def arquivo_unico():
    texto = (SKILL / "SKILL.md").read_text(encoding="utf-8")
    fim_frontmatter = texto.index("\n---", 4) + 4
    partes = [texto[:fim_frontmatter], AVISO, texto[fim_frontmatter:]]
    for caminho in ANEXOS:
        conteudo = (SKILL / caminho).read_text(encoding="utf-8").rstrip()
        cerca = "````html" if caminho.endswith(".html") else None
        partes.append(f"\n\n---\n\n# Anexo: {caminho}\n\n")
        partes.append(f"{cerca}\n{conteudo}\n````" if cerca else re.sub(r"(?m)^# ", "## ", conteudo))
    destino = DIST / "SKILL.md"
    destino.write_text("".join(partes) + "\n", encoding="utf-8")
    return destino


if __name__ == "__main__":
    DIST.mkdir(exist_ok=True)
    for gerado in (zip_completo(), arquivo_unico()):
        print(f"{gerado.relative_to(RAIZ)}  {gerado.stat().st_size // 1024} KB")

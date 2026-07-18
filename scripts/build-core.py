#!/usr/bin/env python3
"""
IA-Productiva - Script de construcció del Core
Executa totes les fases per deixar el projecte operatiu.
"""

import os
from pathlib import Path

# ============================================
# FASE 1: Estructura de carpetes
# ============================================
FOLDERS = [
    "content/prompts",
    "content/templates",
    "resources/snippets",
    "resources/checklists",
    "automation/github",
    "automation/scripts",
    "website/pages",
    "branding",
    "assets/images",
    "assets/icons",
    "analytics",
    "archive",
]

def create_folders():
    print("📁 Fase 1: Creant estructura de carpetes...")
    for folder in FOLDERS:
        path = Path.cwd() / folder
        path.mkdir(parents=True, exist_ok=True)
        # Crear .gitkeep per mantenir carpetes buides
        (path / ".gitkeep").touch()
        print(f"  ✅ {path}")
    print("✅ Fase 1 completada.\n")

# ============================================
# FASE 2: Documentació essencial
# ============================================
def create_documentation():
    print("📄 Fase 2: Creant documentació essencial...")

    # README.md
    readme = """# IA-Productiva

Framework per a desenvolupament assistit per IA amb memòria de context.

## Objectiu

Convertir qualsevol IA (Claude, ChatGPT, Gemini, DeepSeek...) en un desenvolupador autònom que recorda el context del projecte.

## Com funciona

1. Defineix el teu projecte amb fitxers de context (`PROJECT.md`, `TODO.md`, etc.)
2. Executa `ia-productiva run` per carregar el context i obtenir la següent tasca
3. La IA analitza, planifica i executa sense que li hagis d'explicar el projecte cada cop

## Instal·lació

```bash
git clone https://github.com/eduardcasellas/ia-productiva.git
cd ia-productiva
python3 -m venv venv
source venv/bin/activate
pip install -e .
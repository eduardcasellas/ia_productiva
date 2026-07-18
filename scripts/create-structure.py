#!/usr/bin/env python3
import os
from pathlib import Path

# Definir l'estructura de carpetes basada en l'arquitectura
folders = [
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

# Crear carpetes a l'arrel del projecte (on s'executa l'script)
project_root = Path.cwd()
for folder in folders:
    path = project_root / folder
    path.mkdir(parents=True, exist_ok=True)
    print(f"✅ Creat: {path}")

print("\n📁 Estructura de carpetes completada.")
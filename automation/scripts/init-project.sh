#!/bin/bash
# Script per inicialitzar l'estructura del projecte
# Crea carpetes i fitxers .gitkeep si falten

echo "Inicialitzant estructura del projecte..."

# Definir les carpetes necessàries segons l'arquitectura
directories=(
  "content/prompts"
  "content/templates"
  "resources/snippets"
  "resources/checklists"
  "automation/github"
  "automation/scripts"
  "website/pages"
  "branding"
  "assets/images"
  "assets/icons"
  "analytics"
  "archive"
)

# Crear carpetes i .gitkeep
for dir in "${directories[@]}"; do
  if [ ! -d "$dir" ]; then
    mkdir -p "$dir"
    echo "✅ Creada carpeta: $dir"
  else
    echo "⏭️  Ja existeix: $dir"
  fi
done

# Afegir .gitkeep a carpetes buides
find . -type d -empty -not -path "./.git/*" -exec touch {}/.gitkeep \;

echo ""
echo "✅ Inicialització completada"

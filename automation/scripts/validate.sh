#!/bin/bash
# Script per validar el projecte localment
# Replica les comprovacions dels workflows de GitHub Actions

errors=0
warnings=0

echo "=== Validació del projecte ==="
echo ""

# 1. Comprovar format Markdown
echo "--- Comprovant format Markdown ---"
if command -v markdownlint &> /dev/null; then
  markdownlint '**/*.md' --ignore node_modules || true
  echo "✅ Markdown validat"
else
  echo "⚠️  markdownlint no disponible. Instal·la: npm install -g markdownlint-cli"
  warnings=$((warnings + 1))
fi
echo ""

# 2. Verificar convencions
echo "--- Verificant convencions ---"
# Comprovar noms de fitxers
bad_files=$(find . -type f -name '*[A-Z]*' -o -name '* *' | grep -v '.git/' | grep -v 'node_modules/' | head -5)
if [ -n "$bad_files" ]; then
  echo "❌ Fitxers que no segueixen les convencions:"
  echo "$bad_files"
  errors=$((errors + 1))
else
  echo "✅ Tots els fitxers segueixen les convencions"
fi
echo ""

# 3. Comprovar estructura de carpetes
echo "--- Comprovant estructura de carpetes ---"
required_dirs="content/prompts content/templates resources/snippets resources/checklists automation/github automation/scripts website/pages branding assets/images assets/icons analytics archive"
missing=0
for dir in $required_dirs; do
  if [ ! -d "$dir" ]; then
    echo "❌ Falta carpeta: $dir"
    missing=$((missing + 1))
  fi
done
if [ $missing -eq 0 ]; then
  echo "✅ Estructura de carpetes correcta"
else
  errors=$((errors + missing))
fi
echo ""

# 4. Comprovar enllaços interns
echo "--- Comprovant enllaços interns ---"
if command -v lychee &> /dev/null; then
  lychee --no-progress --exclude 'https?://' '**/*.md' || true
  echo "✅ Enllaços verificats"
else
  echo "⚠️  lychee no disponible. Instal·la: sudo apt-get install lychee"
  warnings=$((warnings + 1))
fi
echo ""

# Resum
echo "=== Resum ==="
echo "Errors: $errors"
echo "Warnings: $warnings"
if [ $errors -eq 0 ]; then
  echo "✅ Validació completada"
else
  echo "❌ Corregeix els errors abans de fer push"
fi

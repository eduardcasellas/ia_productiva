#!/usr/bin/env python3
from pathlib import Path

# --------------------------------------------
# FASE 3: Prompts inicials
# --------------------------------------------
prompts = {
    "content/prompts/init-context.md": """# Prompt de configuració inicial

## Objectiu
Carregar el context d'un projecte per primera vegada i establir la línia base.

## Instruccions
1. Llegeix PROJECT_RULES.md, PROJECT.md, TODO.md, SESSION.md i docs/*.
2. Identifica l'estat actual del projecte.
3. Proposa la següent tasca segons TODO.md.
4. No generis codi encara, només anàlisi i planificació.
""",
    "content/prompts/generate-doc.md": """# Prompt de generació de documentació

## Objectiu
Crear nous documents seguint les convencions del projecte.

## Instruccions
1. Llegeix les convencions (docs/conventions.md).
2. Utilitza la template de document (content/templates/doc-template.md).
3. Genera el contingut seguint l'estructura definida.
4. Verifica que compleix les regles de nomenclatura.
""",
    "content/prompts/validate-content.md": """# Prompt de revisió

## Objectiu
Validar que el codi o documentació compleix les regles i convencions.

## Instruccions
1. Llegeix el document a revisar.
2. Comprova que segueix les convencions (docs/conventions.md).
3. Verifica enllaços interns i coherència.
4. Proposa correccions si cal.
"""
}

# --------------------------------------------
# FASE 4: Templates
# --------------------------------------------
templates = {
    "content/templates/template-document.md": """# Títol del Document

## Propòsit
Explica per què existeix aquest document.

## Abast
Què cobreix i què no.

## Contingut
Desenvolupament del tema principal.

## Referències
- [Document relacionat 1](ruta)
- [Document relacionat 2](ruta)

## Historial
- Data de creació: YYYY-MM-DD
- Última modificació: YYYY-MM-DD
""",
    "content/templates/template-prompt.md": """# [Nom del Prompt]

## Objectiu
Què es pretén aconseguir amb aquest prompt.

## Context
Informació que la IA ha de conèixer abans de respondre.

## Instruccions
Passos concrets que ha de seguir la IA.
"""
}

## Exemple de sortida
#!/usr/bin/env python3
import os
import re

PROMPTS_DIR = "content/prompts"
os.makedirs(PROMPTS_DIR, exist_ok=True)

# Llista de noms de prompts (els que tenim actualment)
prompt_names = [
    "analista-competencia",
    "analista-seo",
    "analitzador-idees",
    "arquitecte-saas",
    "auditor-projecte",
    "consultor-automatitzacio",
    "creador-documentacio",
    "creador-mvp",
    "creador-productes",
    "estratega-contingut",
    "estratega-monetitzacio",
    "generador-contingut",
    "generador-saas",
    "investigador-mercat",
    "investigador-tecnologies",
    "mentor-programacio",
    "optimitzador-codi",
    "optimitzador-prompts",
    "planificador-projectes",
    "revisor-critic",
    "system",
    "generate-doc",
    "init-context",
    "validate-content"
]

# Estructura base per a cada prompt (amb les seccions requerides)
BASE_CONTENT = """# Prompt: {titulo}

## Rol

[Descripció del rol de la IA, ex: "Ets un expert en màrqueting digital"]

## Tasca

[Descripció clara de la tasca que ha de realitzar la IA]

## Format

[Especifica com ha de ser la resposta: llista, paràgrafs, taula, etc.]

## To

[Defineix el to de la resposta: professional, divulgatiu, entusiasta, etc.]

## Variables

[Llista de variables que l'usuari ha de substituir, ex: [nom_producte], [public_objectiu]]

## Exemple d'ús

[Breu exemple amb variables substituïdes]

## Restriccions

- [Restricció 1]
- [Restricció 2]
"""

def generar_prompt(nom):
    """Genera un prompt amb l'estructura correcta."""
    titol = nom.replace("-", " ").title()
    return BASE_CONTENT.format(titulo=titol)

def main():
    for nom in prompt_names:
        fitxer = os.path.join(PROMPTS_DIR, f"{nom}.md")
        contingut = generar_prompt(nom)
        with open(fitxer, "w", encoding="utf-8") as f:
            f.write(contingut)
        print(f"✅ Regenerat: {nom}.md")

    print(f"\n🎉 Tots els prompts regenerats a {PROMPTS_DIR}/")

if __name__ == "__main__":
    main()
EOF
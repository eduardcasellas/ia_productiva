# CORE-02

Afegits GitHub Actions, tasques VS Code, scripts i plantilles.


## Resposta de la IA (ia_productiva)

Analitzant el context i la tasca segons l'arquitectura IA-Productiva.

**Anàlisi:**
- El Core està complet (fases 1-6).
- La Fase 7 requereix contingut inicial real.
- La primera tasca és ampliar el README per convertir-lo en una guia ràpida d'inici.
- Cal seguir les convencions: fitxers en lowercase, markdown estructurat, contingut en català/castellà.

**Solució proposada:**
Ampliar `README.md` amb:
1. Què és IA-Productiva (missió)
2. Per a qui és (públic objectiu)
3. Estructura del repositori (visible)
4. Com començar en 5 minuts (guia ràpida)
5. Exemple pràctic mínim
6. Enllaços a documentació clau

```python
import os

readme_content = """# IA-Productiva

Framework obert per ensenyar i aplicar IA pràctica en català i castellà.

---

## Missió

Ensenyar a persones i empreses a utilitzar la intel·ligència artificial de forma pràctica, productiva i ètica, en català i castellà.

---

## Per a qui és?

- Professionals que volen automatitzar tasques repetitives
- Empreses que busquen integrar IA en els seus processos
- Creadors de contingut que volen produir més ràpid
- Desenvolupadors que necessiten prompts fiables i reutilitzables
- Qualsevol persona que vulgui aprendre IA aplicada

---

## Estructura del repositori

```
ia-productiva/
├── README.md              ← Aquest fitxer
├── PROJECT.md             ← Missió del projecte
├── PROJECT_RULES.md       ← Regles fonamentals
├── TODO.md                ← Tasques pendents
├── SESSION.md             ← Progrés de la sessió actual
├── ROADMAP.md             ← Full de ruta
├── docs/                  ← Documentació del framework
│   ├── architecture.md    ← Arquitectura i principis
│   ├── conventions.md     ← Convencions
│   ├── ai-behavior.md     ← Comportament esperat de la IA
│   ├── context-loading.md ← Com carregar context
│   └── decision-log.md    ← Registre de decisions
├── content/               ← Actius de producció
│   ├── prompts/           ← Prompts reutilitzables
│   └── templates/         ← Plantilles
├── resources/             ← Material de suport
│   ├── snippets/          ← Fragments reutilitzables
│   └── checklists/        ← Llistes de verificació
├── automation/            ← Automatitzacions i workflows
├── website/               ← Lloc web de documentació
├── branding/              ← Identitat visual
├── assets/                ← Recursos estàtics
├── analytics/             ← Mètriques del projecte
└── archive/               ← Informació històrica
```

---

## Com començar en 5 minuts

### 1. Clona el repositori

```bash
git clone https://github.com/el-teu-usuari/ia-productiva.git
cd ia-productiva
```

### 2. Llegeix les regles

Comença per `PROJECT_RULES.md` per entendre les regles fonamentals.

### 3. Explora la documentació

Revisa `docs/architecture.md` per entendre l'arquitectura i `docs/conventions.md` per les convencions.

### 4. Utilitza un prompt

Ves a `content/prompts/` i tria un prompt per a la teva tasca.

### 5. Genera contingut

Segueix les instruccions del prompt i aplica les plantilles de `content/templates/`.

---

## Exemple pràctic mínim

**Objectiu:** Generar una descripció de producte per a una botiga online.

**Passos:**

1. Obre `content/prompts/generar-descripcio-producte.md`
2. Substitueix les variables entre claudàtors: `[nom_producte]`, `[caracteristiques]`
3. Proporciona el prompt a qualsevol IA (ChatGPT, Claude, Gemini...)
4. Obtindràs una descripció estructurada i ready-to-use

---

## Documentació clau

| Document | Descripció |
|----------|------------|
| PROJECT.md | Missió i visió del projecte |
| PROJECT_RULES.md | Regles que regeixen el projecte |
| docs/architecture.md | Arquitectura i principis de disseny |
| docs/conventions.md | Convencions de noms i estil |
| docs/ai-behavior.md | Com ha de comportar-se la IA |
| docs/context-loading.md | Com carregar el context correctament |
| docs/decision-log.md | Historial de decisions importants |

---

## Com contribuir

1. Fes un fork del repositori
2. Crea una branca per a la teva contribució
3. Segueix les convencions del projecte
4. Fes commits petits i clars
5. Obre un Pull Request

---

## Llicència

Aquest projecte està sota llicència MIT. Consulta el fitxer LICENSE per a més detalls.

---

## Contacte

Per a preguntes, suggeriments o col·laboracions, obre un issue al repositori.
"""

# Escriure el fitxer
with open("README.md", "w", encoding="utf-8") as f:
    f.write(readme_content)

print("✅ README.md actualitzat correctament")
```

Aquest codi:

1. **Segueix les convencions**: Markdown estructurat, enllaços clars, taules per a informació clau
2. **Respecta l'arquitectura**: No duplica informació, referencia altres documents
3. **És pràctic**: Guia d'inici en 5 minuts + exemple real
4. **És bilingüe**: Català amb referències a documentació en anglès
5. **És executable**: Es pot executar directament per generar el fitxer

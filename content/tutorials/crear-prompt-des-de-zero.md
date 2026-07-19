cat > content/tutorials/crear-prompt-des-de-zero.md << 'EOF'
# Tutorial: Crear un Prompt des de Zero

Aquest tutorial et guiarà pas a pas per crear un prompt efectiu per a IA-Productiva, seguint les convencions del projecte.

## Objectiu

Al final d'aquest tutorial, tindràs un prompt funcional que podràs utilitzar per generar contingut de manera consistent.

---

## Pas 1: Defineix l'objectiu del prompt

Abans de començar a escriure, pregunta't:

- **Què volem aconseguir?** (Ex: generar un article, analitzar dades, crear un script...)
- **Quin és el resultat esperat?** (Ex: un text de 500 paraules, un CSV estructurat, un diagrama...)
- **Qui és l'usuari final?** (Ex: un desenvolupador, un màrqueting, un estudiant...)

**Exemple:** Vull generar un article de blog sobre IA pràctica per a principiants.

---

## Pas 2: Carrega el context necessari

Identifica quins documents del projecte han de formar part del context:

- `PROJECT_RULES.md` (regles bàsiques)
- `docs/conventions.md` (format, estil)
- `docs/glossary.md` (terminologia)
- `content/templates/template-document.md` (estructura base)

**Exemple:** Per a l'article, carregaré PROJECT_RULES.md, docs/conventions.md i la template de document.

---

## Pas 3: Escriu la instrucció principal

Redacta la instrucció de manera clara i directa:

- **Què ha de fer la IA?** (Ex: genera un article de 500 paraules)
- **Com ho ha de fer?** (Ex: seguint l'estructura de la template)
- **Què ha d'evitar?** (Ex: no utilitzar llenguatge tècnic innecessari)

**Exemple:** "Genera un article de 500 paraules per a principiants sobre IA pràctica. Utilitza l'estructura de la template-document.md i el to de docs/conventions.md. Evita tecnicismes i inclou exemples senzills."

---

## Pas 4: Afegeix exemples (opcional)

Si el prompt és complex, inclou un exemple de com ha de ser la resposta:

Exemple de sortida:

Article: Com utilitzar IA al teu dia a dia

Introducció

...

text

---

## Pas 5: Defineix el format de sortida

Especifica com ha de ser la resposta (Markdown, JSON, CSV, etc.):
Format de sortida: Markdown
Estructura:

Títol (H1)
Introducció (H2)
3 seccions de contingut (H2)
Conclusió (H2)
Referències (H2)
text

---

## Pas 6: Valida el prompt

Abans d'utilitzar-lo, comprova que:

- [ ] Segueix les convencions de docs/conventions.md
- [ ] Referencia la documentació existent (no la duplica)
- [ ] És concret i accionable
- [ ] Inclou format de sortida esperat

---

## Exemple complet

```markdown
# Prompt: Generació d'article de blog sobre IA pràctica

## Objectiu
Generar un article de 500 paraules sobre IA pràctica per a principiants, en català.

## Context necessari
- PROJECT_RULES.md
- docs/conventions.md
- content/templates/template-document.md

## Instruccions
1. Carrega el context segons l'ordre de context-loading.md
2. Utilitza l'estructura de template-document.md
3. Escriu en to divulgatiu, evitant tecnicismes
4. Inclou exemples pràctics i aplicacions reals
5. La resposta ha de ser en Markdown

## Format de sortida
# Títol de l'article
## Introducció
## Cos de l'article (3 seccions)
## Conclusió
## Referències
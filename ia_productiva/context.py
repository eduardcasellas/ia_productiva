# ia_productiva/context.py

from pathlib import Path

# Llista de fitxers de context que es carregaran (en ordre)
CONTEXT_FILES = [
    "PROJECT_RULES.md",
    "PROJECT.md",
    "TODO.md",
    "SESSION.md",
    "docs/framework-context.md",
    "docs/architecture.md",
    "docs/conventions.md",
    "docs/ai-behavior.md",
    "docs/context-loading.md",
    "docs/decision-log.md"
]

def load_project_context(project_root):
    """
    Carrega tots els fitxers de context i retorna el contingut concatenat.
    project_root: Path object de la carpeta arrel del projecte.
    """
    context_parts = []
    for filepath in CONTEXT_FILES:
        full_path = project_root / filepath
        if full_path.exists():
            with open(full_path, 'r', encoding='utf-8') as f:
                content = f.read()
                context_parts.append(f"--- {filepath} ---\n{content}\n")
        else:
            # Només avisar, no aturar l'execució
            print(f"Avís: {filepath} no trobat. Continuant...")
    return "\n".join(context_parts)

def detect_next_task(project_root):
    """
    Llegeix TODO.md i retorna la primera línia que comenci per "- [ ]" (tasca pendent).
    Si no en troba, retorna un missatge per defecte.
    """
    todo_path = project_root / "TODO.md"
    if todo_path.exists():
        with open(todo_path, 'r', encoding='utf-8') as f:
            for line in f:
                if "- [ ]" in line:
                    return line.strip()
    return "No s'ha trobat cap tasca pendent."
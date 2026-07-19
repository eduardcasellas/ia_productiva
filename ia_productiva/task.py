from pathlib import Path

def process_response(project_root, response):
    """Actualitza SESSION.md amb la resposta de la IA."""
    session_path = project_root / "SESSION.md"
    with open(session_path, 'a', encoding='utf-8') as f:
        f.write(f"\n\n## Resposta de la IA ({Path.cwd().name})\n\n{response}\n")
    print(f"Resposta guardada a {session_path}")

def marcar_tasca_completada(project_root, tasca_text):
    """
    Marca una tasca com a completada a TODO.md.
    project_root: Path object de l'arrel del projecte.
    tasca_text: Text de la tasca a marcar (ex: "Implementar l'estructura de carpetes").
    """
    todo_path = project_root / "TODO.md"
    if not todo_path.exists():
        print(f"⚠️ {todo_path} no trobat.")
        return

    with open(todo_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    tasca_marcada = False
    with open(todo_path, 'w', encoding='utf-8') as f:
        for line in lines:
            if line.strip().startswith("- [ ]") and tasca_text in line:
                line = line.replace("- [ ]", "- [x]")
                tasca_marcada = True
            f.write(line)

    if tasca_marcada:
        print(f"✅ Tasca marcada com a completada a {todo_path}")
    else:
        print(f"⚠️ No s'ha trobat la tasca '{tasca_text}' a {todo_path}")
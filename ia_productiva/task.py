from pathlib import Path

def process_response(project_root, response):
    """Actualitza SESSION.md amb la resposta de la IA."""
    session_path = project_root / "SESSION.md"
    with open(session_path, 'a', encoding='utf-8') as f:
        f.write(f"\n\n## Resposta de la IA ({Path.cwd().name})\n\n{response}\n")
    print(f"Resposta guardada a {session_path}")
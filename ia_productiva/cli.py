import argparse
from pathlib import Path
from .context import load_project_context, detect_next_task
from .prompt import build_prompt
from .ia_adapter import IAAdapter
from .task import process_response

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("command", choices=["run", "init"])
    parser.add_argument("--auto", action="store_true")
    parser.add_argument("--model", default="deepseek")
    args = parser.parse_args()

    if args.command == "run":
        project_root = Path.cwd()
        context = load_project_context(project_root)
        task = detect_next_task(project_root)
        prompt = build_prompt(context, task)
        print(prompt)
        
        if args.auto:
            adapter = IAAdapter(model=args.model)
            response = adapter.query(prompt, context)
            if response:
                print("Resposta:", response)
                process_response(project_root, response)
            else:
                print("No hi ha resposta.")

if __name__ == "__main__":
    main()
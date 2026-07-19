import argparse
import re
import subprocess
import tempfile
from pathlib import Path
from .context import load_project_context, detect_next_task
from .prompt import build_prompt
from .ia_adapter import IAAdapter
from .task import process_response, marcar_tasca_completada

def extreure_i_executar_codi(resposta):
    """
    Extreu codi Python de la resposta i l'executa.
    Retorna True si s'ha executat codi, False si no.
    """
    # Buscar blocs de codi Python
    blocs = re.findall(r'```python\n(.*?)\n```', resposta, re.DOTALL)
    if not blocs:
        return False

    print(f"\n🔧 S'han trobat {len(blocs)} blocs de codi Python. Executant...")
    for i, codi in enumerate(blocs, 1):
        print(f"\n📝 Executant bloc {i}...")
        try:
            # Crear fitxer temporal
            with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False) as f:
                f.write(codi)
                f.flush()
                temp_path = f.name

            # Executar el codi
            resultat = subprocess.run(
                ['python3', temp_path],
                capture_output=True,
                text=True,
                cwd=Path.cwd()
            )

            # Mostrar sortida
            if resultat.stdout:
                print(resultat.stdout)
            if resultat.stderr:
                print("⚠️ Errors:")
                print(resultat.stderr)

            # Netejar fitxer temporal
            Path(temp_path).unlink()

        except Exception as e:
            print(f"❌ Error executant el bloc {i}: {e}")
            return False

    print("✅ Codi executat correctament.")
    return True

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

        # Mostrar el prompt
        print("\n📋 PROMPT GENERAT:")
        print("=" * 60)
        print(prompt)
        print("=" * 60)

        # Determinar si s'ha d'executar
        executar = args.auto
        if not args.auto:
            resposta = input("\n❓ Vols executar aquesta tasca? (s/n): ").strip().lower()
            if resposta in ['s', 'si', 'y', 'yes']:
                executar = True
            else:
                print("⏹️ Execució cancel·lada.")
                return

        # Si s'ha d'executar, enviar a la IA
        if executar:
            adapter = IAAdapter(model=args.model)
            response = adapter.query(prompt, context)
            if response:
                print("\n✅ RESPOSTA DE LA IA:")
                print(response)
                process_response(project_root, response)

                # Executar codi si n'hi ha
                if extreure_i_executar_codi(response):
                    print("✅ Tasca executada automàticament.")
                else:
                    print("ℹ️ No s'ha trobat codi executable. Revisa la resposta manualment.")

                marcar_tasca_completada(project_root, task)
                print("✅ Tasca marcada com a completada a TODO.md")
            else:
                print("❌ No s'ha rebut resposta de la IA.")
        else:
            print("⏹️ Execució cancel·lada.")

if __name__ == "__main__":
    main()
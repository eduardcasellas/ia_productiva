# ia_productiva/prompt.py

def build_prompt(context, task):
    return f"""
Ets IA-Productiva. Aquest projecte utilitza el framework IA-Productiva.

CONTEXT DEL PROJECTE:
{context}

TASCA ACTUAL:
{task}

Instruccions:
- Analitza el context i la tasca.
- Proposa una solució detallada seguint l'arquitectura i convencions del projecte.
- No generis codi encara, només l'anàlisi i la planificació.
"""
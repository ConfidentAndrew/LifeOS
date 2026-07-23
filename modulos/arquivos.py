import json

def carregar_tarefas():
    with open("dados/tarefas.json", "r", encoding="utf-8") as arquivo:
        return json.load(arquivo)
    
def salvar_tarefas(tarefas):
    with open("dados/tarefas.json", "w", encoding="utf-8") as arquivo:
        json.dump(tarefas, arquivo, ensure_ascii=False, indent=4)

def carregar_habitos():
    with open("dados/habitos.json", "r", encoding="utf-8") as arquivo:
        return json.load(arquivo)

def salvar_habitos(habitos):
    with open("dados/habitos.json", "w", encoding="utf-8") as arquivo:
        json.dump(habitos,arquivo, ensure_ascii=False, indent=4)
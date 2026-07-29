import json


def carregar(nome_arquivo): 
    with open(f"dados/{nome_arquivo}.json", "r", encoding="utf-8") as arquivo:
        return json.load(arquivo)

def salvar(nome_arquivo, dados):
    with open(f"dados/{nome_arquivo}.json", "w", encoding="utf-8") as arquivo:
        json.dump(dados, arquivo, ensure_ascii=False, indent=4)

def carregar_tarefas():
    return carregar("tarefas")
    
def salvar_tarefas(tarefas):
    salvar("tarefas", tarefas)

def carregar_habitos():
    return carregar("habitos")

def salvar_habitos(habitos):
    salvar("habitos", habitos)

def carregar_metas():
    return carregar("metas")

def salvar_metas(metas):
    salvar("metas", metas)
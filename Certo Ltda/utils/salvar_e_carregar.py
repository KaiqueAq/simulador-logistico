import json

def salvar_dados(dados_modificados, arquivo_atual):
    # Função que salva os dados modificados em um arquivo Txt identado com JSON
    try:
        with open(arquivo_atual, 'w', encoding="utf-8") as arquivo:
            json.dump(dados_modificados, arquivo, ensure_ascii=False, indent=4)
        print(f"Dados gravados com sucesso em {arquivo_atual}!")
    except Exception as e:
        print(f"Erro ao gravar os dados em {arquivo_atual}: {e}")

def carregar_dados(arquivo_atual):
    # Função que carrega os dados de um arquivo Txt com JSON
    try:
        with open(arquivo_atual, 'r', encoding="utf-8") as arquivo:
            dadosCarregados = json.load(arquivo)
        print(f"Dados carregados com sucesso de {arquivo_atual}!")
        return dadosCarregados
    except Exception as e:
        print(f"Erro ao carregar os dados de {arquivo_atual}: {e}")
        return {}
    
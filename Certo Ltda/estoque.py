import utils.salvar_e_carregar as sec
from datetime import datetime

arquivo_do_estoque = "estoque.txt"

#===================================================================================================
# FUNÇÕES DE VALIDAÇÃO
def ler_inteiro(mensagem):
    while True:
        try:
            valor = int(input(mensagem))
            if valor < 0:
                print("Erro: O valor não pode ser negativo.")
                continue
            return valor
        except ValueError:
            print("Erro: Digite um número inteiro válido (ex: 10, 50).")

def ler_float(mensagem):
    while True:
        try:
            valor = float(input(mensagem))
            if valor < 0:
                print("Erro: O valor não pode ser negativo.")
                continue
            return valor
        except ValueError:
            print("Erro: Digite um valor numérico válido (ex: 25.50).")

def ler_data(mensagem):
    while True:
        data_str = input(mensagem)
        try:
            # Tenta converter o texto para data no formato Dia/Mês/Ano
            datetime.strptime(data_str, "%d/%m/%Y")
            return data_str
        except ValueError:
            print("Erro: Data inválida! Use o formato DD/MM/AAAA (ex: 31/12/2024).")

#===================================================================================================

def menu_estoque(arquivo_estoque_atual_carregado):
    while True:
        print('\n_+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=_')
        print('| MENU ESTOQUE - (ESTOQUE CERTO) |')
        print('*--------------------------------*')
        print('|[1] Entrada de Produto          |')
        print('|[2] Saída de Produto            |')
        print('|[3] Voltar ao Menu Principal    |')
        print('*--------------------------------*')
        opcao = input('Digite a opção desejada: ')
        match opcao:
            case "1":
                menu_entrada_produto(arquivo_estoque_atual_carregado)
            case "2":
                menu_saida_produto()
            case "3":
                return
            case _:
                input('Opção inválida. Enter para continuar.')

def menu_entrada_produto(arquivo_estoque_atual_carregado):
    while True:
        print('\n_+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+_')
        print('|    MENU ENTRADA DE PRODUTO    |')
        print('*-------------------------------*')
        print('|[1] Cadastrar Produto          |')
        print('|[2] Listar Produto             |')
        print('|[3] Editar Produto             |')
        print('|[4] Excluir Produto            |')
        print('|[5] Voltar ao Menu Estoque     |')
        print('*-------------------------------*')
        opcao = input('Digite a opção desejada: ')
        match opcao:
            case "1":
                cadastrar_produto(arquivo_estoque_atual_carregado)
            case "2":
                pass
            case "3":
                pass
            case "4":
                pass
            case "5":
                return
            case _:
                input('Opção inválida.')

def menu_saida_produto():
    pass

def cadastrar_produto(arquivo_dados):
    while True:
        qnts_produtos = ler_inteiro("Quantos produtos deseja cadastrar? ")
        
        if qnts_produtos < 10:
            print("Cadastre no mínimo 10 produtos de uma vez.")
            continue
        
        for i in range(qnts_produtos):
            print(f"\n({i+1}/{qnts_produtos}) Cadastrando Produto:")
            
            produto_id = ler_inteiro("Digite o Código (ID) do produto: ")
            
            # Evitar duplicidade
            if produto_id in arquivo_dados:
                print(f"O produto {produto_id} já existe! Vamos adicionar ao estoque existente.")
                
                nova_quantidade = ler_inteiro("Quantidade a adicionar: ")
                
                arquivo_dados[produto_id]['quantidade'] += nova_quantidade
                print(f"Estoque atualizado! Nova quantidade: {arquivo_dados[produto_id]['quantidade']}")
            
            else:
                produto_nome = input("Nome do produto: ").strip()
                
                # Loop de validação do Porte
                while True:
                    print("Selecione o porte do produto:")
                    print("[1] Pequeno | [2] Médio | [3] Grande")
                    opcao_porte = input("Opção: ")
                    
                    match opcao_porte:
                        case '1':
                            porte = "Pequeno"
                            break
                        case '2':
                            porte = "Médio"
                            break
                        case '3':
                            porte = "Grande"    
                            break
                        case _:
                            print("Erro: Escolha 1, 2 ou 3.")

                data_fabricacao = ler_data("Data de fabricação (DD/MM/AAAA): ")
                fornecedor = input("Fornecedor: ")
                quantidade = ler_inteiro("Quantidade inicial: ")
                local_armazenamento = input("Local de armazenamento: ")
                valor_unitario = ler_float("Valor unitário (R$): ")

                novo_produto = {
                    "codigo": produto_id,
                    "nome": produto_nome,
                    "porte": porte,
                    "data_fabricacao": data_fabricacao,
                    "fornecedor": fornecedor,
                    "quantidade": quantidade,
                    "local_armazenamento": local_armazenamento,
                    "valor_unitario": valor_unitario
                }
                
                arquivo_dados[produto_id] = novo_produto
        
        sec.salvar_dados(arquivo_dados, arquivo_do_estoque)
        print("\nTodos os produtos foram salvos com sucesso!")
        break
        
    return arquivo_dados
# estoque.py
import utils.salvar_e_carregar as sec
from datetime import datetime

arquivo_estoque = "estoque.txt"

# --- FUNÇÕES DE VALIDAÇÃO ---
def ler_inteiro(mensagem):
    while True:
        try:
            valor = int(input(mensagem))
            if valor < 0:
                print("Erro: O valor não pode ser negativo.")
                continue
            return valor
        except ValueError:
            print("Erro: Digite um número inteiro válido.")

def ler_float(mensagem):
    while True:
        try:
            valor = float(input(mensagem))
            if valor < 0:
                print("Erro: O valor não pode ser negativo.")
                continue
            return valor
        except ValueError:
            print("Erro: Digite um valor numérico válido (use ponto para centavos).")

def ler_data(mensagem):
    while True:
        data_str = input(mensagem)
        try:
            datetime.strptime(data_str, "%d/%m/%Y")
            return data_str
        except ValueError:
            print("Erro: Data inválida! Use o formato DD/MM/AAAA.")

# --- MENUS ---

def menu_estoque(lista_produtos):
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
                menu_entrada_produto(lista_produtos)
            case "2":
                menu_saida_produto()
            case "3":
                return
            case _:
                input('Opção inválida. Enter para continuar.')

def menu_entrada_produto(lista_produtos):
    while True:
        print('\n_+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+_')
        print('|    MENU ENTRADA DE PRODUTO    |')
        print('*-------------------------------*')
        print('|[1] Cadastrar Produto          |')
        print('|[2] Listar Produtos            |')
        print('|[3] Editar Produto             |')
        print('|[4] Excluir Produto            |')
        print('|[5] Voltar ao Menu Estoque     |')
        print('*-------------------------------*')
        opcao = input('Digite a opção desejada: ')
        match opcao:
            case "1":
                cadastrar_produto(lista_produtos)
            case "2":
                listar_produtos(lista_produtos)
            case _:
                input('Opção inválida.')

def menu_saida_produto():
    pass

def listar_produtos(lista_produtos):
    print("\n--- LISTA DE ESTOQUE ---")
    if not lista_produtos:
        print("Nenhum produto cadastrado.")
    else:
        for p in lista_produtos:
            print(f"ID: {p['codigo']} | Nome: {p['nome']} | Qtd: {p['quantidade']} | Preço: R${p['valor_unitario']:.2f}")
    input("\nPressione Enter para continuar...")

def cadastrar_produto(lista_produtos):
    while True:
        qnts_produtos = ler_inteiro("Quantos produtos deseja cadastrar? ")
        
        # if qnts_produtos < 10:
        #     print("Requisito: Cadastre no mínimo 10 produtos de uma vez.")
        #     continue
        
        for i in range(qnts_produtos):
            print(f"\n({i+1}/{qnts_produtos}) Cadastrando Produto:")
            
            produto_id = ler_inteiro("Digite o Código (ID) do produto: ")
            
            produto_encontrado = None
            for item in lista_produtos:
                if item['codigo'] == produto_id:
                    produto_encontrado = item
                    break
            
            if produto_encontrado:
                print(f"O produto '{produto_encontrado['nome']}' (ID {produto_id}) já existe!")
                nova_quantidade = ler_inteiro("Quantidade a adicionar ao estoque existente: ")
                
                produto_encontrado['quantidade'] += nova_quantidade
                print(f"Estoque atualizado! Total: {produto_encontrado['quantidade']}")
            
            else:
                # Se não existe, pede os dados
                produto_nome = input("Nome do produto: ")  
                
                while True:
                    print("Selecione o porte: [1] Pequeno | [2] Médio | [3] Grande")
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
                            print("Opção inválida. Tente novamente.")

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
                
                # --- CORREÇÃO 2: Adicionar na lista com APPEND ---
                lista_produtos.append(novo_produto)
        
        # Salvar a lista atualizada
        sec.salvar_dados(lista_produtos, arquivo_estoque)
        print("\nProdutos cadastrados com sucesso!")
        break
        
    return lista_produtos
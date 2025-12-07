# estoque.py
import utils.salvar_e_carregar as sec
from datetime import datetime

arquivo_estoque = "estoque.txt"

# Funções de validação de entradas ============================================================================
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

# PARTE DE MENUS E AFINS ======================================================================================
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
            case "3":
                editar_produto(lista_produtos)
            case "4":
                excluir_produto(lista_produtos)
            case _:
                input('Opção inválida.')

def menu_saida_produto():
    pass

# Parte do Menu de Entrada ====================================================================================
def cadastrar_produto(lista_produtos):
    while True:
        qnts_produtos = ler_inteiro("Quantos produtos deseja cadastrar? ")
        
        if qnts_produtos < 10:
            print("Requisito: Cadastre no mínimo 10 produtos de uma vez.")
            continue
        
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
                
                # CORREÇÃO 2: Adcionar o novo produto à lista
                lista_produtos.append(novo_produto)
        
        # Salvar a lista atualizada
        sec.salvar_dados(lista_produtos, arquivo_estoque)
        print("\nProdutos cadastrados com sucesso!")
        break
        
    return lista_produtos

def listar_produtos(lista_produtos):
    print("_+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+_")
    print("|       LISTA DE ESTOQUE        |")
    print("*-------------------------------*")

    if not lista_produtos:
        print("\n>>> O estoque está vazio no momento.")
        input("Pressione Enter para voltar...")
        return

    for produto in lista_produtos:
        print(f"Código:     {produto['codigo']}")
        print(f"Nome:       {produto['nome']}")
        print(f"Porte:      {produto['porte']}")
        print(f"Fabricação: {produto['data_fabricacao']}")
        print(f"Qtd:        {produto['quantidade']}")
        print(f"Preço:     R$ {produto['valor_unitario']:.2f}") 
        print(f"Local:      {produto['local_armazenamento']}")
        print("-" * 31)
    
    print(f"Total de produtos cadastrados: {len(lista_produtos)}")
    input("\nPressione Enter para voltar ao menu...")   

def editar_produto(lista_produtos):
    print("_+=+=+=+=+=+=+=+=+=+=+=+=_")
    print("|     EDITAR PRODUTO     |")
    print("*------------------------*")
    id_busca = ler_inteiro("Digite o Código (ID) do produto que deseja editar: ")

    # Busca o produto na lista
    produto_encontrado = None
    for produto in lista_produtos:
        if produto['codigo'] == id_busca:
            produto_encontrado = produto
            break
    
    if not produto_encontrado:
        print("Produto não encontrado!")
        input("Pressione Enter para voltar...")
        return lista_produtos

    # Loop para editar vários campos do mesmo produto
    while True:
        print(f"\nEditando: {produto_encontrado['nome']} (ID: {produto_encontrado['codigo']})")
        print("[1] Nome")
        print("[2] Porte")
        print("[3] Data de Fabricação")
        print("[4] Fornecedor")
        print("[5] Quantidade (Correção Manual)")
        print("[6] Local de Armazenamento")
        print("[7] Valor Unitário")
        print("[0] Salvar e Sair da Edição")
        
        opcao = input("Qual campo deseja alterar? ")

        match opcao:
            case "1":
                produto_encontrado['nome'] = input("Novo Nome: ")
            case "2":
                while True:
                    print("Novo porte: [1] Pequeno | [2] Médio | [3] Grande")
                    op = input("Opção: ")
                    match op:
                        case '1':
                            produto_encontrado['porte'] = "Pequeno"
                            break
                        case '2':
                            produto_encontrado['porte'] = "Médio"
                            break
                        case '3':
                            produto_encontrado['porte'] = "Grande"
                            break
                        case _:
                            print("Inválido.")
                    if op in ['1', '2', '3']: break
            case "3":
                produto_encontrado['data_fabricacao'] = ler_data("Nova Data (DD/MM/AAAA): ")
            case "4":
                produto_encontrado['fornecedor'] = input("Novo Fornecedor: ")
            case "5":
                produto_encontrado['quantidade'] = ler_inteiro("Nova Quantidade: ")
            case "6":
                produto_encontrado['local_armazenamento'] = input("Novo Local: ")
            case "7":
                produto_encontrado['valor_unitario'] = ler_float("Novo Valor (R$): ")
            case "0":
                break
            case _:
                print("Opção inválida.")
        
        print("Alteração registrada (será salva ao sair).")
    
    # Salva as alterações no arquivo ao sair do loop de edição
    sec.salvar_dados(lista_produtos, arquivo_estoque)
    print("Alterações salvas no arquivo com sucesso!")
    return lista_produtos

def excluir_produto(lista_produtos):
    print("_+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+_")
    print("|        EXCLUIR PRODUTO        |")
    print("*-------------------------------*")
    
    id_busca = ler_inteiro("Digite o Código (ID) do produto que deseja excluir: ")

    # Busca o produto na lista
    produto_encontrado = None
    for produto in lista_produtos:
        if produto['codigo'] == id_busca:
            produto_encontrado = produto
            break
    
    if not produto_encontrado:
        print("Produto não encontrado!")
        input("Pressione Enter para voltar...")
        return lista_produtos

    # Mostra os dados para confirmar a exclusão
    print(f"\nATENÇÃO: Você está prestes a excluir:")
    print(f"Nome: {produto_encontrado['nome']}")
    print(f"Qtd em Estoque: {produto_encontrado['quantidade']}")
    
    confirmacao = input("Digite 'S' para CONFIRMAR a exclusão ou qualquer tecla para CANCELAR: ").upper().strip()
    
    if confirmacao == 'S':
        # Remove da lista
        lista_produtos.remove(produto_encontrado)
        
        # Salva a lista atualizada no arquivo
        sec.salvar_dados(lista_produtos, arquivo_estoque)
        print("\nProduto excluído com sucesso!")
    else:
        print("\nOperação cancelada. O produto não foi apagado.")
    
    input("Pressione Enter para continuar...")
    return lista_produtos
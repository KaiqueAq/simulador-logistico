

def menu_estoque():
    while True:
        # limpaTela()
        print('_+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=_')
        print('| MENU ESTOQUE - (ESTOQUE CERTO) |')
        print('*--------------------------------*')
        print('|[1] Entrada de Produto          |')
        print('|[2] Saída de Produto            |')
        print('|[3] Voltar ao Menu Principal    |')
        print('*--------------------------------*')
        opcao = input('Digite a opção desejada: ')
        match opcao:
            case "1":
                menu_entrada_produto()
            case "2":
                menu_saida_produto()
            case "3":
                return
            case _:
                input('Opção inválida. Pressione qualquer tecla para continuar.')
                continue

def menu_entrada_produto():
    while True:
        # limpaTela()
        print('_+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+_')
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
                pass
            case "2":
                pass
            case "3":
                pass
            case "4":
                pass
            case "5":
                return
            case _:
                input('Opção inválida. Pressione qualquer tecla para continuar.')
                continue

def menu_saida_produto():
    pass
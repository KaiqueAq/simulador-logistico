import estoque as est
import utils.salvar_e_carregar as sec

arquivo_estoque_nome = "estoque.txt"

# Função do menu principal
def menu_principal():  
    arquivo_estoque_carregado = sec.carregar_dados(arquivo_estoque_nome)
    while True:
        # limpaTela()
        print('_+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=_')
        print('| MENU LOGÍSTICA - (ESTOQUE CERTO) |')
        print('*----------------------------------*')
        print('|[1] Operacional                   |')
        print('|[2] Estoque                       |')
        print('|[3] Financeiro                    |')
        print('|[4] Gestão de Pessoas             |')
        print('|[0] Sair                          |')
        print('*----------------------------------*')
        opcao = input('Digite a opção desejada: ')  
        match opcao:
            case "1":
                pass
            case "2":
                est.menu_estoque(arquivo_estoque_carregado)
            case "3":
                pass
            case "4":
                pass
            case "0":
                print('Encerrando o programa...')
                # time.sleep(1.5)
                break
            case _:
                input('Opção inválida. Pressione qualquer tecla para continuar.')
                continue

# Função que inicia o programa
menu_principal()

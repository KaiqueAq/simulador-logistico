import operacional as op
import estoque as est
import financeiro as fin
import gestao_de_pessoas as gp
import utils.salvar_e_carregar as sec
import time

arquivo_estoque_nome = "estoque.txt"
arquivo_relatorio_nome = "relatorio_pedidos.txt"
arquivo_funcionarios_nome = "funcionarios.txt"

# Função do menu principal
def menu_principal():  
    arquivo_estoque_carregado = sec.carregar_dados(arquivo_estoque_nome)
    arquivo_funcionarios_carregado = sec.carregar_dados(arquivo_funcionarios_nome)
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
                op.menu_operacional()
            case "2":
                est.menu_estoque(arquivo_estoque_carregado)
            case "3":
                fin.menu_financeiro(arquivo_estoque_carregado, arquivo_relatorio_nome, arquivo_estoque_nome)
            case "4":
                gp.menu_gestao_pessoas(arquivo_funcionarios_carregado)
                pass
            case "0":
                print('Encerrando o programa...')
                time.sleep(1.5)
                break
            case _:
                input('Opção inválida. Pressione qualquer tecla para continuar.')
                continue

# Função que inicia o programa
menu_principal()

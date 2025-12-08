import re # Módulo para expressões regulares, útil para extrair dados do relatório
from utils.limpatela import limpaTela
def ler_float(mensagem):
    """Lê um valor float positivo do usuário."""
    while True:
        try:
            valor = float(input(mensagem))
            if valor < 0:
                print("Erro: O valor não pode ser negativo.")
                continue
            return valor
        except ValueError:
            print("Erro: Digite um valor numérico válido (use ponto para decimais).")

def menu_financeiro(lista_produtos, arquivo_relatorio, arquivo_estoque):
    """
    Exibe o menu financeiro e direciona para as funções correspondentes.
    """
    while True:
        limpaTela()
        print('\n_+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+_')
        print('|      MENU FINANCEIRO - VISÃO       |')
        print('*------------------------------------*')
        print('|[1] Valor Total do Estoque          |')
        print('|[2] Receita Bruta (Pedidos)         |')
        print('|[3] Custo e Preço por Pallet (Proj.)|')
        print('|[4] Voltar ao Menu Principal        |')
        print('*------------------------------------*')
        opcao = input('Digite a opção desejada: ')
        
        match opcao:
            case "1":
                limpaTela()
                ver_valor_total_estoque(lista_produtos)
            case "2":
                limpaTela()
                ver_receita_bruta(lista_produtos, arquivo_relatorio)
            case "3":
                limpaTela()
                calcular_custo_pallet()
            case "4":
                return
            case _:
                input('Opção inválida. Pressione Enter para continuar.')

def ver_valor_total_estoque(lista_produtos):
    """
    Calcula e exibe o valor total de todos os produtos em estoque.
    """
    print("\n_+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+_")
    print("|     VALOR TOTAL DO ESTOQUE     |")
    print("*--------------------------------*")

    valor_total = 0.0
    if not lista_produtos:
        print("Estoque vazio. Valor total: R$ 0.00")
    else:
        for produto in lista_produtos:
            valor_total += produto.get('quantidade', 0) * produto.get('valor_unitario', 0)
        
        print(f"O valor total do estoque é: R$ {valor_total:,.2f}")

    input("\nPressione Enter para voltar...")

def ver_receita_bruta(lista_produtos, arquivo_relatorio):
    """
    Lê o relatório de pedidos, calcula e exibe a receita bruta total.
    """
    print("\n_+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+_")
    print("|      RECEITA BRUTA (PEDIDOS)     |")
    print("*----------------------------------*")

    receita_total = 0.0
    pedidos_processados = 0
    mapa_valores = {produto['codigo']: produto['valor_unitario'] for produto in lista_produtos}

    try:
        with open(arquivo_relatorio, 'r', encoding='utf-8') as f:
            for linha in f:
                match_id = re.search(r'ID: (\d+)', linha)
                match_qtd = re.search(r'Qtd: (\d+)', linha)

                if match_id and match_qtd:
                    produto_id = int(match_id.group(1))
                    quantidade = int(match_qtd.group(1))
                    
                    valor_unitario = mapa_valores.get(produto_id, 0)
                    receita_total += quantidade * valor_unitario
                    pedidos_processados += 1
    except FileNotFoundError:
        print("Arquivo de relatório de pedidos ainda não existe.")
    
    print(f"Receita bruta total com base em {pedidos_processados} pedidos: R$ {receita_total:,.2f}")
    input("\nPressione Enter para voltar...")

def calcular_custo_pallet():
    """
    Calcula o custo por pallet e projeta lucros, salvando em arquivo.
    """
    print("\n_+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+_")
    print("| CUSTO E PRECIFICAÇÃO POR PALLET    |")
    print("*------------------------------------*")
    print("Insira os custos operacionais mensais:")

    # 1. Solicitar os valores mensais
    valor_agua = ler_float(" -> Valor da conta de água (R$): ")
    valor_luz = ler_float(" -> Valor da conta de luz (R$): ")
    valor_salarios = ler_float(" -> Valor total dos salários (R$): ")
    valor_impostos = ler_float(" -> Valor dos impostos (R$): ")

    # 2. Calcular custo total mensal
    custo_total_mensal = valor_agua + valor_luz + valor_salarios + valor_impostos

    # 3. Considerar 1000 pallets por mês
    quantidade_pallets = 1000

    # 4. Calcular custo unitário por pallet
    custo_unitario = custo_total_mensal / quantidade_pallets

    # 5. Calcular preço final com 50% de lucro
    preco_final_unitario = custo_unitario * 1.5

    # 6 & 7. Projeções de lucro
    lucro_mensal = (preco_final_unitario - custo_unitario) * quantidade_pallets
    lucro_anual = lucro_mensal * 12

    # 8. Mostrar resultados na tela
    print("\n*----------- RESULTADOS -----------*")
    print(f"Custo operacional mensal total: R$ {custo_total_mensal:,.2f}")
    print(f"Custo unitário por pallet:      R$ {custo_unitario:,.2f}")
    print(f"Preço final sugerido (50% lucro): R$ {preco_final_unitario:,.2f}")
    print("------------------------------------")
    print(f"Projeção de Lucro Bruto Mensal: R$ {lucro_mensal:,.2f}")
    print(f"Projeção de Lucro Bruto Anual:  R$ {lucro_anual:,.2f}")
    print("*------------------------------------*")

    # 9. Gerar arquivo persistente (relatorio_financeiro.txt)
    nome_arquivo_fin = "relatorio_financeiro.txt"
    try:
        with open(nome_arquivo_fin, "w", encoding="utf-8") as arq:
            arq.write("===== RELATÓRIO FINANCEIRO (PROJEÇÃO DE CUSTOS) =====\n\n")
            arq.write("Custos Operacionais Mensais Inseridos:\n")
            arq.write(f" - Água:      R$ {valor_agua:,.2f}\n")
            arq.write(f" - Luz:       R$ {valor_luz:,.2f}\n")
            arq.write(f" - Salários:  R$ {valor_salarios:,.2f}\n")
            arq.write(f" - Impostos:  R$ {valor_impostos:,.2f}\n")
            arq.write("-" * 50 + "\n")
            arq.write(f"CUSTO TOTAL MENSAL:        R$ {custo_total_mensal:,.2f}\n")
            arq.write(f"Base de cálculo:           {quantidade_pallets} pallets/mês\n")
            arq.write("-" * 50 + "\n")
            arq.write("RESULTADOS UNITÁRIOS E PRECIFICAÇÃO:\n")
            arq.write(f"Custo Unitário (Pallet):   R$ {custo_unitario:,.2f}\n")
            arq.write(f"Preço de Venda (50% margem): R$ {preco_final_unitario:,.2f}\n")
            arq.write("-" * 50 + "\n")
            arq.write("PROJEÇÃO DE LUCROS:\n")
            arq.write(f"Lucro Mensal Estimado:     R$ {lucro_mensal:,.2f}\n")
            arq.write(f"Lucro Anual Estimado:      R$ {lucro_anual:,.2f}\n")
        
        print(f"\n>> Relatório salvo com sucesso em '{nome_arquivo_fin}'")
        
    except Exception as e:
        print(f"\nErro ao salvar o arquivo: {e}")

    input("\nPressione Enter para voltar...")
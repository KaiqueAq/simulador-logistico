import utils.salvar_e_carregar as sec
from datetime import datetime

arquivo_estoque = "estoque.txt"
arquivo_relatorio = "relatorio_pedidos.txt" # Nome do arquivo de relatório

# Controle de pedidos diários e Relatórios
pedidos_realizados_hoje = 0
limite_pedidos_dia = 10
data_sessao_atual = datetime.now().strftime("%d/%m/%Y") # Guarda a data de quando o programa abriu
historico_pedidos = [] # Lista para armazenar os pedidos feitos na sessão

# Funções Auxiliares pra validar entrada de dados em vez do try/except direto
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

# Menu de Saída de Produtos (Pedidos/Vendas)
def menu_saida(lista_produtos):
    while True:
        print('_+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+_')
        print('|    MENU SAÍDA (PEDIDOS/VENDAS)     ')
        # Mostra o contador visualmente para o usuário saber quanto falta
        print(f'| Pedidos Hoje: {pedidos_realizados_hoje}/{limite_pedidos_dia}              ')
        print('*-----------------------------------*')
        print('|[1] Fazer Pedido (Baixa no Estoque)|')
        print('|[2] Gerar Relatório de Pedidos     |')
        print('|[3] Voltar ao Menu Estoque         |')
        print('*-----------------------------------*')
        opcao = input('Digite a opção desejada: ')
        
        match opcao:
            case "1":
                processar_pedido(lista_produtos)
            case "2":
                gerar_relatorio_pedidos()
            case "3":
                return
            case _:
                input('Opção inválida. Enter para continuar.')

# Lógica de Processamento de Pedidos
def processar_pedido(lista_produtos):
    global pedidos_realizados_hoje, data_sessao_atual, historico_pedidos
    
    # 0. Verificação de Mudança de Dia (Reset Automático)
    hoje_atual = datetime.now().strftime("%d/%m/%Y")
    if hoje_atual != data_sessao_atual:
        print(f"\nMudança de dia detectada! ({data_sessao_atual} -> {hoje_atual})")
        print("Resetando o limite diário de pedidos...")
        pedidos_realizados_hoje = 0
        historico_pedidos = [] # Limpa o histórico do dia anterior no programa
        data_sessao_atual = hoje_atual
    
    # Aqui é pra Verificar o limite diário de 10 pedidos
    if pedidos_realizados_hoje >= limite_pedidos_dia:
        print("\nLIMITE ATINGIDO: Não é possível fazer mais de 10 pedidos por dia.")
        input("Pressione Enter para voltar...")
        return

    print("_+=+=+=+=+=+=+=+_")
    print("|  NOVO PEDIDO  |")
    print("*---------------*")
    
    # 2. Identifica o produto
    id_busca = ler_inteiro("Digite o ID do Produto: ")
    
    produto_encontrado = None
    for produto in lista_produtos:
        if produto['codigo'] == id_busca:
            produto_encontrado = produto
            break
            
    if not produto_encontrado:
        print("Produto não encontrado no estoque.")
        input("Enter para continuar...")
        return

    # Mostra disponibilidade atual
    qtd_estoque = produto_encontrado['quantidade']
    print(f"Produto: {produto_encontrado['nome']} | Disponível: {qtd_estoque}")
    
    if qtd_estoque == 0:
        print("Produto ESGOTADO!")
        input("Enter para continuar...")
        return

    # 3. Coleta dados do pedido
    nome_cliente = input("Nome do Cliente: ")
    qtd_desejada = ler_inteiro(f"Quantidade desejada (Máx {qtd_estoque}): ")
    
    if qtd_desejada <= 0:
        print("Quantidade inválida.")
        return

    qtd_final = 0
    tipo_baixa = ""

    # 4. Verifica Disponibilidade (Decisão do Fluxograma)
    if qtd_desejada <= qtd_estoque:
        # Tem estoque suficiente
        qtd_final = qtd_desejada
        tipo_baixa = "Total"
    else:
        # Não tem tudo -> Oferece Parcial
        print(f"\nEstoque insuficiente! Você pediu {qtd_desejada}, mas só temos {qtd_estoque}.")
        aceita_parcial = input(f"Deseja levar os {qtd_estoque} disponíveis (Pedido Parcial)? (S/N): ").upper()
        
        if aceita_parcial == 'S':
            qtd_final = qtd_estoque
            tipo_baixa = "Parcial"
        else:
            print("Pedido cancelado pelo cliente.")
            input("Enter para continuar...")
            return

    # 5. Atualiza o Estoque (Baixa)
    produto_encontrado['quantidade'] -= qtd_final
    
    # 6. Salva no Arquivo TXT do estoque imediatamente
    sec.salvar_dados(lista_produtos, arquivo_estoque)
    
    # 7. Registra para o Relatório e Contadores
    pedidos_realizados_hoje += 1
    
    agora = datetime.now()
    data_formatada = agora.strftime("%d/%m/%Y")
    hora_formatada = agora.strftime("%H:%M")
    
    registro = {
        "data": data_formatada,
        "hora": hora_formatada,
        "cliente": nome_cliente,
        "produto_id": produto_encontrado['codigo'],
        "produto_nome": produto_encontrado['nome'],
        "qtd": qtd_final,
        "tipo": tipo_baixa
    }
    historico_pedidos.append(registro)
    
    # 8. Salva no Arquivo TXT de Relatório
    try:
        with open(arquivo_relatorio, "a", encoding="utf-8") as arquivo_rel:
            linha = f"[{data_formatada} - {hora_formatada}] Cliente: {nome_cliente} | Prod: {produto_encontrado['nome']} (ID: {produto_encontrado['codigo']}) | Qtd: {qtd_final} | Tipo: {tipo_baixa}\n"
            arquivo_rel.write(linha)
    except Exception as e:
        print(f"Erro ao salvar no arquivo de relatório: {e}")
    
    print(f"\nPedido realizado com sucesso! ({tipo_baixa})")
    print(f"Saída de {qtd_final} unidades de '{produto_encontrado['nome']}'.")
    print(f"Estoque restante: {produto_encontrado['quantidade']}")
    input("Pressione Enter para continuar...")

def gerar_relatorio_pedidos():
    print("\n_+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=_")
    print("|      RELATÓRIO DE PEDIDOS      |")
    print("*--------------------------------*")
    
    if not historico_pedidos:
        print("\nNenhum pedido realizado nesta sessão.")
    else:
        print(f"Total de pedidos hoje (nesta sessão): {len(historico_pedidos)}")
        print("-" * 50)
        for i, p in enumerate(historico_pedidos):
            print(f"#{i+1} [{p['data']} - {p['hora']}] - {p['cliente']}")
            print(f"   Produto: {p['produto_nome']} (ID: {p['produto_id']})")
            print(f"   Qtd: {p['qtd']} | Tipo: {p['tipo']}")
            print("-" * 50)
    
    print(f"\nO histórico completo está salvo em: {arquivo_relatorio}")
    input("\nPressione Enter para voltar...")

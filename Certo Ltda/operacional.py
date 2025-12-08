
# ----------- Função 1: Cálculo da capacidade com base nos turnos -----------

def calcular_capacidade(turno_manha, turno_tarde, turno_noite, turnos_ativos, dias_mes):
    # 'dias_mes' é recebido do menu, permitindo flexibilidade (30, 31, 28, etc.).
    meses_ano = 12 

    # Capacidade máxima total.
    capacidade_diaria_total = turno_manha + turno_tarde + turno_noite

    # Soma a capacidade dos turnos ativos.
    capacidade_atual = 0
    if "manhã" in turnos_ativos:
        capacidade_atual += turno_manha
    if "tarde" in turnos_ativos:
        capacidade_atual += turno_tarde
    if "noite" in turnos_ativos:
        capacidade_atual += turno_noite

    # Cálculo da capacidade mensal (agora flexível).
    capacidade_mensal = capacidade_atual * dias_mes 
    capacidade_anual = capacidade_mensal * meses_ano

    # Capacidade ociosa.
    diferenca_cap = capacidade_diaria_total - capacidade_atual
    
    # Previne ZeroDivisionError.
    if capacidade_diaria_total > 0:
        percentual_utilizacao = (capacidade_atual / capacidade_diaria_total) * 100
    else:
        percentual_utilizacao = 0.0

    return {
        "turnos_ativos": turnos_ativos,
        "dias_mes": dias_mes, # Incluído no retorno para o relatório
        "capacidade_diaria": capacidade_atual,
        "capacidade_diaria_total": capacidade_diaria_total,
        "capacidade_mensal": capacidade_mensal,
        "capacidade_anual": capacidade_anual,
        "diferenca_cap": diferenca_cap,
        "percentual_utilizacao": percentual_utilizacao
    }

# ----------- Função 2: Gerar relatório em TXT -----------

def salvar_relatorio_txt(dados, nome_arquivo="relatorio_operacional.txt"):
    # Abre o arquivo para escrita, garantindo o fechamento (with open).
    with open(nome_arquivo, "w", encoding="utf-8") as arq:
        arq.write("===== RELATÓRIO OPERACIONAL =====\n\n")
        
        # Escreve os dados formatados.
        arq.write(f"Turnos ativos: {dados['turnos_ativos']}\n")
        arq.write(f"Base de dias para o mês: {dados['dias_mes']}\n") # Exibe o valor de dias
        arq.write(f"Capacidade diária atual: {dados['capacidade_diaria']:,}\n")
        arq.write(f"Capacidade diária total (100%): {dados['capacidade_diaria_total']:,}\n")
        arq.write("-" * 40 + "\n")
        arq.write(f"Capacidade mensal: {dados['capacidade_mensal']:,}\n")
        arq.write(f"Capacidade anual: {dados['capacidade_anual']:,}\n")
        arq.write("-" * 40 + "\n")
        arq.write(f"Capacidade NÃO utilizada: {dados['diferenca_cap']:,}\n")
        arq.write(f"Percentual de utilização: {dados['percentual_utilizacao']:.2f}%\n")

    print(f"\nRelatório salvo em: {nome_arquivo}")


# ----------- Função 3: Simulação para 1, 2 e 3 turnos -----------
# AGORA RECEBE 'dias_mes' para passar adiante.

def simular_turnos(turno_manha, turno_tarde, turno_noite, dias_mes):
    # Dicionário com as combinações.
    simulacoes = {
        "1 turno": [["manhã"], ["tarde"], ["noite"]],
        "2 turnos": [["manhã", "tarde"], ["manhã", "noite"], ["tarde", "noite"]],
        "3 turnos": [["manhã", "tarde", "noite"]]
    }

    resultados = {}

    # Itera e calcula a capacidade para cada cenário.
    for tipo, lista_turnos in simulacoes.items():
        resultados[tipo] = []
        for turnos_ativos in lista_turnos:
            # Chama a função principal de cálculo com o número de dias.
            resultado = calcular_capacidade(
                turno_manha, turno_tarde, turno_noite, turnos_ativos, dias_mes 
            )
            resultados[tipo].append(resultado)

    return resultados


# ----------- Função 4: Menu operacional (Principal) -----------

def menu_operacional():

    print("\n=== CONFIGURAÇÃO DE ENTRADA ===")
    
    # 1. ENTRADA DO NÚMERO DE DIAS (NOVO PASSO)
    try:
        # Pede ao usuário para definir quantos dias usar no cálculo mensal
        dias_mes = int(input("Número de dias a considerar no mês (ex: 30, 31, 28): "))
        if dias_mes <= 0:
             raise ValueError
    except ValueError:
        print("Erro: O número de dias deve ser um inteiro positivo. O programa será encerrado.")
        return


    # 2. ENTRADA DA CAPACIDADE POR TURNO
    print("\n=== CONFIGURAÇÃO DA CAPACIDADE POR TURNO ===")

    try:
        turno_manha = int(input("Capacidade do turno MANHÃ: "))
        turno_tarde = int(input("Capacidade do turno TARDE: "))
        turno_noite = int(input("Capacidade do turno NOITE: "))
    except ValueError:
        print("Erro: A capacidade deve ser um número inteiro. O programa será encerrado.")
        return

    # 3. SELEÇÃO DE TURNOS ATIVOS
    print("\n=== SELEÇÃO DE TURNOS ATIVOS ===")
    turnos_ativos = []

    # Seleção de turnos, usando .strip().upper() para robustez.
    if input("Ativar manhã? (S/N): ").strip().upper() == "S":
        turnos_ativos.append("manhã")
    if input("Ativar tarde? (S/N): ").strip().upper() == "S":
        turnos_ativos.append("tarde")
    if input("Ativar noite? (S/N): ").strip().upper() == "S":
        turnos_ativos.append("noite")

    # 4. REALIZA O CÁLCULO (passando 'dias_mes')
    dados = calcular_capacidade(turno_manha, turno_tarde, turno_noite, turnos_ativos, dias_mes)

    print(f"\n===== RESULTADO (Base {dias_mes} dias) =====")
    print(f"Turnos ativos: {dados['turnos_ativos']}")
    print(f"Capacidade diária atual: {dados['capacidade_diaria']:,}")
    print(f"Capacidade diária total: {dados['capacidade_diaria_total']:,}")
    print(f"Capacidade mensal: {dados['capacidade_mensal']:,}")
    print(f"Capacidade anual: {dados['capacidade_anual']:,}")
    print(f"Diferença (ociosa): {dados['diferenca_cap']:,}")
    print(f"Utilização: {dados['percentual_utilizacao']:.2f}%")
    
    # 5. SALVA O RELATÓRIO
    salvar_relatorio_txt(dados)

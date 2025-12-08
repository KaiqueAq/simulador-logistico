
# ----------- Função 1: Cálculo da capacidade com base nos turnos -----------

def calcular_capacidade(turno_manha, turno_tarde, turno_noite, turnos_ativos):
    dias_mes = 30
    meses_ano = 12

    capacidade_diaria_total = turno_manha + turno_tarde + turno_noite

    capacidade_atual = 0
    if "manhã" in turnos_ativos:
        capacidade_atual += turno_manha
    if "tarde" in turnos_ativos:
        capacidade_atual += turno_tarde
    if "noite" in turnos_ativos:
        capacidade_atual += turno_noite

    capacidade_mensal = capacidade_atual * dias_mes
    capacidade_anual = capacidade_mensal * meses_ano

    diferenca_cap = capacidade_diaria_total - capacidade_atual
    percentual_utilizacao = (capacidade_atual / capacidade_diaria_total) * 100

    return {
        "turnos_ativos": turnos_ativos,
        "capacidade_diaria": capacidade_atual,
        "capacidade_diaria_total": capacidade_diaria_total,
        "capacidade_mensal": capacidade_mensal,
        "capacidade_anual": capacidade_anual,
        "diferenca_cap": diferenca_cap,
        "percentual_utilizacao": percentual_utilizacao
    }
# ----------- Função 2: Gerar relatório em TXT -----------

def salvar_relatorio_txt(dados, nome_arquivo="relatorio_operacional.txt"):
    with open(nome_arquivo, "w", encoding="utf-8") as arq:
        arq.write("===== RELATÓRIO OPERACIONAL =====\n\n")
        arq.write(f"Turnos ativos: {dados['turnos_ativos']}\n")
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

def simular_turnos(turno_manha, turno_tarde, turno_noite):
    simulacoes = {
        "1 turno": [["manhã"], ["tarde"], ["noite"]],
        "2 turnos": [["manhã", "tarde"], ["manhã", "noite"], ["tarde", "noite"]],
        "3 turnos": [["manhã", "tarde", "noite"]]
    }

    resultados = {}

    for tipo, lista_turnos in simulacoes.items():
        resultados[tipo] = []
        for turnos_ativos in lista_turnos:
            resultado = calcular_capacidade(
                turno_manha, turno_tarde, turno_noite, turnos_ativos
            )
            resultados[tipo].append(resultado)

    return resultados


# ----------- Função 4: Menu operacional -----------

def menu_operacional():

# Definição dos turnos e capacidades (entrada do usuário)

    print("\n=== CONFIGURAÇÃO DA CAPACIDADE POR TURNO ===")

    turno_manha = int(input("Capacidade do turno MANHÃ: "))
    turno_tarde = int(input("Capacidade do turno TARDE: "))
    turno_noite = int(input("Capacidade do turno NOITE: "))

    print("\n=== SELEÇÃO DE TURNOS ATIVOS ===")
    turnos_ativos = []

    if input("Ativar manhã? (S/N): ").upper() == "S":
        turnos_ativos.append("manhã")
    if input("Ativar tarde? (S/N): ").upper() == "S":
        turnos_ativos.append("tarde")
    if input("Ativar noite? (S/N): ").upper() == "S":
        turnos_ativos.append("noite")

# ----------- Função 5: Cálculo de capacidades diária, mensal e anual -----------

    dados = calcular_capacidade(turno_manha, turno_tarde, turno_noite, turnos_ativos)

    print("\n===== RESULTADO =====")
    print(f"Turnos ativos: {dados['turnos_ativos']}")
    print(f"Capacidade diária atual: {dados['capacidade_diaria']:,}")
    print(f"Capacidade diária total: {dados['capacidade_diaria_total']:,}")
    print(f"Capacidade mensal: {dados['capacidade_mensal']:,}")
    print(f"Capacidade anual: {dados['capacidade_anual']:,}")
    print(f"Diferença: {dados['diferenca_cap']:,}")
    print(f"Utilização: {dados['percentual_utilizacao']:.2f}%")


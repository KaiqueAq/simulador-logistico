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

    dados = calcular_capacidade(turno_manha, turno_tarde, turno_noite, turnos_ativos)

    print("\n===== RESULTADO =====")
    print(f"Turnos ativos: {dados['turnos_ativos']}")
    print(f"Capacidade diária atual: {dados['capacidade_diaria']:,}")
    print(f"Capacidade diária total: {dados['capacidade_diaria_total']:,}")
    print(f"Capacidade mensal: {dados['capacidade_mensal']:,}")
    print(f"Capacidade anual: {dados['capacidade_anual']:,}")
    print(f"Diferença: {dados['diferenca_cap']:,}")
    print(f"Utilização: {dados['percentual_utilizacao']:.2f}%")
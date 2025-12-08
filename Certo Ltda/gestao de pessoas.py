def cadastrar_funcionario(lista_funcionarios):
    print("_+=+=+=+=+=+=+=+=+=+=+=+=+=+_")
    print("|  Cadastro de Funcionário  |")
    print("*---------------------------*")
    
    # Validação simples de nome
    while True:
        nome = input("Nome completo: ").strip()
        if len(nome) > 2:
            break
        print("Erro: O nome é muito curto.")

    # Validação de CPF (11 dígitos e unicidade)
    while True:
        cpf = input("CPF (11 números): ").strip()
        if not cpf.isdigit() or len(cpf) != 11:
            print("Erro: CPF deve conter exatamente 11 dígitos numéricos.")
            continue
        
        # Verifica se já existe
        cpf_existe = False
        for f in lista_funcionarios:
            if f['cpf'] == cpf:
                cpf_existe = True
                break
        
        if cpf_existe:
            print("Erro: Este CPF já está cadastrado no sistema.")
        else:
            break # CPF válido e único

    # Validação de RG (10 caracteres)
    while True:
        rg = input("RG (10 caracteres): ").strip()
        if len(rg) != 10:
            print("Erro: RG deve conter exatamente 10 caracteres.")
        else:
            break

    endereco = input("Endereço: ")
    telefone = input("Telefone: ")
    
    try:
        filhos = int(input("Número de filhos: "))
        if filhos < 0: filhos = 0
    except ValueError:
        filhos = 0
    
    # Validação rigorosa de Cargo
    print("\nCargos disponíveis: " + ", ".join(valores_hora.keys()))
    
    while True:
        entrada_cargo = input("Digite o cargo: ").strip().capitalize()
        if entrada_cargo in valores_hora:
            cargo = entrada_cargo
            break
        else:
            print(f"Erro: Cargo '{entrada_cargo}' inválido. Escolha um da lista acima.")

    novo_func = {
        "nome": nome,
        "cpf": cpf,
        "rg": rg,
        "endereco": endereco,
        "telefone": telefone,
        "filhos": filhos,
        "cargo": cargo
    }

    lista_funcionarios.append(novo_func)
    sec.salvar_dados(lista_funcionarios, arquivo_funcionarios)
    print("Funcionário cadastrado com sucesso!")
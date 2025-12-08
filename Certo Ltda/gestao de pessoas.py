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

    
def editar_funcionario(lista_funcionarios):
    print("_+=+=+=+=+=+=+=+=+=+=+=+=_")
    print("|   Editar Funcionário   |")
    print("*------------------------*")
    cpf_busca = input("Digite o CPF do funcionário que deseja editar: ").strip()

    funcionario_encontrado = None
    for f in lista_funcionarios:
        if f['cpf'] == cpf_busca:
            funcionario_encontrado = f
            break
    
    if not funcionario_encontrado:
        print("Funcionário não encontrado!")
        input("Enter para voltar...")
        return

    while True:
        print(f"\nEditando: {funcionario_encontrado['nome']} (Cargo: {funcionario_encontrado['cargo']})")
        print("[1] Nome")
        print("[2] Endereço")
        print("[3] Telefone")
        print("[4] Filhos")
        print("[5] Cargo")
        print("[0] Voltar/Salvar")
        
        opcao_edicao = input("Qual dado deseja alterar? ")

        match opcao_edicao:
            case "1":
                novo_nome = input("Novo nome: ").strip()
                if len(novo_nome) > 2:
                    funcionario_encontrado['nome'] = novo_nome
                else:
                    print("Nome inválido.")
            case "2":
                funcionario_encontrado['endereco'] = input("Novo endereço: ")
            case "3":
                funcionario_encontrado['telefone'] = input("Novo telefone: ")
            case "4":
                try:
                    funcionario_encontrado['filhos'] = int(input("Novo número de filhos: "))
                except ValueError:
                    print("Valor inválido.")
            case "5":
                print("Cargos disponíveis: " + ", ".join(valores_hora.keys()))
                while True:
                    novo_cargo = input("Novo cargo: ").strip().capitalize()
                    if novo_cargo in valores_hora:
                        funcionario_encontrado['cargo'] = novo_cargo
                        break
                    else:
                        print(f"Erro: Cargo '{novo_cargo}' inválido. Escolha um da lista acima.")
            case "0":
                break
            case _:
                print("Opção inválida.")
        
        # Salva a cada alteração ou ao sair
        sec.salvar_dados(lista_funcionarios, arquivo_funcionarios)
        print("Dados atualizados.")

def excluir_funcionario(lista_funcionarios):
    print("_+=+=+=+=+=+=+=+=+=+=+=+_")
    print("|  Excluir Funcionário  |")
    print("*-----------------------*")
    cpf_busca = input("Digite o CPF do funcionário que deseja excluir: ").strip()

    funcionario_encontrado = None
    for f in lista_funcionarios:
        if f['cpf'] == cpf_busca:
            funcionario_encontrado = f
            break
    
    if not funcionario_encontrado:
        print("Funcionário não encontrado!")
        input("Enter para voltar...")
        return

    print(f"\nATENÇÃO: Você vai excluir o funcionário:")
    print(f"Nome: {funcionario_encontrado['nome']}")
    print(f"Cargo: {funcionario_encontrado['cargo']}")
    print(f"CPF: {funcionario_encontrado['cpf']}")

    confirmacao = input("Tem certeza? Digite 'S' para confirmar: ").lower()
    
    if confirmacao == 's':
        lista_funcionarios.remove(funcionario_encontrado)
        sec.salvar_dados(lista_funcionarios, arquivo_funcionarios)
        print("Funcionário excluído com sucesso!")
    else:
        print("Operação cancelada.")
    
    input("Enter para continuar...")

def listar_funcionarios(lista_funcionarios):
    print("_+=+=+=+=+=+=+=+=+=+=+=+=+_")
    print("|  Lista de Funcionários  |")
    print("*-------------------------*")

    if not lista_funcionarios:
        print("Nenhum funcionário cadastrado.")
        input("Enter para voltar...")
        return
    
    for f in lista_funcionarios:
        print(f"Nome: {f['nome']} | Cargo: {f['cargo']} | CPF: {f['cpf']} | RG: {f['rg']}")
    input("Enter para voltar...")

def popular_dados_teste(lista_funcionarios):
    # dados fictícios ajustados para as novas regras de validação (CPF 11, RG 10)
    # CPFs fictícios gerados apenas para teste
    dados_padrao = [
        {"nome": "Ana Souza", "cpf": "11111111111", "rg": "1111111111", "endereco": "Rua A", "telefone": "11", "filhos": 1, "cargo": "Operário"},
        {"nome": "Bruno Lima", "cpf": "22222222222", "rg": "2222222222", "endereco": "Rua B", "telefone": "22", "filhos": 0, "cargo": "Operário"},
        {"nome": "Carlos Silva", "cpf": "33333333333", "rg": "3333333333", "endereco": "Rua C", "telefone": "33", "filhos": 2, "cargo": "Supervisor"},
        {"nome": "Daniela Reis", "cpf": "44444444444", "rg": "4444444444", "endereco": "Rua D", "telefone": "44", "filhos": 0, "cargo": "Gerente"},
        {"nome": "Eduardo Mello", "cpf": "55555555555", "rg": "5555555555", "endereco": "Rua E", "telefone": "55", "filhos": 3, "cargo": "Diretor"},
    ]
    
    adicionados = 0
    for novo in dados_padrao:
        # Verifica duplicidade de CPF antes de adicionar automaticamente
        ja_existe = False
        for existente in lista_funcionarios:
            if existente['cpf'] == novo['cpf']:
                ja_existe = True
                break
        
        if not ja_existe:
            lista_funcionarios.append(novo)
            adicionados += 1

    sec.salvar_dados(lista_funcionarios, arquivo_funcionarios)
    print(f"{adicionados} funcionários de teste foram adicionados!")
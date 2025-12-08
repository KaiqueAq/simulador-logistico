import utils.salvar_e_carregar as sec
from datetime import datetime
from utils.limpatela import limpaTela

arquivo_funcionarios = "funcionarios.txt"
arquivo_folha_pagamento = "folha_de_pagamento.txt"

# tabela de valores hora por cargo (configuração)
valores_hora = {
    "Operário": 15.0,
    "Supervisor": 40.0,
    "Gerente": 60.0,
    "Diretor": 80.0
}

def menu_gestao_pessoas(lista_funcionarios):
    # verifica se a lista está vazia e pergunta se quer popular com dados de teste
    if not lista_funcionarios:
        print("A lista de funcionários está vazia.")
        resp = input("Deseja carregar 5 funcionários de teste automaticamente? (S/N): ").lower()
        if resp == 's':
            popular_dados_teste(lista_funcionarios)

    while True:
        limpaTela()
        print('+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=')
        print('|        MENU GESTÃO DE PESSOAS      |')
        print('------------------------------------')
        print('|[1] Cadastrar Funcionário           |')
        print('|[2] Gerar Folha de Pagamento        |')
        print('|[3] Listar Funcionários             |')
        print('|[4] Editar Funcionário              |')
        print('|[5] Excluir Funcionário             |')
        print('|[6] Voltar ao Menu Principal        |')
        print('------------------------------------')
        opcao = input('Digite a opção desejada: ')

        match opcao:
            case "1":
                limpaTela()
                cadastrar_funcionario(lista_funcionarios)
            case "2":
                limpaTela()
                gerar_folha_pagamento(lista_funcionarios)
            case "3":
                limpaTela()
                listar_funcionarios(lista_funcionarios)
            case "4":
                limpaTela()
                editar_funcionario(lista_funcionarios)
            case "5":
                limpaTela()
                excluir_funcionario(lista_funcionarios)
            case "6":
                return
            case _:
                input('Opção inválida. Enter para continuar.')

def gerar_folha_pagamento(lista_funcionarios):
    if not lista_funcionarios:
        print("Nenhum funcionário cadastrado.")
        return

    # ordena a lista por nome
    lista_ordenada = sorted(lista_funcionarios, key=lambda x: x['nome'])
    
    carga_padrao = 160
    data_atual = datetime.now().strftime("%d/%m/%Y %H:%M")

    # Prepara o conteúdo para exibir e salvar
    linhas_relatorio = []
    
    cabecalho_topo = "="*100
    titulo = f"FOLHA DE PAGAMENTO - GERADA EM: {data_atual}"
    cabecalho_colunas = f"{'NOME':<20} | {'CARGO':<10} | {'BRUTO':<10} | {'EXTRAS':<10} | {'LÍQUIDO':<10} | {'IR ANUAL':<10} | {'PAGA IR?'}"
    
    linhas_relatorio.append(cabecalho_topo)
    linhas_relatorio.append(titulo)
    linhas_relatorio.append(cabecalho_topo)
    linhas_relatorio.append(cabecalho_colunas)
    linhas_relatorio.append("="*100)

    for func in lista_ordenada:
        cargo = func['cargo']
        valor_h = valores_hora.get(cargo, 15.0)
        
        # cálculo base
        salario_base = valor_h * carga_padrao
        
        # cálculo horas extras
        valor_extras = 0.0
        horas_extras_feitas = 0
        
        # gerentes e diretores não recebem hora extra (regra de negócio)
        if cargo not in ["Gerente", "Diretor"]:
            # simulando horas extras (fixo em 5h para visualização no relatório)
            horas_extras_feitas = 5 
            valor_extras = horas_extras_feitas * (valor_h * 2) # 100% de acréscimo
        
        salario_bruto = salario_base + valor_extras
        
        # descontos
        desconto_inss = calcular_inss(salario_bruto)
        base_ir = salario_bruto - desconto_inss
        
        irpf_anual = calcular_irpf_anual(base_ir)
        salario_liquido = salario_bruto - desconto_inss - (irpf_anual / 12) # desconta o ir mensal aproximado
        
        paga_ir = "Sim" if irpf_anual > 0 else "Não"
        
        linha_formatada = f"{func['nome']:<20} | {cargo:<10} | R${salario_bruto:<8.2f} | R${valor_extras:<8.2f} | R${salario_liquido:<8.2f} | R${irpf_anual:<8.2f} | {paga_ir}"
        linhas_relatorio.append(linha_formatada)

    linhas_relatorio.append("="*100)

    # 1. Exibir na tela
    print("\n")
    for linha in linhas_relatorio:
        print(linha)
    
    # 2. Salvar no arquivo persistente
    try:
        with open(arquivo_folha_pagamento, "w", encoding="utf-8") as arq:
            for linha in linhas_relatorio:
                arq.write(linha + "\n")
        print(f"\n>> Relatório salvo com sucesso em '{arquivo_folha_pagamento}'")
    except Exception as e:
        print(f"Erro ao salvar o arquivo: {e}")

    input("Pressione Enter para voltar...")

def cadastrar_funcionario(lista_funcionarios):
    print("+=+=+=+=+=+=+=+=+=+=+=+=+=+")
    print("|  Cadastro de Funcionário  |")
    print("---------------------------")
    
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
        if not rg.isdigit() or len(rg) != 10:
            print("Erro: RG deve conter exatamente 10 dígitos numéricos.")
            continue
        
        # Verifica se já existe
        rg_existe = False
        for r in lista_funcionarios:
            if r['rg'] == rg:
                rg_existe = True
                break
        
        if rg_existe:
            print("Erro: Este RG já está cadastrado no sistema.")
        else:
            break # RG válido e único


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
    print("+=+=+=+=+=+=+=+=+=+=+=+=")
    print("|   Editar Funcionário   |")
    print("------------------------")
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
    print("+=+=+=+=+=+=+=+=+=+=+=+")
    print("|  Excluir Funcionário  |")
    print("-----------------------")
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
    print("+=+=+=+=+=+=+=+=+=+=+=+=+")
    print("|  Lista de Funcionários  |")
    print("-------------------------")

    if not lista_funcionarios:
        print("Nenhum funcionário cadastrado.")
        input("Enter para voltar...")
        return
    
    for f in lista_funcionarios:
        print(f"Nome: {f['nome']} | Cargo: {f['cargo']} | CPF: {f['cpf']} | RG: {f['rg']}")
    input("Enter para voltar...")

def calcular_inss(salario_bruto):
    # cálculo simplificado progressivo 2024/2025
    if salario_bruto <= 1412.00:
        return salario_bruto * 0.075
    elif salario_bruto <= 2666.68:
        return salario_bruto * 0.09
    elif salario_bruto <= 4000.03:
        return salario_bruto * 0.12
    elif salario_bruto <= 7786.02:
        return salario_bruto * 0.14
    else:
        return 7786.02 * 0.14 # teto

def calcular_irpf_anual(base_calculo_mensal):
    # tabela progressiva mensal simplificada
    ir_mensal = 0.0
    
    if base_calculo_mensal <= 2259.20:
        ir_mensal = 0.0
    elif base_calculo_mensal <= 2826.65:
        ir_mensal = (base_calculo_mensal * 0.075) - 169.44
    elif base_calculo_mensal <= 3751.05:
        ir_mensal = (base_calculo_mensal * 0.15) - 381.44
    elif base_calculo_mensal <= 4664.68:
        ir_mensal = (base_calculo_mensal * 0.225) - 662.77
    else:
        ir_mensal = (base_calculo_mensal * 0.275) - 896.00
        
    if ir_mensal < 0: ir_mensal = 0
    
    # retorna a projeção anual
    return ir_mensal * 12

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
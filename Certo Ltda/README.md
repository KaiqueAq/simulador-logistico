# Simulador Logístico - Certo Ltda

## 📝 Descrição

Este projeto é um sistema de console desenvolvido em Python que simula o gerenciamento de um centro de distribuição. Ele abrange as principais áreas de uma operação logística: Operacional, Estoque, Financeiro e Recursos Humanos. O sistema utiliza arquivos de texto com formatação JSON para persistir os dados, funcionando como um banco de dados simples.

O objetivo é fornecer uma ferramenta para automação e análise de processos em um ambiente de armazém, conforme os requisitos da avaliação de aprendizagem.

---

## ✨ Funcionalidades

O sistema é dividido em quatro módulos principais:

### 1. 🚀 Módulo Operacional (`operacional.py`)

- **Cálculo de Capacidade:** Simula a capacidade de movimentação (entrada/saída) do centro com base em 1, 2 ou 3 turnos de trabalho (manhã, tarde, noite).
- **Projeções:** Exibe a capacidade diária, mensal e anual com base nos turnos ativos.
- **Análise de Ociosidade:** Mostra a diferença entre a capacidade atual e a capacidade total (100%), ajudando no planejamento.
- **Relatórios:** Salva a análise em `relatorio_operacional.txt`.

### 2. 📦 Módulo de Estoque (`estoque.py` e `estoque_saida.py`)

- **Entrada de Produtos:** Permite cadastrar novos produtos, evitando duplicidade por código e atualizando a quantidade se o item já existir.
- **Gestão de Inventário:** Funções para listar, editar e excluir produtos do estoque.
- **Status do Galpão:** Calcula e exibe a ocupação do armazém (3000m²) com base no porte e quantidade dos produtos, com uma barra de progresso visual e alertas de ocupação.
- **Saída de Produtos (Pedidos):**
  - Processa até 10 pedidos por dia, com reset automático diário.
  - Verifica a disponibilidade em estoque e permite atender pedidos parciais.
  - Atualiza a quantidade do item automaticamente após cada venda.
  - Registra cada pedido em `relatorio_pedidos.txt`.

### 3. 💰 Módulo Financeiro (`financeiro.py`)

- **Valor do Estoque:** Calcula o valor monetário total de todos os produtos no armazém.
- **Receita Bruta:** Analisa o relatório de pedidos para calcular a receita total gerada.
- **Projeção de Custos:** Simula custos operacionais (água, luz, salários) para calcular o custo por pallet, sugerir um preço de venda com margem de lucro e projetar lucros mensais/anuais. Salva a análise em `relatorio_financeiro.txt`.

### 4. 👥 Módulo de Gestão de Pessoas (`gestao_de_pessoas.py`)

- **Cadastro de Funcionários:** Registra funcionários com dados pessoais e cargo, evitando duplicidade de CPF e RG.
- **Cálculo de Salário:** Calcula o salário bruto com base no cargo e horas, incluindo horas extras (com 100% de acréscimo) para cargos elegíveis.
- **Descontos Legais:** Aplica descontos de INSS e IRPF com base nas faixas salariais vigentes.
- **Folha de Pagamento:** Gera um relatório completo (`folha_de_pagamento.txt`) ordenado por nome, detalhando salário bruto, extras, descontos e salário líquido.

---

## 🛠️ Tecnologias Utilizadas

- **Linguagem:** Python 3
- **Persistência de Dados:** Arquivos de texto (`.txt`) com estrutura JSON para armazenar e carregar dados de estoque e funcionários.

---

## 📂 Estrutura do Projeto

```
Certo Ltda/
├── main.py                   # Ponto de entrada, menu principal
├── operacional.py            # Módulo de cálculo de capacidade
├── estoque.py                # Módulo de entrada e gestão de estoque
├── estoque_saida.py          # Módulo de saída de produtos (pedidos)
├── financeiro.py             # Módulo de análises financeiras
├── gestao_de_pessoas.py      # Módulo de Recursos Humanos
└── utils/
    ├── limpatela.py          # Utilitário para limpar o console
    └── salvar_e_carregar.py  # Funções para manipular os arquivos de dados

dados/
├── estoque.txt               # "Banco de dados" dos produtos
├── funcionarios.txt          # "Banco de dados" dos funcionários
├── relatorio_pedidos.txt     # Histórico de todas as saídas
├── relatorio_financeiro.txt  # Relatório de projeção de custos
└── folha_de_pagamento.txt    # Relatório da folha de pagamento
```

---

## 🚀 Como Executar

1.  **Pré-requisitos:** Certifique-se de ter o Python 3 instalado em sua máquina.

2.  **Clone o repositório** (ou baixe os arquivos para uma pasta em seu computador).

3.  **Execute o programa:** Abra um terminal ou prompt de comando, navegue até a pasta raiz do projeto (`simulador-logistico`) e execute o seguinte comando:

    ```bash
    python "Certo Ltda/main.py"
    ```

4.  Navegue pelos menus utilizando as opções numéricas apresentadas no console.

---

## 👨‍💻 Autores

Desenvolvido por [Juliana Evangelista](https://www.linkedin.com/in/juliana-santos-52bb49275?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app), [Rafael Pirôpo dos Santos](https://www.linkedin.com/in/rafael-pir%C3%B4po-19714538b/), e [Kaique Aquino](https://www.linkedin.com/in/kaique-aquino/)  
Orientação: Prof. [Washington](https://www.linkedin.com/in/wlsa2912/)  
Projeto Acadêmico — 2025

## 💰 Sistema Bancário Simples em Python

Sistema bancário simples desenvolvido em Python, criado como exercício para praticar lógica de programação, estruturas de controle, manipulação de dados no terminal e conceitos básicos de orientação a objetos e funções.

### 📋 Funcionalidades

O sistema permite:

* **Depósito**: Adicionar saldo à conta.
* **Saque**: Realizar saques limitados a R\$ 500 por operação e até 3 vezes por sessão.
* **Extrato**: Exibir histórico completo das transações e saldo atual.
* **Transferência**: Transferir valores para outra conta (simulação com verificação de conta).
* **Novo usuário**: Cadastrar usuários com CPF, nome, data de nascimento e endereço.
* **Nova conta**: Criar novas contas associadas a usuários cadastrados.
* **Listar contas**: Exibir as contas existentes com dados da agência, número e titular.
* **Sair**: Encerra o programa.

### ▶️ Como executar

Você pode rodar este projeto de duas maneiras:

#### ✅ Opção 1: Usando o terminal local (com Python instalado)

1. Certifique-se de ter o **Python** instalado no seu computador.
2. Faça o download do arquivo `atividade_python.py` ou clone este repositório.
3. No terminal, navegue até a pasta onde o arquivo está salvo.
4. Execute o script com o comando:
```
python atividade_python.py
```
#### ✅ Opção 2: Usando o Google Colab (no navegador)

1. Acesse o site: [https://colab.research.google.com](https://colab.research.google.com)
2. Clique em **"Upload"** e envie o arquivo `atividade_python.py`.
3. Execute o código diretamente no navegador.

### 🧠 Lógica e Fluxo Implementados

* Validação e controle de depósitos e saques.
* Limite de saque de R$ 500,00 por operação e até 3 saques por sessão.
* Simulação de transferência com verificação do número da conta.
* Cadastro de múltiplos usuários com dados completos (CPF, nome, nascimento, endereço).
* Criação de contas bancárias associadas a usuários.
* Exibição detalhada do extrato de transações.
* Listagem de todas as contas criadas com informações da agência, número da conta e titular.
* Verificação para evitar cadastro duplicado de usuário (CPF único).
* Uso de funções claras para modularização do código.

### 🛠️ Tecnologias

* Python 

### 📌 Observações

* Sistema simulado — não realiza transações financeiras reais.
* Não utiliza banco de dados; dados são mantidos em memória apenas durante a execução.
* Ótimo para aprendizado de estruturas de controle, funções, listas e manipulação básica de dados em Python.

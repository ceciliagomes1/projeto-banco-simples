## 💰 Sistema Bancário Simples em Python

Este é um simples sistema bancário em Python feito como exercício para praticar lógica de programação, estrutura de controle e manipulação de dados básicos no terminal.

### 📋 Funcionalidades

O sistema permite:

* **Depósito**: Adicionar saldo à conta.
* **Saque**: Realizar saques limitados a R\$ 500 por operação e até 3 vezes por dia.
* **Extrato**: Ver o histórico das transações e o saldo atual.
* **Transferência**: Transferir valores para outra conta (simulação com verificação de conta).
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
3. Execute o código diretamente no navegador, célula por célula.

### 🧠 Lógica implementada

* Controle de **limite de saque** (até R\$ 500 por saque).
* Limitação de **número de saques** por sessão (máximo 3).
* Validação de entrada para evitar valores inválidos.
* Armazenamento do **extrato** como histórico textual.
* Simulação de transferência com verificação do número da conta.

### 🛠️ Tecnologias

* Python 

### 📌 Observações

* Este sistema é apenas uma simulação e não realiza transações reais.
* Não utiliza banco de dados nem interface gráfica.
* Ideal para fins didáticos e aprendizado de Python.

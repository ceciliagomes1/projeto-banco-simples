menu = '''

 [1] Deposito
 [2] Extrato
 [3] Saque
 [4] Transferência
 [5] Sair

=> '''

saldo = 0
limite = 500
numero_saques = 0
limite_saques = 3
extrato = ''


while True:
    opcao = input(menu)

    if opcao == '1':
        valor = float(input("\nInforme o valor do deposito: "))

        if valor > 0:
            saldo += valor
            extrato += f'Deposito no valor de: R$ {valor:.2f}\n'
            print("\nDeposito realizado com sucesso!")

        else:
            print("\nOperação falhou! Valor informado é inválido.")

    elif opcao == '2':
        print('\n=================== EXTRATO ===================')
        print('Não foram realizadas movimentações.' if not extrato else extrato)
        print(f'\nSaldo: R$ {saldo:.2f}')
        print('===============================================')

    elif opcao == '3':
        valor = float(input("\nInforme o valor do saque: "))
        excedeu_saldo = valor > saldo
        excedeu_saques = numero_saques >= limite_saques
        excedeu_limite = valor > limite

        if excedeu_saldo:
            print("\nOperação falhou! Você não tem saldo suficiente.")
    
        elif excedeu_saques:
            print(f"\nVocê já realizou {numero_saques} saques hoje. Tente novamente amanhã.")

        elif excedeu_limite:
            print("\nOperação falhou! O valor do saque excede o limite.")

        elif valor > 0:
            saldo -= valor
            extrato += f'Saque no valor de: R$ {valor:.2f}\n'
            numero_saques += 1
            print("\nSaque realizado com sucesso!")
        else:
            print("\nOperação falhou! O valor informado é inválido.")

    elif opcao == '4':
        valor = float(input("\nInforme o valor da transferência: "))

        if valor <= 0:
          print("\nOperação falhou! O valor informado é inválido.")

        elif valor > saldo:
          print("\nOperação falhou! Você não tem saldo suficiente.")

        elif valor > limite:
          print("\nOperação falhou! O valor da transferência excede o limite.")

        else:
          destino = input("\nInforme o número da conta de destino: ").strip()

          if not destino.isdigit() or int(destino) <= 0:
              print("\nOperação falhou! O número da conta de destino não pode ser vazio.")

          else:
            saldo -= valor
            extrato += f'Transferência no valor de: R$ {valor:.2f} para a conta {destino}\n'
            print("\nTransferência realizada com sucesso!")


    elif opcao == '5':
        print("\nObrigado por utilizar nossos serviços! Volte sempre.")
        break
    else:
        print("\nOpção inválida, por favor selecione novamente a operação desejada.")
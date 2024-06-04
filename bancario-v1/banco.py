menu = """
[d] = Depositar
[s] = Sacar
[e] = Extrato
[q] = Sair
=> 

"""

saldo = 0
limite_por_saque = 500
extrato = []
numero_saques_feitos = 0
LIMITE_SAQUE = 3

while True:
    opcao = input(menu)

    if opcao == 'd':
        print('Operação de Depósito: ')
        valor = float(input('Digite o valor que deseja depositar: '))
        if valor > 0:
            saldo += valor
            mensagem_extrato = f'Adicionado R${valor:.2f} ao saldo'
            extrato.append(mensagem_extrato)
        else:
            print("Valor inválido para depósito")

    elif opcao == 's':
        print('Operação de Saque:')
        if numero_saques_feitos < LIMITE_SAQUE:
            valor = float(input('Digite o valor que deseja sacar: '))
            if valor <= limite_por_saque:
                if saldo > valor:
                    saldo -= valor
                    mensagem_extrato = f'Retirando R${valor:.2f} do saldo'
                    extrato.append(mensagem_extrato)
                    numero_saques_feitos += 1
                else:
                    print("Não é possível sacar pois o valor na conta é inferior ao pedido")
            else:
                print('O valor solicitado é maior que o limite por saque que é de R$500.00')
        else:
            print('Limite de saques diários atingidos')

    elif opcao == 'e':
        print('Operação de Extrato: ')
        if len(extrato) == 0:
            print('Não foram realizadas movimentações')
        
        else:
            for mensagem in extrato:
                print(f"{mensagem}\n")
            print(f'Saldo atual da conta: R${saldo:.2f}')
    
    elif opcao == 'q':
        print('Saindo da aplicação')
        break

    else:
        print('Operação inválida, tente novamente')
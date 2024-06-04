import textwrap


def saque(*, saldo: float, valor: float, extrato: list, limite: int, numeros_saques: int, limite_saques: int):
    print("Operação de Saque:")
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numeros_saques >= limite_saques

    if excedeu_saldo:
        print("Sem saldo suficiente")
    
    elif excedeu_limite:
        print('Valor do saque excedido (limite R$500.00)')
    
    elif excedeu_saques:
        print('Número de saques excedidos')

    elif valor > 0:
        saldo -= valor
        extrato.append(f'Saque de R${valor:.2f}')
        numeros_saques += 1
        print("Saque realizado")
    
    else:
        print("Erro na operação")

    return saldo, extrato

def deposito(saldo, extrato, /):
    print("Operação de Depósito:")
    valor = float(input("Digite o valor que deseja depositar: "))
    if valor > 0:
        saldo += valor
        mensagem_extrato = f'Adicionado R${valor:.2f} ao saldo'
        extrato.append(mensagem_extrato)
        print('Depósito Realizado')
        return saldo, extrato
    else:
        print("Valor inválido")

def exibir_extrato(saldo: float, extrato:list):
    if len(extrato) == 0:
        print('Não foram realizadas movimentações')
        
    else:
        for mensagem in extrato:
            print(f"{mensagem}\n")
        print(f'Saldo atual da conta: R${saldo:.2f}')

def criar_usuario(usuarios):
    cpf = int(input('Digite os números do seu CPF: '))
    cadastrado = buscar_cpf_usuarios(cpf, usuarios)
    if cadastrado:
        print("CPF já cadastrado")
        return
    nome = input("Digite o nome do usuário: ")
    data_nascimento = input("Digite a data de nascimento: ")
    endereco = input('Digite o seu endereco (Logradouro - bairro - cidade - estado): ')

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereço": endereco})
    print("Usuário Criado com sucesso")


def buscar_cpf_usuarios(cpf, lista_usuarios):
    lista_usuarios_filtrados = [usuario for usuario in lista_usuarios if usuario["cpf"] == cpf]
    return lista_usuarios_filtrados[0] if lista_usuarios_filtrados else None


def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário")
    usuario = buscar_cpf_usuarios(cpf, usuarios)

    if usuarios:
        print("Conta criada com sucesso")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    
    print("Usuário não encontrado, abortado")

def menu():
    menu = """
    [u] = Criar usuário
    [c] = Criar conta
    [d] = Depositar
    [s] = Sacar
    [e] = Extrato
    [q] = Sair
    => 

    """
    return input(textwrap.dedent(menu))  

def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    numeros_saques = 0
    saldo = 0
    limite = 500
    extrato = []
    usuarios = []
    contas = []
    nro_conta = 1

    while True:
        opcao = menu()

        if opcao == 'u':
            criar_usuario(usuarios)

        elif opcao == 'c':
            conta = criar_conta(AGENCIA, nro_conta, usuarios)

            if conta:
                contas.append(conta)
                nro_conta += 1

        elif opcao == 'd':
            saldo, extrato = deposito(saldo, extrato)
        
        elif opcao == 's':
            valor = float(input("Digite o valor do saque: "))
            saldo, extrato = saque(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numeros_saques=numeros_saques,
                limite_saques=LIMITE_SAQUES,
            )

        elif opcao == 'e':
            exibir_extrato(saldo, extrato)
    
        elif opcao == 'q':
            print('Saindo da aplicação')
            break

        else:
            print('Operação inválida, tente novamente')



main()
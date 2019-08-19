def atm(valor_Saldo, idade, nome):

    x = int(input('''
        Digite (1) para saque \n
        Digite (2) para depósito \n
        Digite (3) para empréstimo \n
        Digite (4) para visualizar informações \n
        Digite (Qualquer outro caracter) para sair--->
    '''))
    try:
        if x == 1:
            saque(valor_Saldo)
        elif x == 2:
            deposito(valor_Saldo)
        elif x == 3:
            emprestimo(valor_Saldo, idade)
        elif x == 4:
            visualizar_info(nome,valor_Saldo, idade)
        else:
            print('Operação finalizada')
    except:
        print('Operação finalizada')


def visualizar_info(nome, valor_Saldo, idade):
    print('\n {nome} - {idade} anos \n Saldo: R$ {valor_Saldo}')
    return atm(valor_Saldo, idade, nome)


def saque(valor_Saldo):

    solicitar_S = int(input('Digite o valor do saque: '))

    if valor_Saldo < solicitar_S:
        print('nao foi possivel realizar o saque!')

    elif solicitar_S < 1000 :
        print('nao foi possivel realizar o saque!')

    elif solicitar_S >= 1000 :
        menor = valor_Saldo - solicitar_S
        print(menor)
        return atm(valor_Saldo, idade, nome)

def deposito(valor_Saldo):
    solicitar_D = int(input('Digite o valor do deposito: '))

    if solicitar_D > 5000 :
            print('nao foi possivel realizar o deposito!')
    else:
        maior = valor_Saldo + solicitar_D
        print(maior)
        return atm(valor_Saldo, idade, nome)

def emprestimo(valor_Saldo, idade):
    solicitar_E = int(input('Digite o valor do Emprestimo'))

    if idade < 21:
        print('nao foi possivel realizar o saque!')

    elif valor_Saldo < 1000:
        print('nao foi possivel realizar o saque!')

    elif solicitar_E >= 2000 and 15 * valor_Saldo:
        emprestimo = valor_Saldo + solicitar_E
        print(str(emprestimo))
        return atm(valor_Saldo, idade, nome)


print('Bem-vindo(a) ao GROGER BANK, para continuar cadastre as seguintes informações: ')
nome = input('Digite o seu nome completo: ')
idade = int(input('Digite sua idade: '))
valor_Saldo = float(input('(Simulação de Saldo) - Digite a simulação de saldo: '))
atm(valor_Saldo, idade, nome)
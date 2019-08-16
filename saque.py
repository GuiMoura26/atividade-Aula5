nome = input('Digite seu nome: ')
idade = int(input('Digite sua idade: '))
valor_Saldo = int(input('Digite o valor do saldo: '))

resposta = int(input('digite (1) para saque \n Digite (2) para depósito \n Digite (3) Para emprestimo\n digite (4) para visualizar informações \n Digite (Qualquer outro texto ou numero) para sair \n'))



solicitar_S = int(input('Digite o valor do saque: '))

if valor_Saldo < solicitar_S:
    print('nao foi possivel realizar o saque!')

elif solicitar_S < 1000 :
    print('nao foi possivel realizar o saque!')

elif solicitar_S >= 1000 :
    menor = valor_Saldo - solicitar_S
    print(menor)

















#DEPOSITO
# solicitar_D = int(input('Digite o valor do deposito: '))
#
# if solicitar_D > 5000 :
#     print('nao foi possivel realizar o deposito!')
#
# else :
#     maior = valor_Saldo + solicitar_D
#     print(maior)




#EMPRESTIMO

# solicitar_E = int(input('Digite o valor do Emprestimo'))
#
# if idade < 21:
#     print('nao foi possivel realizar o saque!')
#
# elif valor_Saldo < 1000 :
#     print('nao foi possivel realizar o saque!')
#
# elif solicitar_E >= 2000 and 15 * valor_Saldo :
#     emprestimo = valor_Saldo + solicitar_E
#     print(str(emprestimo))
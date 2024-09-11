# Crie um programa que receba dois números e uma operação (soma, subtração, multiplicação ou divisão) e execute a operação desejada.
n1 = float(input("escreva um número:"))
n2 = float(input('escreva outro número:'))

operação = input("escolha uma operação(soma, subtração, multiplicação ou divisão):")
if operação =="soma":
    print(n1+n2)
elif operação =="subtração":
    print(n1-n2)
elif operação =="multiplicação":
    print(n1*n2)
elif operação =="divisão":
    print(n1/n2)

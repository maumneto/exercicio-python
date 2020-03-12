# dados de entrada
valor_saque = int(input('Digite o valor do saque: '))
aux = valor_saque

Nota50 = aux//50
aux = aux % 50

Nota10 = aux//10
aux = aux % 10

Nota5 = aux//5
aux = aux % 5

Nota1 = aux//1
aux = aux % 1

print('Valor requerido: ', valor_saque)
print('Nota de 50: ', Nota50)
print('Nota de 10: ', Nota10)
print('Nota de 5: ', Nota5)
print('Nota de 1: ', Nota1)

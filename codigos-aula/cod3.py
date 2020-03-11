# import math

peso = float(input('Qual o seu peso: '))
altura = float(input('Qual a sua altura: '))
imc = peso/(altura*altura)
# imc = peso/(math.pow(altura, 2))

print('O resultado do IMC é ', imc)
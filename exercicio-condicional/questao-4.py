'''
Faça um programa que receba 3 valores digitados A, B e C, informando se estes podem ser os lados de um triângulo. O valores
A − B − C formam um triângulo somente se A < B + C para qualquer permutação de A, B e C. Caso seja um triângulo, diga se este
triângulo é isósceles, escaleno ou equilátero.
'''

# entrada de dados@
a = int(input('Digite o valor de A: '))
b = int(input('Digite o valor de B: '))
c = int(input('Digite o valor de C: '))

# condição para saber se o triângulo é valido ou não
if (a < b + c) and (b < a + c) and (c < b + a):
    print('Sao valores de um triangulo!')
    # verificando qual o tipo do triângulo
    if (a == b) and (b == c): 
        print('E um triangulo equilatero')
    elif (a != b) and (b != c) and (a != c):
        print('E escaleno')
    else:
        print('E isosceles')
else:
    print('Nao e um triangulo!')
'''
Faça um programa que calcule as raízes de uma equação do segundo
grau, na forma ax2+bx +c. O programa deverá pedir os valores de A,
B e C e fazer as consistências, informando ao usuário nas seguintes
situações:
 - Se o usuário informar o valor de A igual a zero, a equação não é
do segundo grau e o programa não deve fazer pedir os demais
valores, sendo encerrado;

- Se o delta calculado for negativo, a equação não possui raízes
reais. Informe ao usuário e encerre o programa;

- Se o delta calculado for igual a zero a equação possui apenas
uma raiz real; informe ao usuário;
Se o delta for positivo, a equação possui duas raiz reais;
informe-as ao usuário
'''

# dado de entrada!
a = float(input('Digite o valor de A: '))
# verificando se a equação é de fato de 2o grau
if (a == 0):
    print('Nao e equacao do segundo grau!')
else:
    # caso seja de 2o grau, então podemos receber os outros dados de entrada!
    b = float(input('Digite o valor de B: '))
    c = float(input('Digite o valor de C: '))
    # calculo de delta
    delta = (b**2)-(4*a*c)

    # condicional com base no valor de delta
    if (delta < 0):
        print('Nao existem raizes reais!')
    elif (delta == 0):
        x1 = (-b + (delta**(1/2))/(2*a))
        x1 = round(x1, 2)
        print('delta = ', delta)
        print('Possui somente uma raiz real cujo valor e: ', x1)
    else:
        x1 = (-b + (delta**(1/2))/(2*a))
        x1 = round(x1, 2)
        x2 = (-b - (delta**(1/2))/(2*a))
        x2 = round(x2, 2)
        print('delta = ', delta)
        print('Possui duas raizes reais cujos os valores sao: ', x1, ' e ', x2)
print('FIM - ALGORITMO!')
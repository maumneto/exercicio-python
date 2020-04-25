'''
Faça um programa que leia dois números e em seguida pergunte ao
usuário qual operação ele deseja realizar. As operações são: somar,
subtrair, multiplicar e dividir. O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
- par ou ímpar
- positivo ou negativo
'''

# entrada de dados
valor_1 = int(input('Digite o primeiro valor: '))
valor_2 = int(input('Digite o segundo valor: '))
# Nesse caso, pode ser feito de várias formas...usando inteiros, caractere ou strings para escolha do tipo de operação.
# Fica a critério do desenvolvedor escolher. Escolhi usar valor inteiros para representar as opções
print('Possibilidades:\n1-somar\n2-subtrair\n3-multiplicar\n4-dividir')
opcao = int(input('Escolha: '))
# variavel do resultado do calculo: inicialmente recebe a string 'error' 
res = 'error'

# condicional
if (opcao == 1):
    res = valor_1 + valor_2
    print('O resultado da soma e: ', res)
elif (opcao == 2):
    res = valor_1 - valor_2
    print('O resultado da subtracao e: ', res)
elif (opcao == 3):
    res = valor_1 * valor_2
    print('O resultado da multiplicacao e: ', res)
# essa opcao devemos ter cuidado..porque envolve uma condição interna
elif (opcao == 4):
    if (valor_2 == 0):
        print('Indefinido')
    else:
        res = valor_1 / valor_2
        print('O resultado da divisao e: ', res)
else:
    print('Nao foi escolhido nenhuma das opcoes!')

# verificando o estado da variável 'res'
if (res == 'error'):
    print('Fim do Algoritmo!')
else:
    # caso contrário, res tem um valor numérico válido!
    
    # verificando se é positivo ou negativo
    if (res >= 0):
        print('O numero e positivo')
    else:
        print('O numero e negativo')

    # varificando se é par ou ímpar
    if (res % 2 == 0):
        print('O numero e Par')
    else:
        print('O numero e Impar')
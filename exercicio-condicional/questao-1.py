'''
Faça um programa que leia o salário de um trabalhador e o valor
da prestação de um empréstimo. Se a prestação for maior que 20%
do salário imprima: “Empréstimo não concedido”; caso contrário imprima: “Empréstimo concedido”.
'''

# entrada de dados
salarao = float(input('Digite o valor do salario: '))
prestacao = int(input('Digite o valor da prestacao: '))

# condicional
if (prestacao > 0.2*salarao):
    print('Emprestimo nao concedido!')
else:
    print('Emprestimo concedido!')

# mensagem de término de algoritmo 
print('Fim do algoritmo!')
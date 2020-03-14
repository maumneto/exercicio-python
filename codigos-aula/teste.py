# Este codigo apresenta caracteristicas 
# de uma linguagem fracamente tipada.
import math
'''
Este codigo apresenta caracteristicas de uma linguagem fracamente tipada.
'''
idade = 33 
print(type(idade))
idade = 34.5
print(type(idade))
idade = 'TESTE'
print(type(idade))
idade = True
print(type(idade))

# print(dir(math))
# help(math.pow)
nota1 = float(input('Nota1: '))
nota2 = float(input('Nota2: '))
media  = (nota1+nota2)/2
if (media >= 7):
    print('Parabéns')
    print('Esta aprovado!')
    print('Vaza!')
else:
    print('Esta reprovado')
    print('Tente novamente!')
    
print('FIM-ALGORTIMO!')
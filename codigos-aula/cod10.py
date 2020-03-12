
import math 
# entrada de dados
nome_circuito = input('Digite o nome do circuito: ')
extensao = float(input('Digite a extensao do circuito (Km): '))
# constante de percurso minimo
per_min = 350
# gerando o numero de voltas
num_voltas = per_min/extensao
# convertendo para inteiro
# num_voltas = int(num_voltas)
# arredondamento pelo teto
print(num_voltas)
num_voltas = round(num_voltas)
print('O circuito ', nome_circuito, ' precisa de ', num_voltas, ' para completar 350Km')
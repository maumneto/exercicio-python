# entrada de dados
preco_1 = float(input('Produto 1: '))
preco_2 = float(input('Produto 2: '))
preco_3 = float(input('Produto 3: '))
# logica condicional
if (preco_1 < preco_2 and preco_1 < preco_3):
    print('Produto 1')
elif (preco_2 < preco_1 and preco_2 < preco_3):
    print('Produto 2')
elif (preco_3 < preco_1 and preco_3 < preco_2):
    print('Produto 3')
else:
    print('Qualquer um desses produtos')
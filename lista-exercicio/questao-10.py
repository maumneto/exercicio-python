# entrada de dados
letra = input('Digite M ou F: ')
# logica condicional
if (letra == 'M' or letra == 'm'):
    print('Masculino')
elif (letra == 'F' or letra == 'f'):
    print('Feminino')
else:
    print('Sexo Invalido!')
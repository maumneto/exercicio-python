import math

numero = int(input('Digite um numero positivo maior que 0: '))

num_quad = numero**2
print('O quadrado do valor ', numero,' é: ', num_quad)

num_cubo = numero**3
print('O cubo do valor ', numero,' é: ', num_cubo)

num_sqrt = math.sqrt(numero)
print('A raiz quadrado do valor ', numero,' é: ', round(num_sqrt,2))

num_sqrt_cub = numero**(1/3)
print('O quadrado do valor ', numero,' é: ', round(num_sqrt_cub, 2))
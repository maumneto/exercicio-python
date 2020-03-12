valor_hora = float(input('Digite o valor da hora: '))
horas_trab_mes = int(input('Digite as horas trabalhadas por mes: '))

salario_bruto = valor_hora*horas_trab_mes
IR = 0.11*salario_bruto
INSS = 0.08*salario_bruto
sindicato = 0.05*salario_bruto
descontos = IR + INSS + sindicato
salario_liquido = salario_bruto - descontos

print('+ salario bruto: R$: ', round(salario_bruto, 2))
print('- IR: R$: ', round(IR, 2))
print('- INSS: R$: ', round(INSS, 2))
print('- Sindicato: R$: ', round(sindicato, 2))
print('salario liquido: R$: ', round(salario_liquido, 2))


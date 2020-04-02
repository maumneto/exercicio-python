# entrada de dados 
nota_1 = float(input('Digite o valor da \033[1mprimeira\033[0m nota: '))
peso_1 = float(input('Digite o valor do \033[1mprimeiro\033[0m peso (0 - 1): '))

nota_2 = float(input('Digite o valor da \033[1msegunda\033[0m nota: '))
peso_2 = float(input('Digite o valor do \033[1msegundo\033[0m peso (0 - 1): '))

# calculo de media ponderada
media_pond = (nota_1*peso_1 + nota_2*peso_2)/(peso_1 + peso_2)

#saida de dados
print('\033[1mA média ponderada é: \033[0m', media_pond)
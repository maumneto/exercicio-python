'''
    ESTE PROJETO RAPIDO TEM O OBJETIVO DE DESENVOLVER
    O JOGO JOKENPO SIMPLES (CONHECIDO EM PORTUGUÊS COMO: PEDRA, PAPEL E TESOURA).
    @author: maumneto
'''

import random as rdm

print('='*45)
print('Bem Vindo ao Jogo JOKENPO (Pedra-Papel-Tesoura)')
print('='*45)
print('')

# vetor com a lista de opções
list_option = ['PEDRA', 'PAPEL', 'TESOURA']


# entrada de dados: a opção que o jogador escolher!
while True:
    print('Opcoes:\n[0]-pedra\n[1]-papel\n[2]-tesoura')
    user = int(input('Digite a sua opcao: '))
    if (user >= 0 and user <= 2):
        break
    else:
        print('Opcao Incorreta! Escolha novamente!')
        print('')
# gerando a escolha do computador (um numero aleatório entre 0 e 2 inclusive)
computer = rdm.randint(0,2)

# apresentando as escolhas feitas!
print('')
print('--> Voce escolheu: %s' % list_option[user])
print('--> O Computador escolheu: %s' % list_option[computer])

# lógica do jogo
# caso o usuário digite pedra
print('')
if (user == 0): 
    if (computer == 0):
        print('EMPATE!')
    elif (computer == 1):
        print('PERDEU!')
    else:
        print('GANHOU!')
# caso o usuário digite papel
elif (user == 1):
    if (computer == 0):
        print('GANHOU!')
    elif (computer == 1):
        print('EMPATE!')
    else:
        print('PERDEU!')
# caso o usuário digite tesoura
else:
    if (computer == 0):
        print('PERDEU!')
    elif (computer == 1):
        print('GANHOU!')
    else:
        print('EMPATE!')

# mensagem de fim de algoritmo!
print('')
print('='*35)
print('FIM DE JOGO!')
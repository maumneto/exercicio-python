'''
PROJETO JOKENPO USANDO RECURSOS MAIS AVANÇADOS QUE A VERSÃO SIMPLES.
criado por @maumneto
'''

from random import randint
from time import sleep
import os

# funcao que cria a tela de boas vindas ao jogo!
def welcomeScreen():
    os.system('clear')
    print('-='*16)
    print('\033[1m BEM VINDO AO JOGO JO-KEN-PO \033[0m')
    print('\033[1m criado por @maumneto \033[0m')
    print('-='*16)
    print('')

# funcao em que será implementada a lógica do jogo
def gameLogic(user, computer, usrScore = 0, pcScore = 0):
    
    # opcao caso ele queira jogar novamente
    if (user == 'PEDRA'): 
        if (computer == 'PEDRA'):
            print('EMPATE!')
        elif (computer == 'PAPEL'):
            print('PERDEU!')
            pcScore += 1
        else:
            print('GANHOU!')
            usrScore += 1
    # caso o usuário digite papel
    elif (user == 'PAPEL'):
        if (computer == 'PEDRA'):
            print('GANHOU!')
            usrScore += 1
        elif (computer == 'PEDRA'):
            print('EMPATE!')
        else:
            print('PERDEU!')
            pcScore += 1

    # caso o usuário digite tesoura
    else:
        if (computer == 'PEDRA'):
            print('PERDEU!')
            pcScore += 1
        elif (computer == 'PAPEL'):
            print('GANHOU!')
            usrScore += 1
        else:
            print('EMPATE!')
    
    return (usrScore, pcScore)
    

# funcao principal onde se reune todas as outras funcoes
def main():
    welcomeScreen() # chamando a função 'welcomeScreen'
    
    # dados iniciais 
    usrScr = 0
    pcScr = 0
    option_list = ['PEDRA','PAPEL','TESOURA']
    
    while True:
        # entrada de dados: a opção que o jogador escolher!
        while True:
            print('Opcoes:\n- Pedra\n- Papel\n- Tesoura')
            user = input('Digite a sua opcao: ')
            user = user.upper()
            if (user == 'PEDRA' or user == 'PAPEL' or user == 'TESOURA'):
                break
            else:
                print('Opcao Incorreta! Escolha novamente!')
                print('')
        
        # gerando a escolha do computador (um numero aleatório entre 0 e 2 inclusive)
        computer = option_list[randint(0,2)]

        # iniciando o jogo
        print('')
        print('JO...')
        sleep(1)
        print('KEN...')
        sleep(1)
        print('PO!!')
        print('')

        # apresentando as escolhas feitas!
        print('-'*35)
        print('--> Voce escolheu: %s' % user)
        print('--> O Computador escolheu: %s' % computer)
        print('-'*35)

        # chamando a função 'gameLogic'
        usrScr, pcScr = gameLogic(user, computer, usrScr, pcScr)

        gameAgain = input('Deseja jogar novamente? s[sim]/n[nao]')
        gameAgain = gameAgain.upper()
        if (gameAgain == 'N'):
            os.system('clear')
            print('FIM DE JOGO!')
            print('A pontuacao foi: ')
            print('Voce: %d' % usrScr)
            print('Computador: %d' % pcScr)

            # verificar quem venceu e quem perdeu!
            if (usrScr > pcScr):
                print('')
                print('Voce foi o Vencedor! Parabens! ╰(▔∀▔)╯')
            elif (usrScr < pcScr):
                print('')
                print('Voce Perdeu! Melhor Sorte da Proxima Vez! ┐(¯ヘ¯)┌')
            else:
                print('')
                print('Deu Empate! ¯\_(ツ)_/¯')
            break   
        else:
            print('Vamos Novamente!\n')

# executando o módulo principal do jogo!
if __name__ == '__main__':
    main()
'''
ALGORITMO PARA CODIFICAR E DESCODIFICAR UMA PALAVRA
A cifra é um sistema que é utilizado para esconder o significado de uma mensagem trocando as letras
do alfabeto por outras letras ou símbolos!
Suponhamos que você queira enviar uma palavra codificada, ou seja, cada letra será substituída por 
por outra letra deslocada de N no alfabeto em relação a original. Vamos pegar o exemplo do N = 7! 
Com esse valor teríamos as seguintes substituíções: a => h, b => i, ...
Faça um programa que codifique e decodifique uma palavra com base no deslocamento de N posições do 
alfabeto.
'''

import os
import string as str
from time import sleep

# Função que codifica a palavra que foi passada como argumento e retorna uma string codificado
def cipherWord(word, key):
    alph = list(str.ascii_lowercase)
    word = list(word)
    newWord = []

    for i in range(len(word)):
        for j in range(len(alph)):
            if (alph[j] == word[i]):
                if (j + key > 25):
                    exc = (j + key) - 26
                    newWord.append(alph[exc])
                else:
                    newWord.append(alph[j + key])

    cryptoWord = ''.join(newWord)
    return cryptoWord

# Função que decodifica a palavra que foi passada como argumento e retorna uma string codificado
def decipherWord(cipherWord, key):
    alph = list(str.ascii_lowercase)
    cipherWord = list(cipherWord)
    newWord = []

    for i in range(len(cipherWord)):
        for j in range(len(alph)):
            if (alph[j] == cipherWord[i]):
                newWord.append(alph[j - key])

    cryptoWord = ''.join(newWord)
    return cryptoWord


# Função que codifica a mensagem
def encodedMessage(message, key):
    message = message.split()
    newArray = []

    for i in range(len(message)):
        newArray.append(cipherWord(message[i], key))

    newMassage = ' '.join(newArray)
    return newMassage


# Função que decodifica a mensagem
def decodedMessage(message, key):
    message = message.split()
    newArray = []
    for i in range(len(message)):
        newArray.append(decipherWord(message[i], key))
    recoveredMessage = ' '.join(newArray)
    return recoveredMessage


# Função principal do programa
def main():
    os.system('clear')
    message = input('Digite a frase para ser criptografada: ')
    key = int(input('Digite a chave da mensagem: '))
    print('\nCodificando a mensagem...')
    sleep(2)
    messageEnconded = encodedMessage(message.lower(), key)
    print('\033[1mMensagem Codificada!\033[0m\n$ %s\n' % messageEnconded)

    while True:
        verifyKey = int(input('Digite a chave correta: '))
        if (verifyKey == key):
            print('\nIniciando decodificação...')
            sleep(2)
            messageRecovered = decodedMessage(messageEnconded.lower(), verifyKey)
            print('\033[1mMensagem Decodificada!\033[0m\n$ %s\n' % messageRecovered)
            break
        else:
            print('Erro! A chave inserida está incorreta.')
            print('Tente novamente!\n')
    
    print('Fim de Algoritmo')

# chamando a função principal
main()

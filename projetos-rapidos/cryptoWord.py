'''
ALGORITMO PARA CODIFICAR E DESCODIFICAR UMA PALAVRA
A cifra é um sistema que é utilizado para esconder o significado de uma mensagem trocando as letras
do alfabeto por outras letras ou símbolos!
Suponhamos que você queira enviar uma palavra codificada, ou seja, cada letra será substituída por 
por outra letra deslocada de N no alfabeto em relação a original. Vamos pegar o exemplo do N = 7! 
Com esse valor teríamos as seguintes substituíções: a => h, b => i, ...
Faça um programa que codifique e decodifique uma palavra com base no deslocamento de 7 posições do 
alfabeto (N = 7).
'''

import string as str
from time import sleep

# Função que codifica a palavra que foi passada como argumento e retorna uma string codificado
def cipherWord(word):
    alph = list(str.ascii_lowercase)
    word = list(word)
    newWord = []
    
    for i in range(len(word)):
        for j in range(len(alph)):
            if (alph[j] == word[i]):
                if (j + 7 > 25):
                    exc = (j + 7) - 26
                    newWord.append(alph[exc])
                    print(newWord)
                else:
                    newWord.append(alph[j + 7])
                    print(newWord)
    
    criptoStatement = ''.join(newWord)
    return criptoStatement

# Função que decodifica a palavra que foi passada como argumento e retorna uma string codificado
def decipherWord(cipherWord):
    alph = list(str.ascii_lowercase)
    cipherWord = list(cipherWord)
    newWord = []
    
    for i in range(len(cipherWord)):
        for j in range(len(alph)):
            if (alph[j] == cipherWord[i]):
                newWord.append(alph[j - 7])
                print(newWord)
    
    criptoStatement = ''.join(newWord)
    return criptoStatement

# Função principal do programa
def main():
    wordMessage = input('Digite a palavra para ser criptografada: ')
    encodedWord = cipherWord(wordMessage)
    print('%s ---> %s' % (wordMessage, encodedWord))
    sleep(2)
    print(' ')
    decodedWord = decipherWord(encodedWord)
    print('%s ---> %s' % (encodedWord, decodedWord))
    print('Fim de Algoritmo!')

main()



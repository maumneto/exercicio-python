"""
    @register
    @note: file with the function that create an account
"""
import random
import os
from utils import verify_client

# function to create an account
# @params: name [string]
#          cpf [int]
#          clients [list]
# @return: void 
def create_account(name = None, cpf = 0, clients = None):
    # create an client object
    client = {}
    # collect client data
    client['name'] = name
    client['cpf'] = int(cpf)
    client['account'] = random.randint(1000, 9999)
    client['password'] = input('Type a password: ')
    client['amount'] = float(input('Type initial amount: '))
    # add a client in a set of clients
    clients.append(client)
    # verify if the client was add in a set of clients
    os.system('clear')
    verify_client(client)
    # welcome prints
    print('\nWelcome Mr(s) %s!' % client['name'].upper())
    print('\nYour account number is: %d' % client['account'])

    

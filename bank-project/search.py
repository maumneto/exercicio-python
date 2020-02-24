"""
    @search
    @note: file with search and show all functions
"""
import random
from utils import verify_password

# function to search an account
# @params: clients [list]
#          account [int]
# @return: client [object]
def search_account(clients = None, account = 0):
    for i in range(len(clients)):
        if clients[i]['account'] == account:
            print('Registry Founded')
            password = input('Type your password: ')
            if verify_password(password, clients[i]):
                return clients[i]
    return;

# function to show all clients
# @params: clients [list]
# @return: void 
def show_all_registries(clients = None):
    for i in range(len(clients)):
        print('\033[1mName:\033[0m %s' % clients[i]['name'])
        print('\033[1mAccount Number:\033[0m %d' % clients[i]['account'])
        print('\n')

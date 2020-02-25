"""
** Project Number 1 - Digital Banking **

@author: maumneto (maumneto@gmail.com)

@message: This project has the objective implements a digital banking
using python language in a structure way 
"""

import os
from screens import welcome_screen, option_screen, end_screen
from register import create_account
from search import search_account, show_all_registries
from debit import debit
from credit import credit
from transfer import transference

# function main
def main():
    # clear terminal
    os.system('clear')
    # initial prints
    welcome_screen()
    # creating de list of clients (initially empty)
    list_of_clients = []

    while True:
        option_screen()
        # choosing an action!
        ch = int(input('Type action: '))
        os.system('clear')
        
        # first action: create an account 
        if ch == 1:
            name = input('Type your name: ')
            cpf = int(input('Type your CPF: '))
            create_account(name, cpf, list_of_clients)
        
        # second action: search an account in the list 
        elif ch == 2:
            client = {}
            account_search = int(input('Type your account number: '))
            client = search_account(list_of_clients, account_search)
            if client == None:
                print('Registry Not Found!')
            else:
                print('Your data are shown below:\n')
                print('\033[1mName:\033[0m %s' % client['name'].upper())
                print('\033[1mCPF:\033[0m %d' % client['cpf'])
                print('\033[1mAccount\033[0m number: %d' % client['account'])
                print('\033[1mAmount:\033[0m %d' % client['amount'])
                print('\n')

        # third action: show all accounts
        elif ch == 3:
            show_all_registries(list_of_clients)

        # fourth action: debit function
        elif ch == 4:
            account = int(input('Type your account number: '))
            debit(account, list_of_clients)

        # fifth action: credit function
        elif ch == 5:
            account = int(input('Type your account number: '))
            credit(account, list_of_clients)
        
        # sixth action: transference function
        elif ch == 6:
            account_sender = int(input('Type your account: '))
            account_receiver = int(
                input('Type the \033[1maccount receiver\033[0m: '))
            money_transfer = float(input('Type the value: '))
            transference(account_sender, account_receiver,
                         money_transfer, list_of_clients)
            print('Transference Success!')
        # seventh action: exit program
        elif ch == 7:
            end_screen()
            break

        else:
            print('\033[1mNo actions were selected\033[0m')


# calling the main function
if __name__ == '__main__':
    main()

"""
    @debit
    @note: file with debit function
"""
import os
from utils import verify_debit, verify_password

# debit function
# @params: account [string]
#          clients [list]
# @return: void
def debit(account, clients):
    for i in range(len(clients)):
        if clients[i]['account'] == account:
            print('Registry Founded')
            password = input('Type your password: ')
            
            if verify_password(password, client=clients[i]):
                os.system('clear')
                print('Welcome Mr(s). %s!' % clients[i]['name'])

                debit_value = float(input('Type the value of debit: '))
                verify_debit(clients[i], debit_value)
                clients[i]['amount'] = clients[i]['amount'] - debit_value;

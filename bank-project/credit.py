import os
from utils import verify_password

def credit(account, clients):
    for i in range(len(clients)):
        if clients[i]['account'] == account:
            print('Registry Founded')
            password = input('Type your password: ')
            
            if verify_password(password, client=clients[i]):
                os.system('clear')
                print('Welcome Mr(s). %s!' % clients[i]['name'])

                credit_value = float(input('Type the value of credit: '))
                # verify_debit(clients[i], debit_value)
                clients[i]['amount'] = clients[i]['amount'] + credit_value

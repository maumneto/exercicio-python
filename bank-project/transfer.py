"""
    @transfer
    @note: file with transference function
"""
import os
from search import search_account

# transference
# @params: account_sender [int]
#          account_receiver [int]
#          money [float]
#          list_clients [list]
# @return: void
def transference(account_sender, account_receiver, money, list_clients):
    for i in range(len(list_clients)):
        if list_clients[i]['account'] == account_sender:
            list_clients[i]['amount'] = list_clients[i]['amount'] - money
    
    for j in range(len(list_clients)):
        if list_clients[j]['account'] == account_receiver:
            list_clients[j]['amount'] = list_clients[j]['amount'] + money
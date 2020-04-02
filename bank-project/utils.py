"""
    @utils
    @note: file with functions used by other files
"""

# verify password
# @params: password [string]
#          client [object]
# @return: boolean
def verify_password(password, client):
    if client['password'] == password:
        return True
    else:
        print('\033[1mError! Wrong Password!\033[0m')
        return False

# verify debit
# @params: client [object]
#          value [float]
# @return: void
def verify_debit(client, value):
    if client['amount'] < value:
        print('\033[1mYou not have money enough!\033[0m')
    else:
        pass

# verify client
# @params: client [object]
# @return: void
def verify_client(client = None):
    if client == {}:
        print('\033[1mError! data not added!\033[0m')
    else:
        print('\033[1mClient successfully added!\033[0m')


# Create Account By Increment
# @params: client [object]
# @return: void
def createAccountByIncrement(array_clients):
    account = len(array_clients)
    return account

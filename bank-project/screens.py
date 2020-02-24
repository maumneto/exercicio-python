"""
    @screens
    @note: file with all screen functions. No one function needs
    parameters and its return nothing
"""
# function to print welcome message
def welcome_screen():
    print('\033[1m------------------------------------\033[0m')
    print('\033[1m--- WELCOME TO THE BANK PROJECT ----\033[0m')
    print('\033[1m------------------------------------\033[0m')

# function to print end message
def end_screen():
    print('\033[1m------------------------------------\033[0m')
    print('\033[1m------- END OF APPLICATION ---------\033[0m')
    print('\033[1m------------------------------------\033[0m')

# function to print option message
def option_screen():
    print('\033[1mOptions:\033[0m \n1 -- Create Register\n2 -- Search Register\n3 -- Show All Accounts\n4 -- Debit\n5 -- Credit\n6 -- Transference\n7 -- Exit')


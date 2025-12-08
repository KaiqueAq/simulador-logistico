import os

def limpaTela():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')  
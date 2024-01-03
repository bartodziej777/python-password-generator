import sys
import generate_password
import config

def initilization():
    print('''----------------------\n--PASSWORD-GENERATOR--\n----------------------''')

def menu():
    while True:
        print('''1. Generate password \n2. Change password configuration \n3. Exit''')
        uChoice = input('\n>>')
        match uChoice:
            case '1': 
                generate_password.generate()
            case '2':
                config.configMenu()
            case '3':
                print("Bye!")
                sys.exit()
            case _:
                print("Select the correct option to continue")

initilization()
menu()
        
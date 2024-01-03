config = {
    "password_length": 12,
    "enable_digits": True,
    "enable_special_chars": True,
    "enable_big_letters": True
}

def changePasswordLength():
    response = ''
    while not response.isdigit():
        response = input("Type password length (number): ")

    config['password_length'] = int(response);

def changeConfigProperty(propName, displayName):
    response = ''
    while response != 'y' and response != 'n':
        response = input(f"Enable {displayName}? (y/n)")
    
    if response == 'y':
        config[f"{propName}"] = True
    else:
        config[f"{propName}"] = False

def configMenu():
    print('''--------------------------\n--PASSWORD-CONFIGURATION--\n--------------------------''')
    print('''1.Password length\n2.Big letters\n3.Digits\n4.Special chars\n5.Go back''')
    while True:
        uChoice = input('>>')
        match uChoice:
            case '1':
                changePasswordLength()
            case '2':
                changeConfigProperty("enable_big_letters", "big letters")
            case '3':
                changeConfigProperty("enable_digits", "digits")
            case '4':
                changeConfigProperty("enable_special_chars", "special characters")
            case '5':
                break;
            case _:
                print("Select the correct option to continue")
            


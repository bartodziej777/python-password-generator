import string
import secrets
import config

digits = string.digits
specials = string.punctuation
smallLetters = string.ascii_lowercase
bigLetters = string.ascii_uppercase

def generate():
    while True:
        password = ''

        alphabet = smallLetters
        if config.config["enable_big_letters"]:
            alphabet += bigLetters
        if config.config["enable_digits"]: 
            alphabet += digits
        if config.config["enable_special_chars"]:
            alphabet += specials

        for _ in range(config.config["password_length"]):
            password += ''.join(secrets.choice(alphabet))
        break;

    print(f"GENERATED PASSWORD: {password}\n")
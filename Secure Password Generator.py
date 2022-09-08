#Import libraries for the password generator
import random
import secrets
import string

file_path = "C:\\Users\\Ololade\\Documents\\Python Projects\\Projects\\Stored Passwords"
extend = "\\"
pass_file = "secure_pass.txt"

#function to generate passwords
def passwordmaker(length: int, symbols: bool, uppercase: bool):

    with open(file_path + extend + pass_file, "a") as f:
        combination = string.ascii_lowercase + string.digits

        if symbols:
            combination += string.punctuation

        if uppercase:
            combination += string.ascii_uppercase

        combination_length = len(combination)

        new_pass = ""

        for _ in range(length):
            new_pass += combination[secrets.randbelow(combination_length)]
        f.write("Password: " + new_pass + "\n")

    return new_pass

for _, index in enumerate(range(5)):
    password = passwordmaker(length=10, symbols =True, uppercase=True)
    print(index + 1, ">>", password )


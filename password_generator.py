import secrets
import string

import colorama
from colorama import Fore, Back
colorama.init(autoreset=True)

print(Fore.BLACK + Back.YELLOW + " PASSWORD MANAGER ")

add_new = input(Fore.YELLOW + "Add new or generate password (a/g): ")

if add_new.lower() == "a":
    pass_name = input(Fore.YELLOW + "Name your password: ")
    my_pass = input(Fore.YELLOW + "Input your password: ")
    add_pass = open(f"Password for {pass_name}.txt", "w")
    add_pass.write(f"Saved password for {pass_name}: ")
    add_pass.write(my_pass)
    add_pass.close()
    print(Fore.GREEN + "Password saved")

elif add_new.lower() == "g":
    name = input(Fore.BLUE + "Name your password: ")
    try:
        pass_length = int(input(Fore.BLUE + "Enter your password length: "))
    except:
        print(Fore.BLACK + Back.RED + " ENTER VALID NUMBER ")
    special_chars = "!@#$%^&*_~;?<>{}[]"
    characters = string.ascii_letters + string.digits + special_chars

    while True:
        password = ''.join(secrets.choice(characters) for i in range(pass_length))
        password += secrets.choice(special_chars)
        if (any(c.islower() for c in password) and any(c.isupper()
        for c in password) and sum(c.isdigit() for c in password) >= 4):
            print(Fore.YELLOW + f"Password generated for {name}", ':', password)

            strength = len(password)
            if strength > 14:
                print(Fore.BLACK + Back.GREEN + " Your password is strong ")
            elif strength < 14:
                print(Fore.BLACK + Back.RED + " Password should be stronger ")
            need_save = input(Fore.BLUE + "Do you want to save this password? (y/n): ")
            break

    if need_save.lower() == "y":
        saving = open(f"Password for {name}.txt","w")
        saving.write(f"Generated password for {name}: ")
        saving.write(password)
        saving.close()
        print(Fore.GREEN + "Password saved")
    elif need_save == "n":
        print("---------------")
    else:
        print(Fore.BLACK + Back.RED + " INVALID OPTION ")

else:
    print(Fore.BLACK + Back.RED + " INVALID OPTION ")

import secrets
import string

import os.path

import colorama
from colorama import Fore, Back
colorama.init(autoreset=True)

print("Copyright(c) 2022 Ashfaaq Rifath")
print(Fore.BLACK + Back.YELLOW + " PASSWORD MANAGER ")

#asks the user if they need to generate or add a new password
pass_option = input("Add new or generate password (a/g): ")

if pass_option.lower() == "a":
    #the desired file path should be added here (hardcoded)
    default_path = "file path goes here"
    pass_name = input("Name your password: ")
    save_path = os.path.join(default_path, pass_name + ".txt")
    my_pass = input("Input your password: ")
    user_pass = len(my_pass)
    if user_pass > 14:
        #also contains a password strength meter
        print(Fore.BLACK + Back.GREEN + " Your password is strong ")

    elif user_pass < 14:
        print(Fore.BLACK + Back.RED + " Password should be stronger ")
        #takes the file path the user wants as an input
    choose_loc = input("Save to default location or custom location (d/c): ")

    if choose_loc.lower() == "d":
        add_pass = open(save_path, "w")
        add_pass.write(f"Saved password for {pass_name}: ")
        add_pass.write(my_pass)
        add_pass.close()
        print(Fore.GREEN + "Password saved")

    elif choose_loc == "c":
        print(Fore.BLACK + Back.YELLOW + " Enter correct file path ")
        custom_path = input("Enter file path: ")
        save_abs_path = os.path.join(custom_path, pass_name + ".txt")
        add_pass = open(save_abs_path, "w")
        add_pass.write(f"Saved password for {pass_name}: ")
        add_pass.write(my_pass)
        add_pass.close()
        print(Fore.GREEN + "Password saved")

    else:
        print(Fore.BLACK + Back.RED + "INVALID OPTION")

elif pass_option.lower() == "g":
    name = input("Name your password: ")
    try:
        pass_length = int(input("Enter password length: "))
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

            need_save = input("Do you want to save this password? (y/n): ")

            if need_save.lower() == "y":
                choose_loc = input("Save to default location or custom location (d/c): ")

            elif need_save == "n":
                print("---------------")

            else:
                print(Fore.BLACK + Back.RED + " INVALID OPTION ")
            break

    if choose_loc.lower() == "d":
        save_path = "file path goes here"
        def_path = os.path.join(save_path, name + ".txt")
        saving = open(def_path,"w")
        saving.write(f"Generated password for {name}: ")
        saving.write(password)
        saving.close()
        print(Fore.GREEN + "Password saved")

    elif choose_loc.lower() == "c":
        print(Fore.BLACK + Back.YELLOW + " Enter correct file path ")
        save_path = input("Enter file path: ")
        cus_path = os.path.join(save_path, name + ".txt")
        gen_pass = open(cus_path, "w")
        gen_pass.write(f"Saved password for {name}: ")
        gen_pass.write(password)
        gen_pass.close()
        print(Fore.GREEN + "Password saved")

    else:
        print(Fore.BLACK + Back.RED + " INVALID OPTION ")

else:
    print(Fore.BLACK + Back.RED + " INVALID OPTION ")

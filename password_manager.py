import random
import os
import json
import string
from cryptography.fernet import Fernet


def save_pass():
    
    if not os.path.exists("key.json"):
        print("the key.json file does not exist")
        return None
        
    else:
        with open("key.json", "r") as file:
            key_file = json.load(file)

            load_key = key_file["key_2025-06-03"].encode()
            return load_key



def check_exits():

    try:
        if not os.path.exists("passwords.json"):
            with open("passwords.json", "x") as f:
                json.dump({}, f,)
        else:
            pass
    except (FileExistsError, Exception) as e:
        print(e)



def insert_input(userinput, load_key):

    Cipher = Fernet(load_key)

    length = random.randint(15, 20)

    make_pass = "".join(random.sample(string.ascii_letters + string.digits, k = length))
    print(f"generated password for {userinput} is: {make_pass}")
    
    password_encoded = make_pass.encode()
    encrypted_pass = Cipher.encrypt(password_encoded)
    saved_pass = encrypted_pass.decode()

    try:
        with open("passwords.json", "r") as file:

            file_data = json.load(file)

            if userinput not in file_data:

                file_data[userinput] = saved_pass

                with open("passwords.json", "w") as file:

                    json.dump(file_data, file, indent=4)

                    print(f"{userinput} was saved to passwords.json")

            else:

                print("The is already saved")

    except (FileNotFoundError, Exception) as f:
        print(f)


def get_and_decrypt(load_key, get_input):
    Cipher = Fernet(load_key)
    try:
        with open("passwords.json", "r") as file:
            read_file = json.load(file)
            
            if get_input in read_file:
                input_name = read_file[get_input].encode()
                decrypted_name = Cipher.decrypt(input_name).decode()
                print(f"The password for {get_input} is: {decrypted_name}")
            else:
                print(f"{get_input} was not found")
    except (FileNotFoundError, Exception) as e:
        print(e)



def main():
   
    load_key = save_pass()
    check_exits()

    ask_user = input("what would you like: ").strip()

    if ask_user == "add":
        if load_key:
            userinput = input("what is the password for ? ")
            insert_input(userinput, load_key)
        else:
            pass
    elif ask_user == "get":
        if load_key:
            get_input = input("what would you like to retrive ? ")
            get_and_decrypt(load_key, get_input)
        else:
            pass
    else:
        print("This input is not avaliabe")    
    


if __name__ == "__main__":
    main()

    


import os
import json
import datetime 
from cryptography.fernet import Fernet



key = Fernet.generate_key().decode() 


if not os.path.exists("key.json"):
    with open("key.json", "x") as file:
        json.dump({}, file)
else:
    pass

now = datetime.datetime.now()
formatting = now.strftime("%Y-%m-%d") 
name = f"key_{formatting}"

try:
    with open("key.json", "r") as file:
        file_data = json.load(file) 
        file_data[name] = key

        get_user = input("Would you like this password saved to a file: ").strip()
        if get_user == "yes":
            with open(f"{name}.txt", "w") as file:
                file.write(key)
                print(f"File was saved to {name}.txt")
        else:
            pass

        with open("key.json", "w") as file:
            json.dump(file_data, file, indent=4) 
except (FileNotFoundError, Exception) as e:
    print(e)

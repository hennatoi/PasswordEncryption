from cryptography.fernet import Fernet

'''
This function must be run only once. It creates the key.key- file and generates the key.

def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as keyfile:
        keyfile.write(key)
'''

def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key

key = load_key()
fer = Fernet(key)

def view():
    with open ("passwords.txt", "r") as file:
        for line in file.readlines():
            info = line.rstrip()
            user, passw = info.split("|")
            print("User:", user, "| Password:", fer.decrypt(passw.encode()).decode())

def add():
    name = input("Username: ")
    pwd = input("password: ")

    with open ("passwords.txt", "a") as file:
        file.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")

while True:
    choice = input("1: View passwords, 2: Add new password, 3: Quit\n")
    if choice == "3":
        break
    if choice == "1":
        view()
    elif choice == "2":
        add()
    else:
        print("invalid choice")
        continue
    
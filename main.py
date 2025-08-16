import random
import os
import string

def generate_license_key():
    chars = string.ascii_letters + string.digits
    parts = [
        ''.join(random.choices(chars, k=4)),
        ''.join(random.choices(chars, k=4)),
        ''.join(random.choices(chars, k=4)),
        ''.join(random.choices(chars, k=4)),
    ]
    return f"{parts[0]}-{parts[1]}-{parts[2]}-{parts[3]}"

def read_licenses():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    license_path = os.path.join(script_dir, "licenses.txt")
    with open(license_path, "r") as file:
        read_license = file.read()
        print(read_license)

def append_license(generated_license):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    license_path = os.path.join(script_dir, "licenses.txt")
    with open(license_path, "a") as file:
        file.write(f"{generated_license}\n")

def register_account():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    account_path = os.path.join(script_dir, "accounts.txt")
    username = input("Enter a username: ")
    password = input("Enter a password: ")
    with open(account_path, "a") as file:
        file.write(f"{username}:{password}\n")
    print("Account registered successfully!")

def login_account():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    account_path = os.path.join(script_dir, "accounts.txt")
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    found = False
    if os.path.exists(account_path):
        with open(account_path, "r") as file:
            for line in file:
                stored_user, stored_pass = line.strip().split(":", 1)
                if stored_user == username and stored_pass == password:
                    found = True
                    break
    if found:
        print("Login successful!")
        return True
    else:
        print("Login failed. Invalid username or password.")
        return False

def main_menu():
    while True:
        print("\nAvailable actions: \n1. Generate license \n2. Read license file\n3. Exit")
        action = input("Please enter your action: ")
        if action == "1":
            print("Generating license...")
            generated_license = generate_license_key()
            append_license(generated_license)
            print(f"Generated license: {generated_license}")
        elif action == "2":
            read_licenses()
        elif action == "3":
            print("Exiting...")
            exit()
        else:
            print("Invalid action.")

def start():
    logged_in = False
    while not logged_in:
        print("\nAvailable actions: \n1. Register account\n2. Login\n3. Exit")
        action = input("Please enter your action: ")
        if action == "1":
            register_account()
        elif action == "2":
            logged_in = login_account()
        elif action == "3":
            print("Exiting...")
            exit()
        else:
            print("Invalid action.")
    main_menu()

if __name__ == "__main__":
    start()
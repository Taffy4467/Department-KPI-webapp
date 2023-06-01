import subprocess
from login import register_user, login_user
from home import run_app

def main():
    # Prompt user to register or login
    print("Welcome to the Departmental KPI Web app📊")
    choice = input("Enter '1' to register or '2' to login: ")

    if choice == '1':
        # Register user
        username = input("Enter username: ")
        password = input("Enter password: ")
        if register_user(username, password):
            print("User registered successfully.")
        else:
            print("Failed to register user.")
    elif choice == '2':
        # Login user
        username = input("Enter username: ")
        password = input("Enter password: ")
        if login_user(username, password):
            print("User logged in successfully.")
            run_app()
        else:
            print("Login failed.")
    else:
        print("Invalid choice. Exiting...")

if __name__ == '__main__':
    main()

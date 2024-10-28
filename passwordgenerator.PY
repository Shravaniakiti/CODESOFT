import random
import string

def generate_password(length):
    if length < 1:
        return "Password length must be at least 1."

    # Define character sets
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation

    # Combine all characters
    all_characters = lowercase + uppercase + digits + special_characters

    # Generate password
    password = ''.join(random.choice(all_characters) for _ in range(length))
    return password

def main():
    print("WELCOME TO THE SPECIAL PASSWORD GENERATOR!")
    while True:
        try:
            length = int(input("ENTER THE DESIRED LENGTH OF THE PASSWORD (or '0' to exit): "))
            if length == 0:
                print("EXITING THE PASSWORD GENERATOR.")
                break
            if length < 1:
                print("PLEASE ENTER A LENGTH OF GREATER THAN 0.")
                continue

            password = generate_password(length)
            print(f"Generated Password: {password}")

        except ValueError:
            print("INVALID INPUT.PLEASE ENTER A NUMERIC VALUE.")

if __name__ == "__main__":
    main()

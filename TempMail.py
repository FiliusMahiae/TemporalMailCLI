import requests
import random
import string

# Generates a random username
def generate_random_username(length=8):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))

# Generates a random password
def generate_random_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

# Fetches a domain from the mail.tm API
def get_domain():
    try:
        response = requests.get('https://api.mail.tm/domains', timeout=5)
        response.raise_for_status()
        return response.json()['hydra:member'][0]['domain']
    except requests.RequestException as e:
        print("Error fetching domain:", e)
        return None

# Creates an account with the generated email and password
def create_account(email, password):
    data = {
        "address": email,
        "password": password
    }
    response = requests.post('https://api.mail.tm/accounts', json=data)
    return response

# Prints the ASCII art logo and menu
def printMenu():
    print(" _____                   ___  ___      _ _ ")
    print("|_   _|                  |  \\/  |     (_) |")
    print("  | | ___ _ __ ___  _ __ | .  . | __ _ _| |")
    print("  | |/ _ \\ '_ ` _ \\| '_ \\| |\\/| |/ _` | | |")
    print("  | |  __/ | | | | | |_) | |  | | (_| | | |")
    print("  \\_/\\___|_| |_| |_| .__/\\_|  |_/\\__,_|_|_|")
    print("                   | |                     ")
    print("                   |_|                     ")

# Main function
def main():
    printMenu()  # Display the menu
    
    # Generate the email address and password
    domain = get_domain()  # Fetches a valid domain from mail.tm
    username = generate_random_username()  # Generates a random username
    email = f"{username}@{domain}"  # Creates the email address
    password = generate_random_password()  # Generates a secure random password

    # Create the account using the generated credentials
    response = create_account(email, password)

    # Check if the account was created successfully
    if response.status_code == 201:
        print("Account created successfully!")
        print(f"Email: {email}")
        print(f"Password: {password}")
    else:
        print("Error creating the account.")
        print(f"Status code: {response.status_code}")
        print(f"Response: {response.json()}")

# Run the main function if the script is executed directly
if __name__ == "__main__":
    main()




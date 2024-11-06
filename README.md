# TemporalMailCLI

**TemporalMailCLI** is a command-line tool to generate and manage temporary email accounts directly from the Linux terminal. This project allows you to quickly create an email address and password for short-term usage, ideal for receiving verification links, temporary notifications, and protecting your main inbox from spam.

## Features

- **Random Username & Password Generation**: Securely generate random usernames and passwords with customizable length.
- **Fetch Available Domain**: Automatically fetches an available email domain from the `mail.tm` API.
- **Email Creation**: Instantly creates an email account with just one command.
- **CLI-Based Interface**: Simple and efficient, all within the terminal.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/FiliusMahiae/TemporalMailCLI.git
   ```
2. Navigate to the project directory:
   ```bash
   cd TemporalMailCLI
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the script to generate a temporary email account:

```bash
python TempMail.py
```

The program will:
1. Generate a random username and password.
2. Fetch a valid domain from the `mail.tm` API.
3. Create the account and display the generated email and password if successful.

## Example Output

```plaintext
 _____                   ___  ___      _ _ 
|_   _|                  |  \/  |     (_) |
  | | ___ _ __ ___  _ __ | .  . | __ _ _| |
  | |/ _ \ '_ ` _ \| '_ \| |\/| |/ _` | | |
  | |  __/ | | | | | |_) | |  | | (_| | | |
  \_/\___|_| |_| |_| .__/\_|  |_/\__,_|_|_|
                   | |                     
                   |_|                     

Account created successfully!
Email: randomname@mail.tm
Password: securepassword123!
```

## Author

This project was created and is maintained by **Sergio Mahía**.

## License

This project is licensed under the MIT License - see the LICENSE file for details.



def welcome():
    ''' Prints the welcome message and returns nothing.'''
    print("Welcome to the Caesar Cipher\nThis program encrypts and decrypts text with the Caesar Cipher.")

def enter_message():
    '''asks user to enter which mode to imply,checks if the mode is valid, asks the user the messge to perform
      text conversion operation on and then returns two strings values. '''
    while True:
        mode_of_opr = input("Would you like to encrypt (e) or decrypt (d)? ").lower()
        if mode_of_opr in ['e', 'd']:
            break
        else:
            print("Invalid Mode")

    message = input(f"What message would you like to {"encrypt" if mode_of_opr == 'e' else "decrypt"}:")
    
    while True:
        try:
            shift_number = int(input("What is the shift number: "))
            break
        except ValueError:
            print("Invalid Shift")

    return mode_of_opr, message.upper(), shift_number
    #as per the requirement two string values mode and message in upper case to avoid encrypting or decrypting issues are used.

def encrypt(message, shift):
    '''Takes two parameters message and shift key and returns encrypted message'''
    encrypted_message = " "
    for char in message:
        if char.isalpha():
            encrypted_message += chr((ord(char) - ord('A') + shift) % 26 + ord('A')) # to encrypt ascii values are added with respect to that of A
        else:
            encrypted_message += char
    return encrypted_message

def decrypt(message, shift):
    '''Takes two parameters message and shift key and returns encrypted message'''
    decrypted_message = " "
    for char in message:
        if char.isalpha():
            decrypted_message += chr((ord(char) - ord('A') - shift) % 26 + ord('A'))# to decrypt ascii values are subtracted with respect to that of A
        else:
            decrypted_message += char
    return decrypted_message


# Input Output section
def process_file(filename, mode):
    '''has two  parameters filename and mode'''
    messages = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                messages.append(line.strip()) #strip is used to give clean texts.
    except FileNotFoundError:
        print("File not found.")
    return [encrypt(msg,mode) if mode == 'e' else decrypt(msg,mode)  for msg in messages]


def is_file(filename):
    '''take filename as single parameter and return boolean value'''
    try:
        with open(filename, 'r'):
            pass     # not to leave the code blank
        return True
    except FileNotFoundError:
        return False

def write_messages(messages):
    '''takes message as single parameter, a list of strings and and returns nothing.'''
    with open('results.txt', 'w') as file:
        for msg in messages:
            file.write(msg + '\n')

def message_or_file():
    '''takes no parameter but returns three values mode,message and filename.'''
    while True:
        mode = input("Would you like to encrypt (e) or decrypt (d): ").lower()
        if mode in ['e', 'd']:
            break
        else:
            print("Invalid Mode")

    while True:
        option = input("Would you like to read from a file (f) or the console (c)? ").lower()
        if option == 'f':
            filename = input("Enter a filename: ")
            if is_file(filename):
                break
            else:
                print("Invalid Filename")
        elif option == 'c':
            filename = None 
            break
        else:
            print("Invalid option")

    if filename:
        while True:
            try:
                shift_number = int(input("What is the shift number: "))
                break
            except ValueError:
                print("Invalid Shift")

        return mode, None, filename, shift_number
    else:
        return mode, input(f"What message would you like to {"encrypt" if mode == 'e' else "decrypt"}: "), None


def main():

    welcome()
    while True:
        mode = input("Would you like to encrypt (e) or decrypt (d)? ").lower()
        if mode not in ['e', 'd']:
            print("Invalid Mode")
            continue

        option = input("Would you like to read from a file (f) or the console (c)? ").lower()
        if option == 'f':
            filename = input("Enter a filename: ")
            if is_file(filename):
                while True:
                    try:
                        shift_number = int(input("What is the shift number: "))
                        break
                    except ValueError:
                        print("Invalid Shift")

                results = encrypt(filename, shift_number) if mode == 'e' else decrypt(filename, shift_number)
                for result in results:
                    print(result)
            else:
                print("Invalid Filename")
        elif option == 'c':
            message = input(f"What message would you like to {'encrypt' if mode == 'e' else 'decrypt'}: ")
            while True:
                try:
                    shift_number = int(input("What is the shift number: "))
                    break
                except ValueError:
                    print("Invalid Shift")

            result = encrypt(message.upper(), shift_number) if mode == 'e' else decrypt(message.upper(), shift_number)
            print(result)

        another_operation = input("Would you like to encrypt or decrypt another message? (y/n): ").lower()
        if another_operation != 'y':
            print("Thanks for using the program, goodbye!")
            break

main()


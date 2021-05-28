import random
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def main():
    #This program takes your text input to encode or decode, using Ceasar cipher.
    #Ceasar cipher method rotates the the letters of the alphabet to encode using a key as an indicator.
    #For example, key 4 means letter A will be replaced with a letter 4 steps away from it, which is D; B with E, and so on.
    #This program is for writing your diary or exchanging encoded letters with friends :D
    #Limitation: this program does not encode numbers and special characters.

    code_on = True
    while code_on:
        print("Welcome to code factory!")
        your_text = text_input()
        encode = choose_mode()
        if encode:
            print("You are now in encode mode.")
            your_key = pick_key()
            your_new_text = code(your_text, your_key)
            print(f"Here is your encoded message:\n{your_new_text}")
        else:
            print("You are in decode mode.")
            your_key = input_key()
            your_new_text = code(your_text, your_key*(-1))
            print(f"Here is your encoded message:\n{your_new_text}")
        
        code_on = user_proceed()


def input_key():
    while True:
        chosen_key = int(input("Please pick a number from 1 to 26: "))
        if chosen_key not in range(1,27):
            print("Please input an integer from 1 to 26 only.")
        else:
            print(f"It's confirmed that your key is {chosen_key}")
            break
    return chosen_key

def pick_key():
    print("You can pick your key, or it will be picked randomly.")
    while True:
        user_key = input("Do you want to pick your key? Answer Yes or No: ")
        if user_key[0].lower() not in ["y", "n"]:
            print("I don't understand. Please only answer Yes or No.")
        else:
            break
            
    if user_key[0].lower() == "y":
        chosen_key = input_key()
    
    if user_key[0].lower() == "n":
        chosen_key = random.randrange(27)
        print(f"Your key is {chosen_key}")
        
    print("You need to remember the key to decode your text later.")
    return chosen_key

def text_input():
    user_text = input("Please type your message here:\n")
    return user_text

def choose_mode():
    #This function helps the user choose between encode and decode mode
    while True:
        mode = input("Do you want to encode or decode? Answer E for encode, D for decode: ")
        if mode[0].lower() not in ["e", "d"]:
            print("Please answer D or E only.")
        else:
            break
    
    if mode[0].lower() == "e":
        return True
    else:
        return False

def code(text, chosen_key):
    new_text = ""
    for i in text:
        letter_state = i.isupper()
        if i.upper() in ALPHABET:
            letter_position = ALPHABET.find(i.upper())
            if letter_state == True:
                i = ALPHABET[letter_position + chosen_key]
            else:
                i = ALPHABET[letter_position + chosen_key].lower()
        new_text += i
    return new_text

def user_proceed():
    #Ask user if they want to continue decode or encode
    while True:
        proceed_choice = input("Do you want to continue? Answer Yes or No: ")
        if proceed_choice[0].lower() not in ["y", "n"]:
            print("I don't understand. Please only answer Yes or No.")
        else:
            break
    if proceed_choice[0].lower() == "y":
        return True
    else:
        return False


if __name__ == '__main__':
    main()
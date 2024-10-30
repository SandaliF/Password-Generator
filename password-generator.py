import random
import string

def generate_pwd(min_length,number=True,special_character=True):
    letter=string.ascii_letters
    digit=string.digits
    special=string.punctuation

    characters=letter
    if number:
        characters+=digit
    if special_character:
        characters+=special

    pwd=""
    meets_criteria=False
    has_number=False
    has_special=False

    while not meets_criteria or min_length>len(pwd):
        new_char=random.choice(characters)
        pwd+=new_char

        if new_char in digit:
            has_number==True
        if new_char in special:
            has_special==True

        meets_criteria=True

        if number:
            meets_criteria==has_number
        if special_character:
            meets_criteria==meets_criteria and has_special

    return pwd


min_length=int(input("Enter the minimum lenght: "))
number=input("Do you want to have numbers (y/n)?").lower()=="y"
special=input("Do you want to have special characters (y/n)?").lower()=="y"

pwd = generate_pwd(min_length,number,special)

print (f"Password: {pwd}")

import random 
import string


def generate_password(length, use_uppercase, use_lowercase, use_digits, use_special):
    character_pool = ''
    
    if use_uppercase:
        character_pool+= string.ascii_uppercase
    if use_lowercase:
        character_pool+= string.ascii_lowercase
    if use_digits:
        character_pool+= string.digits
    if use_special:
        character_pool+= string.punctuation
    

    if not character_pool:
        raise ValueError("At least seclected one character")
    
    password = ''.join(random.choice(character_pool) for _ in range(length))
    return password



def main():
    print("welcome to the password Generator!")

    #get user input for password length
    length = int(input("Enter the desired password length:"))


    use_uppercase = input("Include uppercase letters ? (y/n): ").lower() == 'y'
    use_lowercase = input("Include lowercase letters ? (y/n): ").lower() == 'y'
    use_digits = input("Include digits ? (y/n): ").lower() == 'y'
    use_special = input("Include special characters ? (y/n): ").lower() == 'y'


    try:
        password = generate_password(length, use_uppercase, use_lowercase, use_digits, use_special)
        print(f"Generate password : {password}")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()

import string
MIN_LENGTH = 8
SPECIAL_CHARACTERS = string.punctuation

def check_password_strength(password):
    score=0
    feedback =[]
    if len(password) >= MIN_LENGTH:
       score += 1
    else:
        feedback.append("Password should be atleast 8 character long")
    if any(char.islower() for char in password):
        score += 1
    else:
        feedback.append("Include atleast one lowercase letter.")
    if any(char.isupper() for char in password):
        score += 1
    else:
        feedback.append("Include atleast one upperrcase letter.")
    if any(char.isdigit() for char in password):
        score += 1
    else:
        feedback.append("Include atleast one number")
    if any(char in SPECIAL_CHARACTERS for char in password):
        score += 1
    else:
        feedback.append("Include at least one special character")
    return score, feedback

def main():
    password = input("Enter your password: ")
    score, feedback = check_password_strength(password)
    
    print("\nPassword Analysis Result: ")
    if score == 5:
        print("Strong Password!")
    elif 3 <= score < 5:
        print("Moderate Password!")
    else:
        print("Weak Password!")

    for tip in feedback:
        print("-" + tip)

if __name__ == "__main__":
    main()
   


    
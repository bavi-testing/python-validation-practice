
while True :
    user = input("Enter your username :").strip()

    if user == "" :
        print("Fields cannot be empty")

    elif " " in user :
        print("Username must not contain spaces")

    elif user.lower() != "admin" :
        print("Invalid user name")

    else:
        print("Valid username")
        break

while True:
    email = input("Enter your email:").strip()

    if email == "" :
        print("Fields cannot be empty")

    elif " " in email :
        print("Email must not contain spaces")

    elif "@" not in email :
        print("Email must contain the character '@'")

    elif "." not in email :
        print("Email must contain the character '.'")

    else:
        print("Valid email")
        break

while True :
    password = input("Enter the password :")

    if password == "" :
        print("Fields cannot be empty")

    elif " " in password :
        print("Password must not contain spaces")

    elif len(password)<=7 :
        print("password must contain 8 letters")

    else:
    
        has_number = False
        for num in password :
            
            if num.isdigit() == True:
                has_number = True
                break

        if has_number == False:
            print("password must contain numbers")

        else:
            print("Valid password")
            break
                

         

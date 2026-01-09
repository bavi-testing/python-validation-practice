password = input("Enter your password :")

if password == "" :
    print("Fields cannot be empty")

elif " " in password :
    print("Password not contain spaces")


elif len(password) <= 7 :
    print("Password must contain atleast 8 characters")


else : 
    has_number = False
    for num in password:
        if num.isdigit() :
            has_number = True
            break

    if has_number == False:
        print("Password must contain a number")

    else:
        print("Valid password")




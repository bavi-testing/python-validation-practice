
mail = input("Enter your email:").strip()
    
if mail == "" :
    print("Fields cannot be empty")

elif " " in mail:
    print("Email should not contain spaces")

elif "@" not in mail :
    print("Email must contain '@'")

elif "." not in mail :
    print("Email must contain '.' ")

else :
    print("Valid email")

    












user = input("Enter the username :").strip()
password = input("Enter the password :").strip()

if user == "" or password == "" :
    print("Field cannot be empty")

elif  user.lower() != "admin":
    print("Invalid username")

elif password != "123" :
    print("Invalid password")

else:
    print("Login successful")
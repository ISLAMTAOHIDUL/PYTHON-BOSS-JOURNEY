username = input("Enter your username: ")
password = int(input("Enter your password: "))

if username == "admin" and password == 12345:
    print("You are loggeed in successfully.")
else:
    print("Youre username or password is incorrect. Please try again.")
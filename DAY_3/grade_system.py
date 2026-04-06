number = int(input("Enter your exam score: "))

if number >= 80:
    print("You have got an A+ grade.")
elif number >= 70:
    print("You have got an A grade")
elif number >= 65:
    print("You have got a B+ grade.")
elif number >= 60:
    print("You have got a B grade.")
elif number >= 55:
    print("You have got a C grade")
elif number >= 40:
    print("You have got a D grade.")
else:
    print("You have got an F grade.")
#Mobile login attemps system
attempts=0
while attempts<3:
    password=input("Enter your password:")
    if password=="1234":
        print("Login successful!")
        break
    else:
        attempts+=1
        print("Incorrect password. Try again.")
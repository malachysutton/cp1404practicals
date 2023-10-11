minimum_length = 5
password_guess = input("What's the password? ")

while len(password_guess) < minimum_length:
    print("Password is too short try again")
    password_guess = input("What's the password? ")
print("*" * len(password_guess))


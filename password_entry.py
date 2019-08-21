MIN_LENGTH = 5
is_valid = False

password = input("Please enter a password: ")

while not is_valid:
    if len(password) > MIN_LENGTH:
        is_valid = True
    else:
        print("Password is not valid")
        password = input("Please enter a password: ")

for i in range(0, len(password)):
    print('*', end=' ')


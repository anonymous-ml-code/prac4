def numbers():
    # Initialize an empty list to store numbers
    numbers = []

    # Prompt the user for 5 numbers and append them to the list
    for i in range(5):
        number = float(input(f"Number: "))
        numbers.append(number)

    # Output the required information
    print(f"The first number is {numbers[0]}")
    print(f"The last number is {numbers[-1]}")
    print(f"The smallest number is {min(numbers)}")
    print(f"The largest number is {max(numbers)}")
    print(f"The average of the numbers is {sum(numbers) / len(numbers)}")


def authorized():
    # List of authorized usernames
    usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface',
                 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface',
                 'StartServer', 'bob']

    # Ask the user for their username
    username = input("Enter your username: ")

    # Check if the username is in the list of authorized usernames
    if username in usernames:
        print("Access granted")
    else:
        print("Access denied")


# Basic list operations
numbers()
# Woefully inadequate security checker
authorized()

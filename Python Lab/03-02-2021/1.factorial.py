num = int(input("Enter a number: "))
factorial = 1
if num < 0:
    print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
    print("The factorial of 0 is 1")
else:
    for i in range(1, num + 1):
        factorial = factorial * i
    print("The factorial of", num, "is", factorial)

    # OUTPUT
    #
    # Enter a number: 2
    # The factorial of 2 is 2
    #
    # Enter a number: 5
    # The factorial of 5 is 120

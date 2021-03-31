number1=float(input("Enter first value: "))
number2=float(input("Enter second value: "))
number3=float(input("Enter third value: "))

if (number1>number2) and (number1>number3):
    largest=number1
elif (number2>number1) and (number2>number3):
    largest=number2
else:
    largest=number3

print("Largest number is is ",largest);
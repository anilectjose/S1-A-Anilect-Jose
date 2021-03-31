lines = int(input("Enter a number: "))
i = 1
j = 1
while i <= lines:
    j = 1
    while j <= i:
        temp = i * j
        print(temp, end='', flush=True)
        print(" ", end='', flush=True)
        j = j + 1;
    print("");
    i = i + 1;

# Enter a number: 5
# 1
# 2 4
# 3 6 9
# 4 8 12 16
# 5 10 15 20 25

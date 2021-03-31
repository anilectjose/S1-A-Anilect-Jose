def print_factors(x):
    print("The factors of", x, "are:")
    for i in range(1, x + 1):
        if x % i == 0:
            print(i)


print_factors(354)

# The factors of 354 are:
# 1
# 2
# 3
# 6
# 59
# 118
# 177
# 354

def call():
    for x in range(1000, 10000):
        num = str(x)
        number = int(x)
        first = int(num[0])
        second = int(num[1])
        third = int(num[2])
        fourth = int(num[3])
        if first % 2 == 0:
            if second % 2 == 0:
                if third % 2 == 0:
                    if fourth % 2 == 0:
                        for i in range(2, number):
                            if i * i == number:
                                print(number)


call()

# 4624
# 6084
# 6400
# 8464

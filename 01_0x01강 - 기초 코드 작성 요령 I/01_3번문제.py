def square(x):
    for i in range(x):
        if (i*i > x):
            break
        elif (i*i == x):
            return 1
    return 0

square(9)
square(693953651)
square(756580036)
from math import sqrt


n = int(input("Enter n: "))

is_numbers = False
sq = sqrt(n)
for y in range(1, int(sqrt(n)) + 1):
    # n = x^2 + y^2
    # x^2 = sqrt(n)^2 - y^2 = (sq + y) * (sq - y)
    x = sqrt((sq + y) * (sq - y))

    if int(x) == x:
        if int(x) >= y:
            print(int(x), y)
            is_numbers = True
            break

    elif abs(round(x) - x) < 0.0000000001: # prevention of calculation errors
        if round(x) >= y:
            print(round(x), y)
            is_numbers = True
            break

if not is_numbers:
    print("This number cannot be represented as the sum of two squares")

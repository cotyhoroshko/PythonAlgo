from math import log


m = int(input("Enter m: "))
k = log(m, 4)

print("k =", int(k) if k != int(k) or k == 0 else int(k) - 1)


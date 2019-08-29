def F(n):
    if n == 1:
        return 1
    else:
        return n * F(n - 1)
n = int(input("Введіть число:"))
print(F(n))
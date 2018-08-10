def hano(n, a, b, c):
    if n == 1:
        print(a, '-->', c)
        return None
    hano(n-1, a, c, b)
    print(a, '-->', c)
    hano(n-1, b, a, c)

a = "A"
b = "B"
c = "C"

n = 2
hano(n, a, b, c)

s = {1, 2, 4, 5, "d", "f", "g"}
for i in s:
    print(i, end=" ")

g = {(1, 3, 2), ("gg", "cc", "dd"), (3, 4, 1)}
for k,m,n in g:
    print(k, "---", m, "---", n)

for k in g:
    print(k)
a = int(input())
c, d = 0, 1
for _ in range(a):
    print(c, end=' ')
    rw = c + d
    c = d
    d = rw
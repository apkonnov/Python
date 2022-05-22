# Торговля акциями

a = input().split()
n = int(a[0])
x = int(a[1])
a = [int(s) for s in input().split()]
b = [int(s) for s in input().split()]
ibest = 0
jbest = 0
imin = 0
for j in range(1, n):
    if x // a[imin] * b[j] > x // a[ibest] * b[jbest]:
        jbest = j
        ibest = imin
    if a[j] < a[imin]:
        imin = j
if (x // a[ibest] * b[jbest] + x % a[ibest]) > x:
    print(x // a[ibest] * b[jbest] + x % a[ibest])
    print(ibest + 1, jbest + 1)
else:
    print(x)
    print(-1, -1)

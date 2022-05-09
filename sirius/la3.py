# Клиппи и Мерлин грабят банк

n = int(input())
a = [int(s) for s in input().split()]
ibest = 0
jbest = 1
imin = 0
for j in range(2, n):
    if a[j - 1] < a[imin]:
        imin = j - 1
    if a[j] / a[imin] > a[jbest] / a[ibest]:
        jbest = j
        ibest = imin
if a[jbest] / a[ibest] > 1:
    print(ibest + 1, jbest + 1)
else:
    print(0, 0)

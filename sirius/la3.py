# Клиппи и Мерлин грабят банк

a = input().split()
n = int(a[0])
k = int(a[1]) + 1
a = [int(s) for s in input().split()]
ibest = 0
jbest = k
imax = 0
for j in range(k, n):
    if a[j - k] > a[imax]:
        imax = j - k
    if a[j] + a[imax] > a[jbest] + a[ibest]:
        jbest = j
        ibest = imax
print(ibest + 1, jbest + 1)

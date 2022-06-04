# Сумма подряд идущих
n, k, m = map(int, input().split())
a = list(map(int, input().split()))
p = [0] * (n + 1)
for i in range(1, n + 1):
    p[i] = p[i - 1] + a[i - 1]
res = 0
for i in range(n - k):
    if p[i + k + 1] - p[i] == m:
        res = i + 1
        break
print(res)

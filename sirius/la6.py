# Сумма подряд идущих
n, k, m = map(int, input().split())
a = list(map(int, input().split()))
p = [0] * (n + 1)
for i in range(1, n + 1):
    p[i] = p[i - 1] + a[i - 1]
i = 0
while (i < n - k) and (p[i + k + 1] - p[i] != m):
    i += 1
print(i)

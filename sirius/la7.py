# Новый маршрут для трекинга
n, m = map(int, input().split())
h = list(map(int, input().split()))
p = [0] * (n + 1)
for i in range(2, n + 1):
    p[i] = p[i - 1] + 1 if h[i - 1] > h[i - 2] else p[i - 1]
l = [0] * m
r = [0] * m
for i in range(m):
    l[i], r[i] = map(int, input().split())
for i in range(m):
    if l[i] == r[i]:
        print(0)
    else:
        print(p[r[i]] - p[l[i] - 1])

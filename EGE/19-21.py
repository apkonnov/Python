# одна куча
# функция, которая проверяет, можно ли выиграть за m ходов
def f(s, c, m):
    # если игра окончена, то количество ходов должно иметь ту же четность что и m.
    if s >= 30:
        return c % 2 == m % 2
    # если игра не окончилась за m ходов.
    if c == m:
        return 0
    # смотрим следующие ходы
    h = [f(s + 2, c + 1, m), f(s + 3, c + 1, m), f(s * 2, c + 1, m)]
    # если это ход целевого игрока, то достаточно победы в одном из вариантов
    # иначе победа должна быть во всех вариантах (мы побеждаем при любом ходе противника)
    return any(h) if (c + 1) % 2 == m % 2 else all(h)


for s in range(1, 30):
    for m in range(1, 5):
        if f(s, 0, m) == 1:
            if m == 4:
                print(s, m)
            # если нашлась выигышная стратегия, то не копаем дальше
            break
# логические операции             python
# Отрицание (НЕ)          ¬       not()
# Конъюнкция (И)          ∧       and
# Дизъюнкция (ИЛИ)        ∨       or
# Эквивалентность         ↔ ≡     ==
# Импликация (если…, то…) A ⟶ B   not(A) or B
#                         A ⟶ B   A <= B

# таблица истинности x,y,z
print('x y z   F')
for x in (0, 1):
    for y in (0, 1):
        for z in (0, 1):
            # вместо True записываем логическое выражение из условия на питоне
            # (¬x ∧ y ∧ z) ∨ (¬x ∧ ¬y ∧ z) ∨ (¬x ∧ ¬y ∧ ¬z)
            F = (not x and y and z) or (not x and not y and z) or (not x and not y and not z)
            # if True - вся таблица истинности
            # if F - таблица истинности с F = 1
            # if not(F) - таблица истинности с F = 0
            if F:
                print(x, y, z, ' ', int(F))

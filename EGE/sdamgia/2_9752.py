# таблица истинности x,y,z
print('x y z   F')
for x in (0, 1):
    for y in (0, 1):
        for z in (0, 1):
            # (¬x ∧ y ∧ z) ∨ (¬x ∧ ¬y ∧ z) ∨ (¬x ∧ ¬y ∧ ¬z)
            F = (not x and y and z) or (not x and not y and z) or (not x and not y and not z)
            if F:
                print(x, y, z, ' ', int(F))

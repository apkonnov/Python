# таблица истинности x,y,z
print('x y z   F')
for x in (0, 1):
    for y in (0, 1):
        for z in (0, 1):
            # (x ∨ y) → (z ≡ x)
            F = (x or y) <= (z == x)
            if not F:
                print(x, y, z, ' ', int(F))

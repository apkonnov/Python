# таблица истинности x,y,z,w
print('x y z w   F')
for x in (0, 1):
    for y in (0, 1):
        for z in (0, 1):
            for w in (0, 1):
                # ¬w ∧ z ∧ (y → x)
                F = not w and z and (y <= x)
                if F:
                    print(x, y, z, w, ' ', int(F))

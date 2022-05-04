# таблица истинности x,y,z
print('x y z   F')
for x in (0, 1):
    for y in (0, 1):
        for z in (0, 1):
            F = True
            if F:
                print(x, y, z, ' ', int(F))

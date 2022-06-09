for i in range(28, 33):
    s = bin(i)[2:]
    if i % 2 == 0:
        print(i, s, '00', int(s + '00', 2))
print()
for i in range(27, 32):
    s = bin(i)[2:]
    if i % 2 != 0:
        print(i, s, '11', int(s + '11', 2))

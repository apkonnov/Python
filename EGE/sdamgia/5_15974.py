for i in range(24, 27):
    s = bin(i)[2:]
    if i % 2 == 0:
        s = s + '10'
        print(i, s[:-2], '10', s,  int(s, 2))
print()
for i in range(25, 28):
    s = bin(i)[2:]
    if i % 2 != 0:
        print(i, s, '01', s + '01', int(s + '01', 2))

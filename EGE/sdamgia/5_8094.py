for i in range(0, 27):
    s = bin(i)[2:]
    z = s.count('1') % 2
    s_res = s + str(z)
    z = s_res.count('1') % 2
    s_res = s_res + str(z)
    print(i, s, s_res,  int(s_res, 2))
print()

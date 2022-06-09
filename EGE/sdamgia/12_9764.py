st = '9' * 127
print(st)
while ('333' in st) or ('999' in st):
    if '333' in st:
        st = st.replace('333', '9', 1)
    else:
        st = st.replace('999', '3', 1)
    print(st)
print(st)

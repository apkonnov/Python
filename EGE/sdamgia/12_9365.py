st = '8'*68
print(st)
while st.find('222') > -1 or st.find('888') > -1:
    if st.find('222') > -1:
        st = st.replace('222', '8', 1)
    else:
        st = st.replace('888', '2', 1)
    print(st)
print(st)

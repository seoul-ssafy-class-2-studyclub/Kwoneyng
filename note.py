pw = [(0, '0001101'), (1, '0011001'), (2, '0010011'), (3, '0111101'), (4, '0100011'), (5, '0110001'), (6, '0101111'), (7, '0111011'), (8, '0110111'), (9, '0001011')]
val = [pw[i][1] for i in range(10)]
if '0001101' in val:
    print('있네?')
else :
    print('있지않아?')

# 0001011 0001101 0110001 0011001 0010011 0001101 0001011 0100011 000000
for T in range(int(input())):
    N, M = list(map(int, input().split()))
    rs = set()
    for i in range(N):
        su_set = []
        st = list(map(int, input()))
        for j in range(10000):
            if sum(st[:4]) == 0:
                if len(st) > 0:
                    st.pop(0)
            elif ''.join(map(str, st[:7])) in val and ''.join(map(str, st[7:14])) in val:
                for z in range(2):
                    for i in pw:
                        print(''.join(map(str, st[:7])))
                        if ''.join(map(str, st[:7])) in i:
                            su_set.append(i[0])
                            print(su_set)
                            print(st)
                            del st[:7]
            else :
                if len(st) > 0:
                    st.pop(0)
                else :
                    break
        if len(su_set) > 7 :
            print((su_set[0] + su_set[2] + su_set[4] + su_set[6])*3 + su_set[1] + su_set[3] + su_set[5] + su_set[7])
            if ((su_set[0] + su_set[2] + su_set[4] + su_set[6])*3 + su_set[1] + su_set[3] + su_set[5] + su_set[7]) % 10 == 0:
                rs.update([sum(su_set)])
            else :
                rs.update([0])
        print(rs)
    print('#{0} {1}'.format(T+1, rs.pop()))    

for T in range(10):
    bd = []
    t_no = int(input())
    count = 0
    for i in range(t_no):
        bd.append(list(map(int, input().split())))
    bd_ro = list(map(list, zip(*bd)))
    for x in range(len(bd_ro)):
        for y in range(len(bd_ro)):
            if len(bd_ro[x]) == 0 :
                break
            else :
                if bd_ro[x][0] == 1:
                    if 2 in bd_ro[x]:
                        pair = bd_ro[x].index(2)
                        del bd_ro[x][0:pair+1]
                        count += 1
                    else :
                        break
                else : 
                    del bd_ro[x][0]
    print(f'#{T+1} {count}')                                
    
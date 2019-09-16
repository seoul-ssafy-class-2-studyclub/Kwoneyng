def asc_set(h):
    asc = ord(h)
    if asc >= A:
        asc = asc - A + 10
    else:
        asc = asc - zero
    return asc


def chk_bar():
    global c
    pw = []
    mag = 0
    bi_no = asc_set(ls[r][c])
    chk = 0
    for i in range(8):
        ratio = [0, 0, 0]
        while not(bi_no & 1):
            chk += 1
            bi_no >>= 1
            if chk == 4:
                chk = 0
                c -= 1
                bi_no = asc_set(ls[r][c])
        while bi_no & 1:
            ratio[2] += 1
            chk += 1
            bi_no >>= 1
            if chk == 4:
                chk = 0
                c -= 1
                bi_no = asc_set(ls[r][c])
        while not (bi_no & 1):
            ratio[1] += 1
            chk += 1
            bi_no >>= 1
            if chk == 4:
                chk = 0
                c -= 1
                bi_no = asc_set(ls[r][c])
        while bi_no & 1:
            ratio[0] += 1
            chk += 1
            bi_no >>= 1
            if chk == 4:
                chk = 0
                c -= 1
                bi_no = asc_set(ls[r][c])
        if not mag:
            mag = min(ratio[0], ratio[1], ratio[2])
        if mag > 1:
            ratio = map(lambda x: x // mag, ratio)
        pw.insert(0, decode[tuple(ratio)])
    if chk:
        c -= 1

    code = 0
    for i in range(8):
        if not i % 2:
            code += pw[i] * 3
        else:
            code += pw[i]
    if not code % 10:
        return sum(pw)
    else:
        return 0

decode = {(2, 1, 1): 0, (2, 2, 1): 1, (1, 2, 2): 2, (4, 1, 1): 3, (1, 3, 2): 4,
(2, 3, 1): 5, (1, 1, 4): 6, (3, 1, 2): 7, (2, 1, 3): 8, (1, 1, 2): 9}

zero = ord('0')  # 48
A = ord('A')  # 65
rs_set = []
for case in range(int(input())):
    N, M = map(int, input().split())
    ls = [input() for _ in range(N)]
    rs = 0
    for r in range(N):
        c = M - 1
        while c >= 0:
            if ls[r][c] != '0' and (ls[r-1][c] == '0' or r == 0):
                rs += chk_bar()
            else:
                c -= 1       

    rs_set.append(rs)

for i in range(len(rs_set)):
    print(f'#{i+1} {rs_set[i]}')
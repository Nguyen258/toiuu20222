import random

data = {}
# Small
data["Small/input_8_4_3.txt"] = [8, 4, 3]
data["Small/input_10_4_3.txt"] = [10, 4, 3]
data["Small/input_10_6_3.txt"] = [10, 6, 3]
data["Small/input_12_6_4.txt"] = [12, 6, 4]
# Medium
data["Medium/input_12_8_4.txt"] = [12, 8, 4]
data["Medium/input_14_8_4.txt"] = [14, 8, 4]
data["Medium/input_14_10_5.txt"] = [14, 10, 5]
data["Medium/input_16_10_6.txt"] = [16, 10, 6]
data["Medium/input_16_12_6.txt"] = [16, 12, 6]
# Large
data["Large/input_18_12_6.txt"] = [18, 12, 6]
data["Large/input_18_14_8.txt"] = [18, 14, 8]
data["Large/input_20_14_8.txt"] = [20, 14, 8]
data["Large/input_24_14_10.txt"] = [24, 14, 10]
data["Large/input_24_16_10.txt"] = [24, 16, 10]
# Extra-large 
data["Extra-large/input_26_16_12.txt"] = [26, 16, 12]
data["Extra-large/input_30_18_12.txt"] = [30, 18, 12]
data["Extra-large/input_40_18_12.txt"] = [40, 18, 12]
data["Extra-large/input_40_20_14.txt"] = [40, 20, 14]
data["Extra-large/input_50_24_16.txt"] = [50, 24, 16]

path = "/Users/duongdong/toiuu20222/Dataset/"
for name, NMK in data.items():
    path_input = path + name
    # xoa trang
    with open(path_input, 'w') as file:
        file.truncate(0)
    
    N,M,K = NMK
    # so DA_min ~= (N/K)-1
    a = 1
    b = N - K + 1 
    # so GV ~= (M/K) - 1
    c = 1
    d = M - K + 1
    # dotuongdong
    e = 1
    f = 1
    # t(i): do an i do ai huowng dan
    t = []
    while(len(t) < N):
        gv = random.randint(1,M)
        check = 0
        for i in t:
            if i == gv: check +=1
        if check > N/M + 1:
            continue
        else:
            t.append(gv)
    # s(i)
    s = zeros_matrix = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(i, N):
            if i == j: continue
            dotuongdong = random.randint(1,10)
            s[i][j] = dotuongdong
            s[j][i] = dotuongdong

    # g(i)
    g = []
    while(len(g) < N):
        g_row = []
        while(len(g_row) < M):
            dotuongdong = random.randint(1,10)
            g_row.append(dotuongdong)
        g.append(g_row)

    with open(path_input, 'a') as file:
        # Ghi các lời gọi print vào file
        print("{} {} {}".format(N, M, K), file=file)
        print("{} {} {} {} {} {}".format(a, b, c, d, e, f), file=file)

        line = " ".join(str(element) for element in t)
        file.write(line + "\n")

        for row in s:
            line = " ".join(str(element) for element in row)
            file.write(line + "\n")
        
        for row in g:
            line = " ".join(str(element) for element in row)
            file.write(line + "\n")

    


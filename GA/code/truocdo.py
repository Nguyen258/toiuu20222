
# path_output,N,M,K,t,s,g,a,b,c,d,e,f

# Nhập số nguyên từ bàn phím
num = (input(""))


data = num.split(" ")

N = int(data[0])
M = int(data[1])
K = int(data[2])

num = (input(""))
data = num.split(" ")
a = int(data[0])
b = int(data[1])
c = int(data[2])
d = int(data[3])
e = int(data[4])
f = int(data[5])

s = []
for i in range(N):
    s.append([-1 for k in range(N)])

for i in range(N):
    num = (input(""))
    data = num.split(" ")
    for j in range(N):
        s[i][j] = int(data[j])

g = []
for i in range(N):
    g.append([-1 for k in range(M)])

for i in range(N):
    num = (input(""))
    data = num.split(" ")
    for j in range(M):
        g[i][j] = int(data[j])

num = (input(""))
data = num.split(" ")

t = [0]*N
for i in range(N):
    t[i] = int(data[i])

print(s)
print(g)
print(t)
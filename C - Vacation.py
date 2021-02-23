from sys import stdin, stdout
def gmi(): return map(int, stdin.readline().strip().split())
def gms(): return map(str, stdin.readline().strip().split())
def gari(): return list(map(int, stdin.readline().strip().split()))
def gars(): return list(map(str, stdin.readline().strip().split()))
def gs(): return stdin.readline().strip()
def gls(): return list(stdin.readline())
def gi(): return int(stdin.readline())



n = gi()
prev = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

ar = gari()
for i in range(3):
    for j in range(3):
        if i != j:
            prev[i][j] = ar[i]
n -= 1

if n > 0:
    ar = gari()
    for i in range(3):
        for j in range(3):
            if i != j:
                prev[i][j] += ar[j]
    n -= 1


for t in range(n):
    ar = gari()
    temp = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    for j in range(3):
        m = 0
        for k in range(3):
            m = max(prev[k][j], m)
        for z in range(3):
            if z != j:
                temp[j][z] = m + ar[z]
    prev = temp[:]

ans = 0
for i in prev:
    ans = max(ans, max(i))

print(ans)

from sys import stdin, stdout
def gmi(): return map(int, stdin.readline().strip().split())
def gms(): return map(str, stdin.readline().strip().split())
def gari(): return list(map(int, stdin.readline().strip().split()))
def gars(): return list(map(str, stdin.readline().strip().split()))
def gs(): return stdin.readline().strip()
def gls(): return list(stdin.readline())
def gi(): return int(stdin.readline())

n, k = gmi()
h = gari()

h += [0]*k

ans = [1000000000]*(n+k)
ans[0] = 0
for i in range(n):
    for j in range(1, k+1):
        ans[i+j] = min(ans[i+j], abs(h[i]-h[i+j])+ans[i])

print(ans[n-1])

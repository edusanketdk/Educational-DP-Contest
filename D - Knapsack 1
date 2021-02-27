from sys import stdin, stdout
#stdin = open('tc.txt', 'r')
#stdout = open('ans.txt', 'w')
def gmi(): return map(int, stdin.readline().strip().split())
def gms(): return map(str, stdin.readline().strip().split())
def gari(): return list(map(int, stdin.readline().strip().split()))
def gars(): return list(map(str, stdin.readline().strip().split()))
def gs(): return stdin.readline().strip()
def gls(): return list(stdin.readline())
def gi(): return int(stdin.readline())
def pr(s): return stdout.write(str(s)+'\n')

n, w = gmi()
W, V = [], []
for i in range(n):
    a, b = gmi()
    W.append(a)
    V.append(b)

dp = [0]*(w+1)
for i in range(n):
    v = w
    while v >= W[i]:
        dp[v] = max(dp[v], V[i]+dp[v-W[i]])
        v -= 1
print(dp[-1])

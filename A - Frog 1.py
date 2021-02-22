from sys import stdin, stdout
def gmi(): return map(int, stdin.readline().strip().split())
def gms(): return map(str, stdin.readline().strip().split())
def gari(): return list(map(int, stdin.readline().strip().split()))
def gars(): return list(map(str, stdin.readline().strip().split()))
def gs(): return stdin.readline().strip()
def gls(): return list(stdin.readline())
def gi(): return int(stdin.readline())

n = gi()
h = gari()

ans = [0, abs(h[1]-h[0])]
for i in range(2, n):
    ans.append(min(ans[i-2]+abs(h[i]-h[i-2]), ans[i-1]+abs(h[i]-h[i-1])))
    
print(ans[-1])


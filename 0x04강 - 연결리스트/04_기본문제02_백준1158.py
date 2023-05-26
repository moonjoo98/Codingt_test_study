import sys

n,k=map(int,sys.stdin.readline().split())
n_list=[i for i in range(1,n+1)]
idx=0
ans=[]

for i in range(n):
    idx += (k-1)
    if idx >= len(n_list):
        idx %= len(n_list)
    ans.append(n_list[idx])
    n_list.pop(idx)
    
print("<"+", ".join(map(str,ans))+">")

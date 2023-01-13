import sys
n=int(sys.stdin.readline().strip())
for i in reversed(range(1,n+1)):
    print("*"*i,sep='\n')

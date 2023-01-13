#두 양의 정수가 주어졌을 때, 두 수 사이에 있는 정수를 모두 출력하는 프로그램을 작성하시오.

import sys
a,b = map(int,sys.stdin.readline().split())

max_=max(a,b)
min_=min(a,b)

a_list=[]
for i in range(min_+1,max_):
    a_list.append(i)

a_list.sort()

print(len(a_list))
print(*a_list)
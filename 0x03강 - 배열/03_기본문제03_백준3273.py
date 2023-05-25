# n개의 서로 다른 양의 정수 a1, a2, ..., an으로 이루어진 수열이 있다. ai의 값은 1보다 크거나 같고, 1000000보다 작거나 같은 자연수이다. 
# 자연수 x가 주어졌을 때, ai + aj = x (1 ≤ i < j ≤ n)을 만족하는 (ai, aj)쌍의 수를 구하는 프로그램을 작성하시오.

#solution 1 o(N)풀이 O(1) * O(N)
import sys

n = int(sys.stdin.readline().strip())

arr = list(map(int,sys.stdin.readline().split()))

x= int(sys.stdin.readline().strip())


cnt=0

for i in range(n):
    if (x-arr[i] > 0) & 
    answer_ = x - arr[i]
    if answer_ in arr:
        cnt+=1
    else:
        pass
print(int(cnt/2))

#solution 2 
# import sys
# n = int(sys.stdin.readline().strip())

# arr = list(map(int,sys.stdin.readline().split()))

# x= int(sys.stdin.readline().strip())
# arr.sort() # 정렬 하지 않으면 투 포인터를 정상적으로 사용할 수 없다.

# count=0
# left=0
# right=n-1

# while left!=right:   #좌측 포인트와 우측 포인트가 겹치게 되면 종료
#     if arr[left]+arr[right]==x:
#         count+=1
#         left+=1
#     elif arr[left]+arr[right]>x:
#         right-=1
#     else:
#         left+=1

# print(count)
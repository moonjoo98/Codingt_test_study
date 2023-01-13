# 7개의 자연수가 주어질 때, 이들 중 홀수인 자연수들을 모두 골라 그 합을 구하고, 고른 홀수들 중 최솟값을 찾는 프로그램을 작성하시오.

# 예를 들어, 7개의 자연수 12, 77, 38, 41, 53, 92, 85가 주어지면 이들 중 홀수는 77, 41, 53, 85이므로 그 합은

# 77 + 41 + 53 + 85 = 256 이 되고,

# 41 < 53 < 77 < 85 이므로 홀수들 중 최솟값은 41이 된다.

# solution 1
import sys
a_list=[]
for i in range(7):
    a=int(sys.stdin.readline().strip())
    if a % 2 != 0 : 
        a_list.append(a)
if a_list:
    print(sum(a_list))
    print(min(a_list))
else:
    print(-1)

#solution 2 
min = 100
sum = 0
for _ in range(7):
    num = int(input())
    if num % 2 == 1:
        sum += num
        if num < min:
            min = num
if sum == 0:
    print(-1)
else:
    print(sum)
    print(min)




    
    
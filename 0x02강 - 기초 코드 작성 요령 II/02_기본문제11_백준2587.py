# 어떤 수들이 있을 때, 그 수들을 대표하는 값으로 가장 흔하게 쓰이는 것은 평균이다. 평균은 주어진 모든 수의 합을 수의 개수로 나눈 것이다. 예를 들어 10, 40, 30, 60, 30의 평균은 (10 + 40 + 30 + 60 + 30) / 5 = 170 / 5 = 34가 된다.

# 평균 이외의 또 다른 대표값으로 중앙값이라는 것이 있다. 중앙값은 주어진 수를 크기 순서대로 늘어 놓았을 때 가장 중앙에 놓인 값이다. 예를 들어 10, 40, 30, 60, 30의 경우, 크기 순서대로 늘어 놓으면

# 10 30 30 40 60

# 이 되고 따라서 중앙값은 30이 된다.

# 다섯 개의 자연수가 주어질 때 이들의 평균과 중앙값을 구하는 프로그램을 작성하시오.

#solution 1
import sys
a_list=[]
for i in range(5):
    a = int(sys.stdin.readline().strip())
    if a % 10 ==0:
        a_list.append(a)

average = int(sum(a_list)/len(a_list))
median = sorted(a_list)[2]

print(average)
print(median)

## solution 2
import sys
a_list=[]
for i in range(5):
    a = int(sys.stdin.readline().strip())
    a_list.append(a)

print(int(sum(a_list)/len(a_list)))
print(sorted(a_list)[2])


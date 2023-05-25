# 정보 초등학교에서는 단체로 2박 3일 수학여행을 가기로 했다. 여러 학년이 같은 장소로 수학여행을 가려고 하는데 1학년부터 6학년까지 학생들이 묵을 방을 배정해야 한다. 남학생은 남학생끼리, 여학생은 여학생끼리 방을 배정해야 한다. 또한 한 방에는 같은 학년의 학생들을 배정해야 한다. 물론 한 방에 한 명만 배정하는 것도 가능하다.

# 한 방에 배정할 수 있는 최대 인원 수 K가 주어졌을 때, 조건에 맞게 모든 학생을 배정하기 위해 필요한 방의 최소 개수를 구하는 프로그램을 작성하시오.

# 예를 들어, 수학여행을 가는 학생이 다음과 같고 K = 2일 때 12개의 방이 필요하다. 왜냐하면 3학년 남학생을 배정하기 위해 방 두 개가 필요하고 4학년 여학생에는 방을 배정하지 않아도 되기 때문이다.

#solution 1 
import sys

n, k = map(int, input().split())
st = [[0]*2 for _ in range(6)] #성별2개 6학년

for i in range(n):
    s, g = map(int, input().split())
    st[g-1][s] += 1

ans = 0
for sex in range(2):
    for grade in range(6):
        ans += (st[grade][sex] // k)
        if st[grade][sex] % k > 0:
            ans += 1
print(ans)

# import sys

# n, k = map(int, input().split())
# st = [[0]*2 for _ in range(6)] #성별2개 6학년

# for i in range(n):
#     s, g = map(int, input().split())
#     st[g-1][s] += 1
# print(st)
# ans = 0
# for sex in range(k):
#     for grade in range(6):
#         ans += (st[grade][sex] // k)
#         if st[grade][sex] % k > 0:
#             ans += 1
# print(ans)
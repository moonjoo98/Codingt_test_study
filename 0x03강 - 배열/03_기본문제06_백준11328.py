# C 언어 프로그래밍에서 문자열(string)은 native한 자료형이 아니다. 사실, 문자열은 그저, 문자열의 끝을 표시하기 위한 말단의 NULL이 사용된, 문자들로 이루어진 문자열일 뿐이다. 하지만 프로그래밍 언어에서 문자열을 다루는 것은 매우 중요하기 때문에, C 표준 라이브러리는 문자열을 다루는 데에 매우 유용한 함수들을 제공하고 있다 : 그들 중에는 strcpy, strcmp, strtol, strtok, strlen, strcat 가 있다.

# 하지만, 잘 알려져 있지 않으며, 잘 사용되지도 않는 함수가 하나 있다 : strfry 함수다. strfry 함수는 입력된 문자열을 무작위로 재배열하여 새로운 문자열을 만들어낸다. (역자 주 : 여기에서 입력된 문자열과 새로 재배열된 문자열이 다를 필요는 없다.)

# 두 개의 문자열에 대해, 2번째 문자열이 1번째 문자열에 strfry 함수를 적용하여 얻어질 수 있는지 판단하라. 

import sys
n = int(sys.stdin.readline().strip())
for i in range(n):
    a,b = map(str,sys.stdin.readline().split())
    a = ''.join(sorted(a))
    b = ''.join(sorted(b))
    if len(a) != len(b):
        print('Impossible')
        continue
    
    for j in range(len(a)):
        if a[j] != b[j]:
            flag=False
            break
        else:
            flag=True
    if flag :
        print('Possible')
    else:
        print('Impossible')
        
        
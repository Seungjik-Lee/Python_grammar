## 연산자

print(1+1) #2
print(3-2) #1
print(5*2) #10
print(6/3) #2

print(2**3) #2^3=8
print(5%3) #나머지 구하기 2
print(10%3) #1

print(5//3) #1
print(10//3) #3

print(10>3)
print(4>=7)
print(10<3)
print(5<=5)

print(3==3)
print(4==2)
print(3+4==7)

print(1!=3) # 앞뒤가 같지않다
print(not(1!=3))

print((3>0)and(3<5))
print((3>0)&(3<5))

print((3>0)or(3>5))
print((3>0|(3>5)))

print(5>4>3)
print(5>4>7)

# 수식

print(2+3*4)
print((2+3)*4)

number=2+3*4
print(number)

number=number+2
print(number)

number+=2
print(number)
number*=2
print(number)
number/=2
print(number)
number-=2
print(number)
number%=5
print(number)

#숫자처리 함수

print(abs(-5)) #절대값
print(pow(4,2)) #4^2 , 4*4
print(max(5,12)) #12
print(min(5,12)) #5
print(round(3.14)) #3
print(round(4.99)) #5

from math import*
print(floor(4.99)) # 내림 4
print(ceil(3.14)) # 올림 4
print(sqrt(16)) # 제곱근 4

# 랜덤함수

from random import*

print(random()) #0.0 이상 1.0 미만의 임의의 값 생성
print(random()*10) #0.0 이상 10.0 미만의 임의의 값 생성
print(int(random()*10)) # 0이상 10미만의 임의의 값 생성
print(int(random()*10)+1) #1 이상 10미만의 임의의 값 생성
print(randrange(1, 46)) #1이상 46 미만의 임의의 값 생성
print(randint(1, 45)) #1이상 45이하의 임의의 값 생성

#퀴즈

'''
Quiz. 당신은 최근에 코딩 스터티 모임을 새로 만들었습니다.
월 4회 스터디를 하는데 3번은 온라인으로 하고 1번은 오프라인으로 하기로 했습니다.
아래 조건에 맞는 오프라인 모임 날짜를 정해주는 프로그램을 작성하시오.

조건1 : 랜덤으로 날짜를 뽑아야함
조건2 : 월별 날짜는 다름을 감안하여 최소 일수인 28 이내로 정함
조건3 : 매월 1~3일은 스터디 준비를 해야하므로 제외

(출력문 예제)
오프라인 스터디 모임 날짜는 매월 X 일로 선정되었습니다.
>>>
'''
from random import*
day = randint(4, 28)
print("오프라인 스터디 모임 날짜는 매월 " + str(day) + " 일로 선정되었습니다.")
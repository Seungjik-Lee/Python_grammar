# 숫자 자료형
print(5)
print(-10)
print(3.14)
print(1000)
print(5+3)
print(2*8)
print(3*(3+1))
#문자 자료형
print('풍선')
print("나비")
print("ㅋㅋㅋㅋㅋㅋㅋㅋ")
print("ㅋ"*9)
#boolean 자료형
print(5 > 10)
print(5 < 10)
print(True)
print(False)
print(not True)
print(not False)
print(not (5 > 10))
#변수
animal = "강아지"
name = "연탄이"
age = 4
hobby = "산책"
is_adult = age >= 3

print("우리집 " + animal + "의 이름은 " + name + "에요")
print(name + "는 " + str(age) + "이며, " + hobby + "을 아주 좋아해요")
print(name + "는 어른일까요? "+str(is_adult))

print("우리집 " + animal + "의 이름은 " + name + "에요")
hobby = "공놀이"
print(name, "는 ", age, "이며, ", hobby, "을 아주 좋아해요")
print(name + "는 어른일까요? "+str(is_adult))

#주석

'''
이렇게 하면
여러 문장이
주석 처리
됩니다.
'''
# 편한 주석처리 방법
# 범위 지정 후 컨트롤 + 슬래시

#퀴즈

'''
Quiz. 변수를 이용하여 다음 문장을 출력하시오

변수명
: Station

변수값
: "사당", "신도림", "인천공항" 순서대로 입력

출력 문장
: XX 행 열차가 들어오고 있습니다.

>>>
'''

Station = "사당"
print(Station,"행 열차가 들어오고 있습니다")
print(Station + "행 열차가 들어오고 있습니다")

Station = "신도림"
print(Station,"행 열차가 들어오고 있습니다")
print(Station + "행 열차가 들어오고 있습니다")

Station = "인천공항"
print(Station,"행 열차가 들어오고 있습니다")
print(Station + "행 열차가 들어오고 있습니다")

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

number += 2
number *= 2
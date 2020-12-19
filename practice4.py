#리스트

# 지하철 칸별로 10명 20명 30명

# subway1 = 10
# subway2 = 20
# subway3 = 30

subway = [10, 20, 30]
print(subway)

subway = ["유재석", "조세호", "박명수"]
print(subway)

#조세호씨가 몇 번째 칸에 타고 있는가?
print(subway.index("조세호"))

#하하씨가 다음 정류장에서 다음 칸에 탐
subway.append("하하")
print(subway)

#정형돈씨를 유재석 / 조세호 사이에 태움
subway.insert(1, "정형돈")
print(subway)

#지하철에 있는 사람을 한 명씩 뒤에서 꺼냄
subway.pop()
print(subway)

#같은 이름의 사람이 몇 명 있는지 확인하기
subway.append("유재석")
print(subway)
print(subway.count("유재석"))

#정렬도 가능
num_list = [5,2,4,3,1]
num_list.sort()
print(num_list)

#순서 뒤집기 가능
num_list.reverse()
print(num_list)
 
#모두 지우기
num_list.clear()
print(num_list)

#다양한 자료형 함께 사용
mix_list = ["조세호", 20, True]
print(mix_list)

#리스트 확장
num_list = [5,2,4,3,1]
num_list.extend(mix_list)
print(num_list)

#사전
cabinet = {3:"유재석", 100:"김태호"}
print(cabinet[3])
print(cabinet[100])
print(cabinet.get(3))
#print(cabinet[5]) 값이 저장되어 있지 않으면 오류 출력 후 프로그램 종료
print(cabinet.get(5)) # 값이 없으면 none 출력 후 다음프로그램 실행
print(cabinet.get(5, "사용가능"))
print("hi")

print(3 in cabinet)
print(5 in cabinet)

cabinet = {"A-3":"유재석", "B-100":"김태호"}
print(cabinet["A-3"])
print(cabinet["B-100"])

#새 손님
print(cabinet)
cabinet["A-3"] = "김종국"
cabinet["C-20"] = "조세호"
print(cabinet)

#간 손님
del cabinet["A-3"]
print(cabinet)

#key 들만 출력
print(cabinet.keys())

#key, value 쌍으로 출력
print(cabinet.items())

#목욕탕 폐점
cabinet.clear()
print(cabinet)


#튜플

menu = ("돈까스", "치즈까스")
print(menu[0])
print(menu[1])

# menu.add("생선까스") 튜플은 추가를 허용하지 않는다

name = "김종국"
age = 20
hobby = "코딩"
print(name, age, hobby)

(name, age, hobby) = ("김종국", 20, "코딩")
print(name, age, hobby)

#세트(집합)
#중복없음, 순서없음

my_set = {1,2,3,3,3}
print(my_set)

java = {"유재석", "김태호", "양세형"}
python = set(["유재석", "박명수"])

#교집합(java와 python을 모두 할 수 있는 개발자)
print(java & python)
print(java.intersection(python))

#합집합(java 할 수 있거나 python 할 수 있는 개발자)
print(java | python)
print(java.union(python))

#차집합(java 할 수 있지만 python 할 줄 모르는 개발자)
print(java - python)
print(java.difference(python))

#python 할 줄 아는 사람이 늘어남
python.add("김태호")
print(python)

#java를 잊었다
java.remove("김태호")
print(java)

#자료구조의 변경

menu = {"커피", "우유", "주스"}
print(menu)
print(menu, type(menu))

menu = list(menu)
print(menu, type(menu))

menu = tuple(menu)
print(menu, type(menu))

menu = set(menu)
print(menu, type(menu))

"""
Quiz) 당신의 학교에서는 파이썬 코딩 대회를 주최합니다.
참석률을 높이기 위해 댓글 이벤트를 진행하기로 했습니다.
댓글 작성자들 중에 추첨을 통해 1명은 치킨, 3명은 커피 쿠폰을 받게 됩니다.
추첨 프로그램을 작성하시오.

조건1 : 편의상 댓글은 20명이 작성하였고, 아이디는 1~20이라고 가정
조건2 : 댓글 내용과 상관없이 무작위로 추첨하되, 중복 불가
조건3 : random 모듈의 shuffle 과 sample 을 활용

(출력 예제)

 -- 당첨자 발표 --
치킨 당첨자 : 1
커피 당첨자 : [2, 3, 4]
 -- 축하합니다 --

(활용 예제)

from random import *
lst = [1,2,3,4,5]
print(lst)
shuffle(lst)
print(lst)
print(sample(lst,1))

"""

from random import *
users = range(1, 21)
users = list(users)
shuffle(users)

winners = sample(users, 4)

print(" -- 당첨자 발표 -- ")
print("치킨 당첨자 : {0}".format(winners[0]))
print("커피 당첨자 : {0}".format(winners[1:]))
print(" -- 축하합니다 -- ")
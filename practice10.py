#------------------------------------------------모듈

# import theater_module
# theater_module.price(3) #3명이서 영화 보러 갔을 때 가격
# theater_module.price_morning(4) #4명이서 조조 할인 영화 보러 갔을 때 가격
# theater_module.price_soldier(5) #5명의 군인이 영화 보러 갔을 때 가격

# import theater_module as mv #theater_module을 mv로 호출
# mv.price(3)
# mv.price_morning(4)
# mv.price_soldier(5)

# from theater_module import * #theater_module을 모두 사용
# price(3)
# price_morning(4)
# price_soldier(5)

# from theater_module import price, price_morning #필요한 정의만 가져다 사용
# price(5)
# price_morning(6)

# from theater_module import price_soldier as price #theater_module의 price_soldier를 price로 사용
# price(5)

#--------------------------------------------------패키지

# import travel.thailand
# trip_to = travle.thailand.ThailandPakage()
# trip_to.detail()

# from travel.thailand import ThailandPakage
# trip_to = ThailandPakage()
# trip_to.detail()

# from travel import vietnam
# trip_to = vietnam.VietnamPakage()
# trip_to.detail()

#---------------------------------------------------__all__, 모듈 직접 실행

# from travel import *
# # trip_to = vietnam.VietnamPakage()
# trip_to = thailand.ThailandPakage() 
# trip_to.detail()

#---------------------------------------------------패키지, 모듈 위치

# import inspect
# import random
# print(inspect.getfile(random))

# from travel import*
# trip_to = thailand.ThailandPakage() 
# trip_to.detail()
# print(inspect.getfile(thailand))

#----------------------------------------------------pip install

# from bs4 import BeautifulSoup
# soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
# print(soup.prettify())

#----------------------------------------------------내장 함수

#input : 사용자 입력을 받는 함수
# language = input("무슨 언어를 좋아하세요?")
# print("{0}은 아주 좋은 언어입니다!".format(language))

#dir : 어떤 객체를 넘겨줬을 때 그 객체가 어떤 변수와 함수를 가지고 있는지 표시
# print(dir())
# import random #외장 함수
# print(dir())
# import pickle
# print(dir())
# lst = [1, 2, 3]
# print(dir(lst))

# name = "Jim"
# print(dir(name))

#---------------------------------------------------외장 함수

#glob : 경로 내의 폴더 / 파일 목록 조회 (윈도우 dir)
# import glob
# print(glob.glob("*.py")) #확장자가 py 인 모든 파일

#os : 운영체제에서 제공하는 기본 기능
# import os
# print(os.getcwd()) #현재 디렉토리 표시
# folder = "sample_dir"
# if os.path.exists(folder):
#     print("이미 존재하는 폴더입니다.")
#     os.rmdir(folder)
#     print(folder, "폴더를 삭제하였습니다.")
# else:
#     os.makedirs(folder) #폴더 생성
#     print(folder, "폴더를 생성하였습니다.")

#time : 시간 관련 함수
# import time
# print(time.localtime())
# print(time.strftime("%Y-%m-%d %H:%M:%S"))

# import datetime
# print("오늘 날짜는 ", datetime.date.today())
# #timedelta : 두 날짜 사이의 간격
# today = datetime.date.today() #오늘 날짜 저장
# td = datetime.timedelta(days=100) #100일 저장
# print("우리가 만난지 100일은", today + td) #오늘부터 100일 후

'''
Quiz) 프로젝트 내에 나만의 시그니처를 남기는 모듈을 만드시오

조건 : 모듈 파일명은 byme.py 로 작성

(모듈 사용 예제)
import byme
byme.sign()

(출력 예제)
이 프로그램은 이승직에 의해 만들어 졌습니다.
유튜브 : http://youtube.com
이메일 : dltmdwlr@gmail.com
'''
import byme
byme.sign()
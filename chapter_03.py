# Chapter03-1
# 숫자형

# 파이썬 지원 자료형
"""
int : 정수
float : 실수
complex : 복소수
bool : 불린
str : 문자열(시퀀스)
list : 리스트(시퀀스)
tuple : 튜플(시퀀스)
set : 집합
dict : 사전
"""

# 데이터 타입
str1 = "Python"
bool = True
str2= 'Anaconda'
float_v = 10.0 # 10 == 10.0
int = 7
list = [str1, str2]
print(list)

dict = {
    "name" : "Machine Learning",
    "version" : 2.0
}

tuple = (7, 8, 9)
tuple2 = 7 ,8, 9
set = {3, 5, 7}

# 데이터 타입출력
print(type(str1))
print(type(bool))
print(type(str2))
print(type(float_v))
print(type(int))
print(type(list))
print(type(tuple))
print(type(set))

# 숫자형 연산자
"""
+ - *


"""


i1 = 39
i2 = 9939
big_int1 = 777777777888382323
big_int2 = 343434323423411111

f1 = 1.234
f2 = 3.134

# +
print(">>>>>>>>+")
print("i1 + i2 :", i1 + i2)
print("f1 + f2 :", f1 + f2)
print("big_int1 + big_int2 :", big_int1 + big_int2)


#형이 다른것끼리 연산하면 형변환이 자동으로 이뤄진다

# *
print(">>>>>>>>*")
print("i1 * i2 :", i1 * i2)
print("f1 * f2 :", f1 * f2)
print("big_int1 * big_int2 :", big_int1 * big_int2)



# 형변환 실습

a = 3.
b = 6
c = .7
d = 12.7
# 타입출력
print(type(a), type(b), type(c), type(d))

# 형변환
print(float(b))

#print(int(True)) # True : 1 False : 0
#print(float(False))
#print(complex(3))

# 수치 연산 함수

x, y = divmod(100, 8)
print(x, y)
print(pow(5,3), 5 ** 3)


# 외부 모듈
import math
print(math.ceil(5.1)) # x 이상의 수중에서 가장 작은 정수
print(math.pi)

###

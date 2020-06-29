# Chapter04_2
# 파이썬 반복문
# 랙 tlftmq

#코딩의 핵심
#for in <colleciton>
# <loop body>

for v1 in range(10): # 0~9
    print('v1 is :', v1)

for v2 in range(1,  11): # 1 ~ 10
    print('v2 is :', v2)

for v3 in range(1, 11, 3):
    print('v3 is :', v3)



# 1 ~1000 합
sum1 = 0

for v in range(1, 1001):
    sum1 += v

print(sum1)

print(sum(range(1,1001)))

print(type(range(1,11)))

sum2 = 0
for v2 in range(1, 1001, 4):
    sum2 += v2

print(sum2)

# Iterables 자료형 반복
# 문자열, 리스트 튜플, 집합, 사전(딕셔너리)
# iterable 리턴함수 : range, reversed, enumerate, filter,map, zip

names = ['Kim', 'Park','Cho','Lee','Yoo', 'Han', 'Choi']

for n in names :
    print('You are :' , n)

lotto_numbers = [11, 19, 20, 29, 33, 38, 41]

for n in lotto_numbers:
    print('number :', n)

print()
print()

my_info = {
    "name" : "lee",
    "age" : 33,
    "city" : "seoul"
}

for k in my_info:
    print('key :', my_info.get(k))

for v in my_info.values():
    print(v)

name = 'FineAppLE'

for n in name:
    if n.isupper():
        print(n)
    else:
        print(n.upper())


# break

numbers = [14, 3, 4, 6, 10, 124, 18, 1, 33, 15, 23, 34, 35, 36, 37]

for num in numbers:
    if num == 34:
        print('Found : 34!')
        break
    else:
        print('not found')

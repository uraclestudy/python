#Chapter04-1
#파이썬제어문
#if실습 들여쓰기!!1

#기본 형식
print(type(True)) #0이 아닌수 , "abc", [1,2,3...]
print(type(False)) # 0, "",[] (),...

#얘

if True:
    print('Good')
if False:
    print('BAd')
else:
    print('Good!')

print()
#관계연산자

# >, >=, <=, ==, !=
x = 15
y = 10

#양변이 같은경우 참
print(x == y)

#양변이 다를때 참
print(x != y)

print(x > y)
print(x >= y)
print(x < y)

city = ""
if city:
    print("You are in:", city)
else:
    print("plz enter your city")


city2 = "Seoul"
if city2:
    print("You are in:", city2)
else:
    print("plz enter your city")

#논리연산자 (중요)
# and, or , not

a = 75
b = 40
c = 50


print('and:', a > b and b > c)
print('or:', a > b or b > c)
print('not:', not a > b)
print('not:', not b > c)


# 산술, 관계, 논리 우선순위
# 산술 > 관계 > 논리
print('e1 :', 3+12 > 7+3)
print(5 + 10 > 3 and 7 + 3 == 10)
print( 5+10 > 0 and not 7 + 3 == 10)



score1 = 90
score2 = 'A'

if score1 >= 90 and score2 == 'A':
    print('PASS')
else:
    print('FAIL')


#예 5

id1 = 'vip'
id2 = 'admin'
grade ='platinum'

if id1 == 'vip' or id2 == 'admin':
    print('관리자 입장')
else :
    print('sssee')

if id2 == 'admin' and grade =='platinum':
    print('최상위 관리자')

#다중 조건문

num =90
grade = 'A'
total = 85
if num >=90:
    print('Grade : A')
elif num >=80:
    print('Grade : B')
elif num >= 70:
    print('Grade : C')
elif num >= 60:
    print('Grade : D')
else:
    print('Grade : F')

#중첩조건문
if grade =='A':
    if total >= 90:
        print('장학금 100%')
    elif total >=80:
        print('장학금 50%')
    else:
        print('장학금 없어')


# in, not if __name__ == '__main__':

    q = [10,20,30]
    w = {70,80,90,100}
    e = {"name" : "lee", "city" : "Seoul", "grade" : "A"}
    r = (10,12,14)
    print( 15 in q)
    print( 90 in w)
    print ( 12 not in r)

print("name" in e)
print("Seoul" in e)
print("Seoul" in e.values())

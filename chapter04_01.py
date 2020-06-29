#Chapter04-1
#파이썬제어문
#if실습

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

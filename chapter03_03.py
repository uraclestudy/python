# Chapter03-3
# 파이썬 리스트
# 자료구조에서 중요
# 리스트 자료형(순서, 중복, 수정, 삭제)

# 선언
a = []
print(type(a))
b = list()
c = [70, 75, 80, 85]
d = [1000, 10000, 'Ace', 'Base', 'Captine']
e = [1000, 10000, ['Ace', 'Base', 'Captine']]
f = [21.42, 'foobar', 3, 4, False, 3.14159]
print(len(c))

#인덱싱
print('>>>>>')
print('d - ', type(d), d)
print('d - ', d[1])
print('d - ', d[0] + d[1] + d[1])
print('d - ', d[-1])
print('e - ', list(e[-1][1]))

#슬라이싱
print('d - ', d[0:3])
print('>>>>>>')
print('d - ', d[2:])
print('e - ', e[-1][1:3])

#리스트연산
print('>>>>>>')
print('c + d',c+d)
print('c * 3',c*3)
print("'Test' + c[0]", 'Test' + str(c[0]))

# 값비교
print(c == c[:3] + c[3:])
print(c)
print(c[:3] + c[3:])
# Identity(id)

temp = c
print (temp, c)
print(id(temp))
print(id(c))

#리스트 수정,ㅅ ㅏㄱ제
print('>>>>>>')
c[0] = 4
print('c - ', c)
c[1:2] = [['a', 'b', 'c']] #괄호가 두개
print('c - ', c)

c[1:2] = ['a', 'b', 'c']
c[1] = ['a', 'b', 'c']

c[1:3] = []
print('c - ', c)
del c[2] #삭제


#리스트 함수
a = [5,2,3,1,4]
print('a - ', a)
a.append(10)
print('a - ', a)
a.sort()
print('a - ', a)
a.reverse()
print('a - ', a)
print('a - ', a.index(3), a[3])
a.insert(2, 7)
print('a - ', a)
a.reverse()
#del a[6]
#print('a - ', a)
a.remove(10)
print('a - ', a)
print('a - ', a.pop())
print('a - ', a)
print('a - ', a.pop())
print('a - ', a)
print('a - ', a.pop())
print('a - ', a)
print('a - ', a.pop())
print('a - ', a.count("사과"))
ex = [8, 9]
a.extend(ex)
print('a - ', a)

#삭제 remove, pop, del

#반복문활용

while a:
    data = a.pop()
    print(data)

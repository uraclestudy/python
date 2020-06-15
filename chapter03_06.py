#Chapter03-6
#집합(set) 특징
# 집합 자료형 순서X 중복X
#선언

a = set()

print(type(a))

b= set([1,2,3,4,4,4,4])
c= set([1,4,5,6])
d = set([1,2,'Pen','Cat','Plate'])
e = {'key', 'bar', 'baz' }

f= {42, 'foo', (1,2,3), 3.1234314}


print('a -' , type(a), a)
print('b -' , type(b), b)

print('c -' , type(c), c)

print('d -' , type(d), d)

print('e -' , type(e), e)

print('f -' , type(f), f)

#튜플변환 (set -> tuple)
t = tuple(b)
print('t - ', type(t), t)
print('t -', t[0], t[1:3])

#리스트변환 (set -> list)
l = list(c)
l2 = list(e)

print(l)
print(l2)

# 길이
print(len)

# 집합 자료형 활용

s1 = set([1,2,3,4,5,6])
s2 = set ([4,5,6,7,9,8])

print(s1 & s2)
print(s1.intersection(s2)) #교집합

print( s1 | s2)
print(s1.union(s2)) #합집합

print(s1 -s2)
print(s1.difference(s2)) #차집합

#중복원소 확인

print(s1.isdisjoint(s2))  #교집합 있으면 flase, 잇으면 ture

#부분집합확인

print(s1.issubset(s2)) # s1이 s2의 부분집합이냐
print(s1.issuperset(s2)) # subset  반대개념


# 추가 제거

s1 = set([1,2,3,4])
s1.add(5)
print(s1)


s1.remove(2) #예외가 발생하니까 체크해야됨 실제 값이 있는지
print(s1)
s1.discard(3)
s1.discard(7) #예외(에러) 발생하지않음
print(s1)

s1.clear()
print(s1)

#Chapter03-5
# 파이썬딕셔너리
# 범용적으로 가장많이사용
# 딕셔너리 자료형(순서 없음, 키 중복불가, 수정 삭제 가능

#선언

a ={'name' : 'Kim' , 'phone' : '01033336666', 'birth' : '870202'}
b = {0 : 'hello kitty'}
c = {'arr' : [1,2,3,4]}
d = {
    'Name' : 'nical ki',
    'City' : 'Seoul',
    'Age' : 33,
    'Grade' : 'A',
    'Status' : True
}

e = dict([
    ('Name', 'nical ki'),
    ('City', 'Seoul'),
    ('Age', 33),
    ('Grade', 'A'),
    ('Status', True)
])

f = dict(
    Name ='niceman',
    City ='Seoul',
    Age=33,
    Garde='A',
    Status=True
)

print('a - ', type(a), a)
print('b - ', type(b), b)
print('c - ', type(c), c)
print('d - ', type(d), d)
print('e - ', type(e), e)
print('f - ', type(f), f)


#출력

print('a - ', a['name'])  #키가존재하지않으면 에러발생
print('a - ', a.get('name1')) #키가존재하지않으면 None 처리
print('b -', b[0])
print('b -', b.get(0))
print('f -', f.get(0))
print('f -', f.get('City'))
print('f -', f.get('Age'))

# 딕셔너리 추가
a['address'] ='seoul'
a['rank'] =[1,2,3]
print('a -', a)

print(len(a))
print(len(b))
print(len(c))
print(len(d))

#dict_key, dict_values, dict_items: 반복문(_iter_)에서 사용가능

print('a - ', a.keys())
print('a - ', b.keys())
print('a - ', c.keys())
print('a - ', d.keys())
print('a - ', list(c.keys()))
print('a - ', list(d.keys()))
print('b:  - ', list(c.values()))
print('b - ', list(d.values()))
print('b:  - ', list(c.items()))
print('b - ', list(d.items()))
print()

print('a - ', a.pop('name'))
print('a - ', a)

print()

print('f -', f.popitem())
print('f -', f)
print('f -', f.popitem())
print('f -', f)
print('f -', f.popitem())
print('f -', f)
print('f -', f.popitem())
print('f -', f)
print('f -', f.popitem())
print('f -', f)


print()

print('a - ', 'birth2' in a)
print('d - ', 'Age' in d)


#수정 & 추가

a['test']= 'test_dict'

print('a -' , a)
a['address'] = 'dj'
print('a -' , a)


a.update(birth='980902')
print('a -' , a)
temp = {'address' :'busan'}

a.update(temp)
print('a -' , a)

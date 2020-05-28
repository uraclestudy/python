#파이썬 변수

# 기본선언
n = 700

#출력

print(n)
print(type(n))

# 동시선언
var = 75

#재선언
var = "Change Value"

#출력
print(var)
print(type(var))

#object References
#변수값 할당상태
# 1. 타입에 맞는 오브젝트 생성
# 2. 값 생성
# 3. 콘솔출력

# 예1)
print(300)
print(int(300))

# 예2)
# n -> 777

n = 777
print( n, type(n))
print()

m = n

print(m, n)
print(type(m), type(n))

m = 400

print(m, n)
print(type(m), type(n))

# id(identity) 확인 : 객체의 고유값확인
m = 800
n = 655

print(id(m))
print(id(n))
print(id(m) == id(n))
print()

# 같은 오브젝트 참조
m = 800
n = 800

print(id(m))
print(id(n))
print(id(m) == id(n))
print()


# 다양한 변수 선언
# Camel Case : numberOfColleageGraduates -> Method
# Pascal Case : NumberOfColleageGraduates -> class
# Snake Case : number_of_colleage_graduates 보통 파이썬의 변수

# 허용하는 변수 선언법
age = 1
Age = 2
aGe = 3
AGE = 4
a_g_e = 5
_age = 6
age_ = 7
_AGE_ = 8

# 예약어는 변수명으로 불가능
"""
False	def	if	raise
None	del	import	return
True	elif	in	try
and	else	is	while
as	except	lambda	with
assert	finally	nonlocal	yield
break	for	not
class	from	or
continue	global	pass
"""

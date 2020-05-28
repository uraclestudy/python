#파이썬 문자형 중요

#문자열생성
str1 = "I am Python"
str2 = 'python'
str3 = """How are you?"""
str4 = '''thankyou!!'''

print(type(str1),type(str2),type(str3),type(str4))
print(len(str1), len(str2), len(str3), len(str4))

# 빈문자열

str1_t1 = ''
str2_t2 = str()

print(type(str1_t1), len(str1_t1))
print(type(str2_t2), len(str2_t2))


#이스케이프 문자 사용
#I'm Boy

print("I'm Boy") #큰따옴표로 묶거나.
print('I\'m Boy')
print('I\\m Boy')

print('a \n b')
print('a \t b')
print('a \t b')

escape_str1= "do you have a \" retor games\"?"
print(escape_str1)

escape_str2 = 'What \'s on tv?'
print(escape_str2)

# 탭 줄바꿈

t_s1 = "click \t start!"
t_s2 = " new line \n chekck"

print(t_s1)
print(t_s2)

#raw stirng
raw_s1 = r'D:\pythonstudynic\test'
print(raw_s1)


#멀티라인 입력
# 역슬래시 사용
multi_str = \
"""
String
multiline
test
hahaah
"""
print(multi_str)

asf = \
'ekfdjsa' \
'dddd' \

print(asf)

#문자열 연산
str_o1 = "python"
str_o2 = "apple"
str_o3 = "how are you doing"
str_o4 = "seoul daejeon busan jinju"

print(str_o1 * 3)
print(str_o1 + str_o2)
print('y' in str_o1)
print('n' in str_o1)
print('P' not in str_o2)

#문자열 형 변환
print(str(66), type(str(66)))
print(str(10.1))
print(str(True), type(str(True)))

# 문자열 함수(upper, isalnum, startswith, cout, endswith, isalpha

print("Capitalize : ", str_o1.capitalize())
print("endswith? : ", str_o1.endswith("!"))
print("replace", str_o1.replace("thon", 'good'))
print("sorted: ", sorted(str_o1))

print("split: ", str_o4.split(' '))


#반복(시퀀스)
im_str= "Good Boy!"

print(dir(im_str))  #_iter_

#출력
for i in im_str :
    print(i)
#슬라이싱 연습

str_s1 = "Nice Python"
print(str_s1[0:3])
print(str_s1[5:11])
print(str_s1[5:])
print(str_s1[:len(str_s1)])
print(str_s1[1:9:2])
print(str_s1[-5:])
print(str_s1[1:-1])
print(str_s1[::2])
print(str_s1[::-1])

#아스키코드
a ='z'

# 함수의 기초

# 함수의 정의

def add(a,b):
    #print(f"a는 {a}야")
    return a+b
c = add(3,4)
print(c)

def say():
    return 'hi'
#print(say())

def say_nothing():
    print('say nothing')
say_nothing()

# 함수의 초기값을 미리 설정.
def say_myself(name,old,man=True):
    print("나의 이름은 %s입니다."%name)
    print("나의 나이는 %d입니다"%old)
    if man == True :
        print("나의 성별은 남자입니다.")
    else :
        print("나의 성별은 여자입니다.")
    
say_myself("박현아1", 30, False)
say_myself("박현아2", 35)
say_myself("박현아3", 40, True)

# 지역변수
a = 1
def vartest(a):
    a = a+1 # 이때의 a 는 함수 밖에 선언된 a 랑 다른 것임. # 이 함수 내부에서만 사용함.
vartest(a)
print("지역변수의 a 값 :: %d"%a) # 출력값 1 --> 33행의 a 임.

# 그렇다면 전역변수의 a 에 값을 더하고 싶으면?
def vartest(a):
    return a+1
a = vartest(a)
print("전역변수의 a 값 :: %d"%a)

# lambda 사용
add = lambda a,b: a+b
print("람다 사용 :: %d"%add(3,4))

# 숫자 리스트
numbers = [1,2,3,4,5,6,7,8,9,10]

# ------------------------------------------------------------------------

# filter 와 lambda 사용해보기

# 짝수를 판별하는 함수
def is_even(x):
    return x % 2 == 0

# filter 함수를 사용해서 짝수만 필터링
'''
filter(함수, 반복가능한 객체)
'''
even_numbers = list(filter(is_even, numbers))
#even_numbers = filter(is_even, numbers) # 객체 형태로 나옴.
print(even_numbers)

result = list(filter(lambda x: x % 2 ==0, numbers)) # 람다를 쓰게 된다면? 
print(result)

# ------------------------------------------------------------------------

# input() 함수의 사용
a = input()
print("a의 값은 %s 입니다."%a)

# ------------------------------------------------------------------------

# print 함수
## 중요 중요!!
aa = 123
print(aa) # 결과값 :: 123
print(print(aa)) # 결과값 :: None # --> print 함수는 반환값이 없음.

print("life", "is", "too short") # 띄어쓰기 # life is too short
print("life" " " "is" " " "too short") # 연결하기 # life is too short
print("life" "-" "is" " " " too short") # 연결하기 # life-is  too short
print("life" + "_" + "is" + "_" + "too short") # 연결하기 # life_is_too short

# ------------------------------------------------------------------------
# 파일생성
f = open("./python_programming/python_9th/python_9th.txt", "w")
f.close()

# 파일 읽기
# 1줄 읽기
f = open("./python_programming/python_9th/python_9th.txt", "r")
line = f.readline()
print(line)
f.close()

# 1줄씩 읽는 것을 반복문 사용해서 모든 값 읽기
f = open("./python_programming/python_9th/python_9th.txt", "r")
count = 0
while True:
    line = f.readline()
    if not line: 
        break
    count += 1
    print(f"{count}: {line}", end="")  # 줄 번호: 내용
f.close()

print(f"\n총 {count}줄 읽음")
''' 결과값 ::
>>> 
1: test1
2: a 1 2 3dddddaaaaaaa 1 2 3dddddaaaaaaa 1 2 3dddddaaaaaaa 1 2 3dddddaaaaaaa 1 2 3dddddaaaaaaa 1 2 3dddddaaaaaaa 1 2 3dddddaaaaaaa 1 2 3dddddaaaaaaa 1 2 3dddddaaaaaaa 1 2 3dddddaaaaaa
3: b
4: c
5: d
6: e
>>> 총 6줄 읽음
'''

# 모든 줄 읽기. # readlines
f = open("./python_programming/python_9th/python_9th.txt", "r")
lines = f.readlines()
print(type(lines))
for line in lines:
    print(line)

'''   
# enumerate()는 파이썬 내장 함수로, 
# 반복 가능한(iterable) 객체를 순회할 때 
# **현재 인덱스(index)**와 값(value) 을 함께 얻고 싶을 때 사용합니다.
'''

for idx, line in enumerate(lines, start=1):
    print(f"{idx}: {line}")
f.close()

# read 는 파일 내용 전체를 하나의 문자열로 반환함.
f = open("./python_programming/python_9th/python_9th.txt", "r")
data = f.read()
print(type(data)) # <class 'str'>
print(data)
''' 결과값 :: 
test1
a 1 2 3dddddaaaaaaa 1 2 3dddddaaaaaaa 1 2 3dddddaaaaaaa 1 2 3dddddaaaaaaa 1 2 3dddddaaaaaaa 1 2 3dddddaaaaaaa 1 2 3dddddaaaaaaa 1 2 3dddddaaaaaaa 1 2 3dddddaaaaaaa 1 2 3dddddaaaaaa
b
c
d
e
'''
f.close()

# 파일에 새로운 값 추가
f = open("./python_programming/python_9th/python_9th.txt", "a")
for i in range(11, 20):
    data = "%d번째 줄입니다.\n" % i
    f.write(data)
f.close()

# with open ( 파일명, w/r/a ) as 파일변수명 # 자동으로 open 하고 close 까지 함.
with open("./python_programming/python_9th/auto_open_n_close.txt", "w") as f:
    f.write("life is too short, you need python")
    
with open("./python_programming/python_9th/auto_open_n_close.txt", "r") as f:
    lines = f.readlines()
    for idx, line in enumerate(lines, start=1):
        print(f"{idx}: {line}")
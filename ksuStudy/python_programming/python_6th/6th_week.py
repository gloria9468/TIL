# print('test')
'''


a = '1'
b = 1
c = '1'
# print( type(a) )


""" 주석은 이렇게 처리 """
if( a == b) :
    print('a==1')    
    print('type a 는 -- str() -- ' + str(type(a)))
    print(f'type a 는 -- f -- {type(a)}')
elif ( a == c ) :
    print(f' a == c {a == c}')
else :
    print('a!=1')
    

## 강의 실습 파일
# 조건문 기본
age = -25
if( age >= 10 and age < 20 ) :
    print(f'age가 {age} 입니다.')
elif( age >= 0 and age < 10 ) :
    print(f'영유아 입니다.')
elif( age >= 20 ) :
    print(f'성인 입니다.')
else :
    print(f'나이를 잘 못 입력했습니다. -- {age}')


'''

'''
# 정상 혈압 유무 판단
# 딕셔너리 형태로 변수 선언
bloodPressure = {}
print('당신의 나이를 입력하세요')
bloodPressure['age'] = int(input()) # input 같이 키보드로 입력받는 것은 무조건 문자열로 받아짐. --> string 을 int 로 타입 변환해줘야함.

print('당신의 성별을 입력하세요')
bloodPressure['sex'] = input()

print('당신의 최고혈압을 입력하세요')
bloodPressure['maxBP'] = int(input())

print('당신의 최저혈압을 입력하세요')
bloodPressure['minBP'] = int(input())

print( bloodPressure )

if (bloodPressure['age'] >= 10 and bloodPressure['age'] < 20):  # 10대
    if(bloodPressure['sex'] == 'M'):
        if(bloodPressure['maxBP']<102 and bloodPressure['minBP']<64):
            print("정상 혈압입니다.")
        else:
            print("비정상 혈압입니다. 정밀 검사가 필요합니다")
    elif (bloodPressure['sex'] == 'F'):
        if(bloodPressure['maxBP']<98 and bloodPressure['minBP']<62):
            print("정상 혈압입니다.")
        else:
            print("비정상 혈압입니다. 정밀 검사가 필요합니다")
    else:
        print("성별을 잘못 입력하였습니다.")    # 성별에 대한 예외 처리

elif (bloodPressure['age'] >= 20  ): # 20대 이상

    if(bloodPressure['sex'] == 'M'):
        if(bloodPressure['maxBP']<120 and bloodPressure['minBP']<80):
            print("정상 혈압입니다.")
        else:
            print("비정상 혈압입니다. 정밀 검사가 필요합니다")
    elif (bloodPressure['sex'] == 'F'):
        if(bloodPressure['maxBP']<115 and bloodPressure['minBP']<75):
            print("정상 혈압입니다.")
        else:
            print("비정상 혈압입니다. 정밀 검사가 필요합니다")
    else:
        print("성별을 잘못 입력하였습니다.")   # 성별에 대한 예외 처리
else:
    print( "나이를 잘못 입력하였습니다.")       # 나이에 대한 예외 처리


'''


# 23
a = [10,20,30,40]
for i in a:
    if i % 20 == 0:
        for j in range(i // 10 - 1):
            print("test")
            
            
total = 0
total += 20
total /= 2
total **= 2
print("total")
print(total)            


# 29
x = 10
y = 5
z = 7
result = ""

if x < y or z < x and y > z: # F or F and F
    result = "its true"
elif x > y and y < z :
    result = "its Fa"
elif x == y or y == z:
    result = "none"
else:
    result = "somthing else"
    
print(result)    

aa = "apple"
print(aa[:3])





import itertools

# 1부터 9까지의 숫자 리스트
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# 3개를 순서 상관없이 뽑는 조합 생성
combinations = list(itertools.combinations(numbers, 3))

# 조합의 수 출력
print(len(combinations))  # 출력: 84

# 모든 조합 출력
for combination in combinations:
    print(combination)

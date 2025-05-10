# 클래스 실습해보기

# 클래스 정의
# 클래스명은 대문자로 선언하는 게 일반적임.

# 파이썬에서 클래스 선언할 때 생성자 만들 때 쓰는 self 는 뭔가 java 의 this 랑 비슷한 느낌.

class Robot:
    
    pass

# 객체 생성
r1 = Robot()
r2 = Robot()

# 클래스의 구성요소
class Robot:
    robot_model = "t800"  # 클래스 변수

    def set_position(self, x, y):   # 메서드(method)
        self.x = x       # 인스턴스 변수
        self.y = y       # 인스턴수 변수

    def forward(self, a, b):   # 앞으로 이동
        self.x += a    #  a 만큼 앞으로
        self.y += b    # b 만큼 앞으로


    def backward(self, a, b):   # 앞으로 이동
        self.x -= a    #  a 만큼 뒤로
        self.y -= b    # b 만큼 뒤로


r1 = Robot()
r2 = Robot() 
r1.robot_model = "t0001"
print(r1.robot_model + " ---- " + r2.robot_model)

# ------------------------------------------------------------------------------------
# 인스턴스 변수 설정
r1.set_position(100, 200)    # 객체 메서드를 이용한 인스턴스 변수 설정
r2.set_position(300, 400)    # 객체 메서드를 이용한 인스턴스 변수 설정

print(r1.x, r1.y)
print(r2.x, r2.y)

# ------------------------------------------------------------------------------------
# 클래스 내의 함수 사용해보기
r1.forward(10, 10)
print(r1.x, r1.y)

r2.backward(10,10)
print(r2.x, r2.y)
     
# ------------------------------------------------------------------------------------
# 계산기 클래스

class FourCal:
    num = 0
    def setdata(self, first, second):
        FourCal.num += 1
        self.first = first
        self.second = second
    def add(self):
        result = self.first + self.second
        return result
    def mul(self):
        result = self.first * self.second
        return result
    def sub(self):
        result = self.first - self.second
        return result
    def div(self):
        result = self.first / self.second
        return result
    
a = FourCal()
b = FourCal()
a.setdata(4, 2)
b.setdata(3, 8)

print("a.add() = ",a.add())
print("a.mul() = ",a.mul())
print("a.sub() = ",a.sub())
print("a.div() = ",a.div())
print("b.add() = ",b.add())
print("b.mul() = ",b.mul())
print("b.sub() = ",b.sub())
print("b.div() = ",b.div())

'''
>>> print("a.add() = ",a.add())
a.add() =  6
>>> print("a.mul() = ",a.mul())
a.mul() =  8
>>> print("a.sub() = ",a.sub())
a.sub() =  2
>>> print("a.div() = ",a.div())
a.div() =  2.0
>>> print("b.add() = ",b.add())
b.add() =  11
>>> print("b.mul() = ",b.mul())
b.mul() =  24
>>> print("b.sub() = ",b.sub())
b.sub() =  -5
>>> print("b.div() = ",b.div())
b.div() =  0.375
'''
# 생성자 정의

class Country:
    name = '국가명'
    population = '인구'
    capital = '수도'
    calling_code = '국가 전화번호'

    def __init__(self,name,population, capital):
        print("init class")
        self.name = name
        self.population = population
        self.capital = capital

    def show(self):
        print("국가명은 : %s 입니다."%self.name)
        print("인구는 : %s명 입니다."%self.population)
        print("수도는 : %s 입니다." %self.capital)
        print("국가 전화번호는 : %s 입니다." %self.calling_code)


# 생성자 선언할 때
# 생성자 parameter 개수를 맞추지 못할 경우--- 에러 발생!!!
korea = Country()
'''
>>> korea = Country()
Traceback (most recent call last):
  File "<python-input-1>", line 1, in <module>
    korea = Country()
TypeError: Country.__init__() missing 3 required positional arguments: 'name', 'population', and 'capital'
'''
# 생성자 parameter 규칙을 맞추며 클래스 객체화 해야한다.

korea = Country("대한민국",50000000,"서울") 
''' 
>>> korea = Country("대한민국",50000000,"서울")
init class
'''

korea.show()
'''
>>> korea.show()
국가명은 : 대한민국 입니다.
인구는 : 50000000명 입니다.
수도는 : 서울 입니다.
국가 전화번호는 : 국가 전화번호 입니다.
'''

korea.calling_code = 82
korea.show()
'''
>>> korea.show()
국가명은 : 대한민국 입니다.
인구는 : 50000000명 입니다.
수도는 : 서울 입니다.
국가 전화번호는 : 82 입니다.
'''

# --------------------------------------------------

# 클래스 상속 및 정의

class Korea(Country):
    independence_fighter = []

    def add_independence_fighter(self, name):
        self.independence_fighter.append(name)

    def show_independence_fighter(self):
        print(self.independence_fighter)

    def show(self):     # 메서드 오버라이딩
        super().show()
        print("우리나라의 독립운동가 : ",self.independence_fighter)
        
a = Korea("대한민국",50000000,"서울")
'''
>>> a = Korea("대한민국",50000000,"서울")
init class
'''
a.add_independence_fighter("유관순")
a.add_independence_fighter("김구")
a.show()
'''
>>> a.add_independence_fighter("유관순")
>>> a.add_independence_fighter("김구")
>>> a.show()
국가명은 : 대한민국 입니다.
인구는 : 50000000명 입니다.
수도는 : 서울 입니다.
국가 전화번호는 : 국가 전화번호 입니다.
우리나라의 독립운동가 :  ['유관순', '김구']
'''

# 생성자 함수의 오버라이딩
class Korea(Country):
    independence_fighter = []

    # Country 의 생성자를 재정의함. 
    # 생성자 오버라이딩 했음.
    def __init__(self):
        self.name = "대한민국"
        self.population = 50000000
        self.capital = "서울"


    def add_independence_fighter(self, name):
        self.independence_fighter.append(name)

    def show_independence_fighter(self):
        print(self.independence_fighter)

    def show(self):     # 메서드 오버라이딩
        super().show()
        print("우리나라의 독립운동가 : ",self.independence_fighter)


# 처음부터 생성자에 값을 넣어서 시작했음. 
# super class 의 생성자 오버라이딩 해서 사용함.
a = Korea() 
a.add_independence_fighter("유관순")
a.add_independence_fighter("안중근")
a.show()        
'''
>>> a = Korea()
>>> a.add_independence_fighter("유관순")
>>> a.add_independence_fighter("안중근")
>>> a.show()
국가명은 : 대한민국 입니다.
인구는 : 50000000명 입니다.
수도는 : 서울 입니다.
국가 전화번호는 : 국가 전화번호 입니다.
우리나라의 독립운동가 :  ['유관순', '안중근']
'''


class USA(Country):
    state = []

    def __init__(self):
        self.name = "미국"
        self.population = 300000000
        self.capital = "Washington"

    def add_state(self, state):
        self.state.append(state)

    def show(self):
        super().show()
        print("미국의 주 : ",self.state)

a = USA()
a.add_state('CA')
a.add_state('NY')
a.add_state('TX')
a.show()
             
'''
>>> a = USA()
>>> a.add_state('CA')
>>> a.add_state('NY')
>>> a.add_state('TX')
>>> a.show()
국가명은 : 미국 입니다.
인구는 : 300000000명 입니다.
수도는 : Washington 입니다.
국가 전화번호는 : 국가 전화번호 입니다.
미국의 주 :  ['CA', 'NY', 'TX']
'''             
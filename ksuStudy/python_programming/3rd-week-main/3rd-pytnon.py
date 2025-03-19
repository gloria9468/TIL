# 파이썬에서 변수 선언 방법
a=1
b=5
print("변경 전---")
print(f"a = {a}")
print(f"b = {b}")

a,b = b,a
print("변경 후---")
print(f"a = {a}")
print(f"b = {b}")

# 파이썬 연산자 
# // :: 정수 몫
a=10
b=3
c = a // b
print(f"c // {c}")

# ** :: 누승 연산 :: 제곱
c = a**b # 10의 3승
print(f"c ** {c}")
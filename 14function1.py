'''
함수
  형식] def 함수명(매개변수1, 매개변수2):
        실행부
        return 결과1, 결과2
  상황에 따라 매개변수와 return문은 생략이 가능하다.
  2개 이상의 값을 반환하는 경우 Tuple로 받을 수 있다.      
'''
print(f"{'함수정의 및 호출':-^30}")
# 매개변수와 반환값 없이 수열의 결과를 출력하는 함수 정의
def sumTen():
  sum = 0
  for i in range(1,11):
    sum += i
  print('1~10까지의합:', sum)
# 함수 호출
sumTen()

print(f"{'함수정의 및 응용':-^30}")
# 네뉴출력 및 입력값을 반환하는 함수
def menu():
  print('메뉴중 숫자를 선택하세요:')
  print('1.덧셈 2.뺄셈 3.곱셈 4.나눗셈')
  print('5.종료')
  # 입력받은 문자를 반환한다.
  return input('번호선택:')
# 사칙연산을 위한 함수(매개변수ㅇ, 반환값X)
def add(a, b):
  print(a, "+", b, '=', a+b)
def sub(a, b):
  print(a, "-", b, '=', a-b)
def mul(a, b):
  print(a, "*", b, '=', a*b)
def div(a, b):
  print(a, "/", b, '=', a/b)
  
choice = 0
# 무한루프 내부에서 사용자가 종료할때까지 반복해서 함수 호출
while True:
  # 함수의 반환값을 정수로 변환 후 변수에 저장
  choice = int(menu())
  # 사칙연산 수행 및 반복문 탈출
  if choice == 1:
    add(int(input("덧셈 a=")), int(input("b=")))
  elif choice ==2:
    sub(int(input("뺄셈 a=")), int(input("b=")))
  elif choice ==3:
    mul(int(input("곱셈 a=")), int(input("b=")))
  elif choice ==4:
    div(int(input("나눗셈 a=")), int(input("b=")))             
  elif choice ==5:
    break
print("연산 종료!!")         
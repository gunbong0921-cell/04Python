print(f"{'if문 첫번째 형식':-^30}")
# 4개의 변수 생성 및 초기화
a, b, c, str = 10, 20, 30, 'Python'

# 비교연산자를 이용해서 조건 판단
if a != b:
  print("a는 b와 다르다.")
if a <= c:
  print("a는 c보다 작거나 같다.")
# 문자열 자체를 조건으로 사용할 수 있다. 빈문자열인 경우 False 반환.
if str:
  print("문자열은 True를 한다.")
# 변수의 타입이 다르므로 비교연산을 할 수 없어 에러 발생  
# if a > str: # 에러발생
#   print("문자열과 정수는 비교의 대상이 될수없다.")
 
print(f"{'if문 두번째 형식':-^30}")
# if~else 구문은 Java와 동일한 문법을 지원한다.
if not a > b:
  print('a는 b보다 크지 않습니다.')
else:
  print('a는 b보다 큽니다.')

if a == b and b != c:
  print('모든 조건을 만족합니다.')
else:
  print('조건중 False가 있습니다.')
  
if a > b or b < c:
  print('조건중 True가 있습니다.')
else:
  print('모든 조건에 만족하지 않습니다.')
  
print(f"{'if문 세번째 형식':-^30}")
# 2개 이상의 조건에서는 elif를 사용한다.(Java와 다른 문법)
age = 33
print(age, "살은 ", end="")
if age >= 35:
  print("중년입니다.")
elif age >= 30:
  print("중년의 시작입나다.")  
else:
  print("청년입니다.")               
  
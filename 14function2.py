print(f"{'2개 이상의 반환값을 가진 함수':-^30}")
def min_max(num):
  sum = 0
  # 매개변수를 통해 반복하게 되므로 컬렉션이라 예상할 수 있다.
  for val in num:
    # 각 요소를 누적해서 합산
    sum += val
  # 합산결과, 최소, 최댓값 3가지를 개별적으로 반환 
  return sum, min(num), max(num)
# 인수로 사용할 튜플 생성
numbers = (8,7,6,8,4,9,5)
# 반환값의 갯수만큼 좌측향의 변수를 선언 후 함수 호출
sumval, minval, maxval = min_max(numbers)
print("튜플의합, 최대값, 최소값:", sumval, minval, maxval)

print(f"{'지역변수와 전역변수':-^30}")
# 전역변수 정의
total = 0
def sum(arg1, arg2):
  # 함수의 지역변수로 정의
  total = arg1 + arg2
  # 전역변수와 지역변수가 충돌되면 지역변수의 우선순위가 높다.
  print("지역변수 total=", total)
  # 결과 반환. 이 변수는 함수 종료시 메모리에서 소멸된다.
  return total
# 초기값 0이 그대로 출력됨
print("전역변수 total=", total)
# 함수 호출 후 반환값은 30
print("sum(10, 20)호출후 반환값=", sum(10, 20))

'''
내부함수 : 파이썬에서는 함수내부에 다른 함수를 정의할 수 있다.
        Java의 내부클래스와 유사하다.
'''
print(f"{'내부함수':-^30}")
# 외부함수 정의
def person(name, age):
  # 내부함수 정의
  def myName(n):
    print("이름:%s" % n)
  def myAge(a):
    return "나이:%s" % a
  # 내부함수 호출 1
  myName(name)
  # 내부함수 호출 2. print 안에서 호출
  print(myAge(age))
# 외부함수를 호출하면 인수가 내부함수로 전달되어 결과가 출력됨 
person('성유겸', 13)

# 함수에서 사용하는 가장 일반적인 매개변수로 작성 순서대로 적용

print(f"{'매개변수1 : 순서 매개변수':-^30}")
def paramFunc1(str1, str2):
  print(str1, str2)
  return
cont = "은 매우 좋은 프로그램입니다."
paramFunc1("Python", cont)
  
# 매개변수수명을 그대로 사용하여 값 전달. 따라서 순서없이 작성가능
print(f"{'매개변수2 : 키워드 매개변수':-^30}")
def paramFunc2(name, age):
  print("이름:", name)
  print("나이:", age)
  return
paramFunc2(age=50, name='홍길동')

# 매개변수로 값이 전달되지 않으면 디폴트값ㅇ르 사용하는 방식
print(f"{'매개변수3 : 디폴트 매개변수':-^30}")
def paramFunc3(lan="Java"):
  print("내가 좋아하는 언어는 ", lan, "입니다")
  return
paramFunc3()
paramFunc3("C++")

# *args는 튜플이 되어 여러값(인수)를 전달받게 된다.
print(f"{'매개변수4 : 가변 매개변수(튜플)':-^30}")
def paramFunc4(*args):
  print("*args=>", args)
  result = 1
  # 튜플이므로 갯수만큼 반복 가능
  for a in args:
    # 누적해서 곱한 결과를 반환
    result *= a
  return result
print(paramFunc4(1,2,3,4))

# **man은 딕셔너리 형태로 인수를 전달받아 사용한다.
print(F"{'매개변수5 : 가변 매개변수(딕셔너리)':-^30}")
def paramFunc5(**man):
  print('**man', man)
  # 딕셔너리 이므로 key와 alue를 구분해서 사용할 수 있다.
  for key in man:
    print(key, "=>", man[key])  
paramFunc5(의인='홍길동', 장군='이순신', 임금='세종대왕')          
  

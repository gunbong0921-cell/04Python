'''
서식문자로 문자열, 정수, 실수 표현
형식] "%s %d %f 등이 포함된 문자열" % 값 또는 변수
'''

# 문자열 사용
str = '내 이름은 %s 입니다.' % '칸'
print("str1=", str)

# 리스트를 for문으로 반복해서 문자열 출력
names = ['유비', '관우', '장비']
for n in names:
  print('이름 : %s' % n)
  
# 정수 사용
money = 10000
str = '마우스 가격은 %d원 입니다.' % money
print(str)

# 실수 사용
pi = 3.141592
print('원주율은 %f' % pi)
# 소수이하 3자리까지 표현
print('원주율은 %5.3f' % pi) 

# 변수가 2개 이상인 경우 컴마로 구분해서 사용
str = '이름 : %s, 나이 : %d' % ('홍길동', 99)
print(str)

# 변수를 여러개 선언 및 초기화
phone, age, height = "010-1234-5678", 28, 181.5
# str2 = '전화번호:%s, 나이:%d, 키:%f' % (phone, age, height)
# %f 대신 %g를 사용하면 소수점 뒤의 불필요한 0이 제거됨.
# str2 = '전화번호:%s, 나이:%d, 키:%g' % (phone, age, height)
# 더 직관적인 소수점 0제거 코드
str2 = f"전화번호:{phone}, 나이:{age}, 키:{height:g}"
print("str2=", str2) 
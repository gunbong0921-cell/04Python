'''
format() 함수
: 문자열 포매팅(String formatting)은 서식문자보다 더 간단히
문자열을 표현할 수 있다. 중괄호 안에 포매팅을 저장하고 format()
함수로 값을 삽입한다.
형식] '{인덱스}' , format(값 or 변수)
'''

# 값을 직접 대입하기
str1 = 'name : {0}'.format('홍길동')
print(str1)

# 변수 대입 후 인덱스로 삽입
age = 55
str2 = 'age : {0}'.format(age)
print(str2)

# 인덱스 대신 변수명을 직접 사용하기
str3 = 'name : {name}, age : {age}'.format(name='홍길동', age=33)
print(str3)

# 인덱스를 입력하지 않으면 인자의 순서대로 매칭됨 
str4 = '이름 : {}, 나이 : {}'.format('이순신', 44)
print(str4)

# 인덱스를 사용하면 순서를 바꿀 수 있음
str5 = '나이 : {1}, 이름 : {0}'.format('이성계', 55)
print(str5)

# 인덱스를 통해 하나의 변수를 2번 이상 삽입할 수 있음
str6 = '항목1 : {0}, 항목2 : {1}, 항목3 : {0}'.format('서울','부산')
print(str6)

# 정수 N자리로 표현. 남는 자리수는 0으로 채워짐
str7 = '정수3자리 : {0:03d}, {1:03d}'.format(12345, 12)
print(str7)

# 실수 N자리로 표현. 남는 자리수는 0으로 채워짐
str8 = '소수점 아래 2자리 : {0:0.2f}, 소수점 아래 5자리 : {1:0.5f}'.format(123.1234567, 3.14)
print(str8)

# 드물지만 {} 자체를 출력해야 할때는 {{}}와 같이 두번 겹쳐서 사용
str9 = '{{ {0} }}'.format('Python 중괄호 표현')
print("str9=", str9)

# 세자리마다 컴마
str10 = 1592000
print(format(str10, ','))
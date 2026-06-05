#파이썬은 문장의 끝에 세미콜론을 사용하지 않는다.
# 또한 문자와 문자열의 구분이 없으므로, 싱글 혹은 더블 쿼테이션 모두 가능.
a = "Hello Python"
print(a, id(a))
print("한줄에 "); print("여러줄 쓰려면 "); print("세미콜론이 필요함")

# 변수 선언시 자료형을 결정하는 별도의 키워드가 없음.
a = 100
print(a, id(a))

#정수형
i = 200
print(i, type(i))

#실수형
i = 3.14
print(i, type(i))

#Bool형
# 작성시 Java와는 다르게 첫글자를 대문자로 기술해야한다.
i = True
print(i, type(i))

#문자형
i = "안녕"
print(i, type(i))

# 변수와 할당을 여러개 할때는 컴마로 좌측, 우측을 구현하여 작성. 
r, g, b = "Red", "Green", "Blue"
print(r, g, b)

i = False
print(i, type(i))
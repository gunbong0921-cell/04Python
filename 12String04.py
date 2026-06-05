'''
문자열 바꾸기
  replace(바꿀문자열, 새문자열)
'''
print(f"{'replace()':-^30}")
# 문자열에 replace 함수 사용
print('Hello, world!'.replace('world', 'Python'))
# 변수에 함수 사용
s = 'Hello, world!'
s = s.replace('Hello', '안녕')
print(s)

'''
문자바꾸기
  : maketrans(바꿀문자, 새문자)로 변환 테이블을 만든 후
  translate()로 적용한다.
'''
print(f"{'maketrans()/translate()':-^30}")
str1 = "apple"
# a는 1, e는 2 .. 와 같이 변경할 수 있는 변환테이블 생성
table = str1.maketrans('aeiou', '12345')
# 변환테이블을 문자열에 적용해서 변경
print(str1.translate(table))
# 한글도 영문과 동일하게 적용된다. '한'을 'X'로 변환한다.
str2 = "한글은 아름다운 언어"
table = str2.maketrans('한아언', 'XYZ')
print(str2.translate(table))

'''
문자열연결
  : 리스트로 주어진 요소들을 특정 구분자를 통해 연결한다.
''' 
print(f"{'join()':-^30}")
print('-'.join(['010', '7906', '3600']))

'''
공백 삭제 or 특정 문자 삭제
  : 인수로 삭제할 문자열 줄수있고, 인수가 없으면 공백을 삭제한다. 
''' 
print(f"{'strip()':-^30}")
str = "#^%오늘은 @@ 파이썬 @@ 공부하는날#^%"
# 좌측, 우측의 문자를 제거 
print(str.lstrip('#'))
print(str.rstrip('%'))
# 중간에 있는 문자는 replace 함수로 삭제해야한다.
print(str.rstrip('%').lstrip('#').replace('@', ''))

'''
문자열의 위치 찾기
  : 문자열을 찾은 후 인덱스를 반환해준다. strip() 함수처럼
  왼쪽부터 혹은 오른쪽부터 찾을 수 있다.
'''
print(f"{'find()':-^30}")
print('apple pineapple'.find('pl')) # 왼쪽부터 검색
print('apple pineapple'.rfind('pl')) # 오른쪽부터 검색

'''
문자열 상세 검사
  : 문자열에서 숫자, 알파벳, 한글만 있는 경우 True, 그 외의
  문자가 포함된 경우에는 False를 반환한다.
'''
print(f"{'isalnum()':-^30}")
str = 'python312좋아' 
print( str.isalnum() ) # True
str = 'python3.12좋아^^' 
print( str.isalnum() ) # False 

'''
퀴즈] 입력한 문자열에 영문대문자, 소문자, 숫자만 포함되어 있다면 True, 나머지 문자가 하나라도 
포함되면 False를 반환하는 프로그램을 작성하시오. 
isupper(), islower(), isdigit() 함수를 활용해서 작성하면 됩니다. 
'''
print(f"{'퀴즈()':-^30}")
s = input('문자열을 입력하세요:')
result = True
# 입력받은 문자열의 길이만큼 반복해서 한글자씩 인출
for ch in s:
  # 영문 대문자, 소문자, 숫자가 아닌 문자가 있는지 판단
  if not (ch.isupper() or ch.islower() or ch.isdigit()):
    # 한글자라도 아닌게 있으면 False로 변경
    result = False
    
print(f'입력한문자열:{s}')
print("결과:%s" % result)    

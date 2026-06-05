'''
집합(Set)
: 객체를 참조하기 위한 순서가 없는 집합자료형을 중복요소는 허용하지
않는다. 딕셔너리에서 Value를 제거하고, Key만 남은 상태로 보면된다.
선언 시 중괄호를 사용한다.
'''
# 함수를 통해 새로운 Set을 생성
empty_set = set
print(empty_set)

# 인수로 List를 전달하여 Set을 초기화
even_set = set([0,2,4,6,8])
print(even_set)

# 생성과 동시에 Set 초기화. 이때 중복값은 자동으로 제거됨.
odd_set = {1,3,5,7,9,7,5,3,1} 
print('중복제거', odd_set)
print('크기', len(odd_set))

# 새로운 Set 생성 및 초기화
myset = {1, 3, 5}

# 요소 추가
myset.add(7)
print("myset1", myset)

# 여러개의 요소 추가
myset.update({4, 6, 8})
print("myset2", myset)

# 요소 삭제
myset.remove(1)
print("myset3", myset)

# 전체 삭제
myset.clear()
print("myset4", myset)

# 집합 연산 가능
set_a = {1, 3, 5, 7, 9}
set_b = {1, 2, 5}
print("합집합", set_a | set_b) #{1, 2, 3, 5, 7, 9}
print("교집합", set_a & set_b) #{1, 5}
print("차집합", set_a - set_b) #{9, 3, 7}

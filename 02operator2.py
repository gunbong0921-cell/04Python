# 대입 연산자
a = tot = 10

# 복합 대입 연산자
a += 1
tot += a
print(a, tot)

# 최초 100, 200할당
v1, v2 = 100, 200
# 변수의 값을 서로 교환(Swap)할때 이와같이 간편하게 구현 가능
v2, v1 = v1, v2
print('변수교체', v1, v2)

# 5개의 값을 저장한 List를 선언한 후 초기화
mylist = [1,2,3,4,5]
# x1에는 1이 할당되고, 나머지는 x2에 할당된다.
x1, *x2 = mylist
print('패킹연산자1-1', x1, x2)

x1, x2, *x3 = mylist
print('패킹연산자1-2', x1, x2, x3)

# 1~4까지가 패킹되어 y1에 할당된다.
*y1, y2 = mylist
print('패킹연산자2-1', y1, y2)

*y1, y2,y3 = mylist
print('패킹연산자2-2', y1, y2, y3)
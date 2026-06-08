'''
정보은닉
 : 멤버변수의 외부 접근을 차단하고 클래스 내부에서만 접근하도록
 설정하는것을 말한다.
 파이썬에서는 private과 같은 접근지정자 대신, 더블언더바(__)를
 사용한다.
'''
class Computer:
  def __init__(self, name, passwd):
    # 외부 접근이 허용되는 멤버변수(public)
    self.name = name
    # 외부 접근이 차단되는 멤버변수(private)
    self.__passwd = passwd
  # 멤버함수 
  def hitKeyboard(self):
    return f"{self.name}로 키보드 작업을 합니다."
  def clickMouse(self):
    print(f"{self.name}로 마우스 클릭합니다.")
  # 정보은닉된 멤버변수에 접근하기 위한 getter/setter 정의 
  def getPasswd(self):
    return self.__passwd
  def setPasswd(self, passwd):
    self.__passwd = passwd
# 인스턴스 생성 
myCom = Computer("LG Gram", "qwer1234")
# 멤버함수 호출
print(myCom.hitKeyboard())
myCom.clickMouse()
# 외부접근이 허용되므로 정상 출력됨
print("컴퓨터이름:", myCom.name)

# private 이므로 접근할 수 없어 에러 발생
# AttributeError: 'Computer' object has no attribute '__passwd' 발생됨
# print("패스워드", myCom.__passwd)
# 접근이 안되므로 getter 함수를 통해 접근 후 출력해야함
print("패스워드", myCom.getPasswd())

# 패스워드 변경을 위해 setter를 호출
myCom.setPasswd("abcd9876")
print("패스워드 변경후1", myCom.getPasswd())

'''
맹글링 규칙에 의해 정보은닉된 멤버변수는 내부적으로 이름이
변경된다. 따라서 아래와 같이 작성하면 값이 변경되지 않는다. 또한
에러도 발생하지 않는다.
'''
myCom.__passwd = "xxxxXXXX"
print("패스워드 변경후2", myCom.getPasswd())

'''
정보은닉된 멤버변수는 아래와 같이 클래스명을 포함한 형태로
이름이 변경된다. 하지만 권장사항은 아니므로 사용하지 않는것이
좋다.
'''
# 권장되지 않음
print("맹글링규칙", myCom._Computer__passwd)

'''
open()
  : 파일을 다룰때 사용하는 내장함수로 첫번째 인자인 파일경로만
  필수사항이고 나머지는 선택사항(옵션)이다.
  형식] open(파일경로, mode, encoding)
    mode : 파일을 열때 사용하는 모드로
       W(쓰기), R(읽기), A(추가)가 있고
       b(2진모드), t(텍스트모드)로 파일의 형식을 지정할 수 있다.
'''
print("="*30)
print("내파일01.txt")
print("="*30)
'''
새로운 파일을 생성한 후 반복문으로 내용을 입력한다.
wt이므로 쓰시/텍스트 모드로 파일을 오픈한다.
'''
f_open = open("./saveFiles/내파일01.txt", mode="wt", encoding="utf-8")
# 20번 반복 실행
for i in range(1, 21):
  # 서식문자를 이용해서 문자열 구성
  data = "%d번째 줄입니다.\n" % i
  # 파일에 문자열을 입력한다.
  f_open.write(data)
# 반복문으로 모든 내용을 입력했다면 파일 객체를 닫아준다. 
f_open.close()

### 여기까지 실행하면 파일은 생성된다. ###

'''
파일을 읽기/쓰기 텍스트 모드로 오픈. 만약 파일이 해당 경로에 없다면
에러가 발생한다.
'''
f_read = open("./saveFiles/내파일01.txt", mode="rt", encoding="utf-8")
# 파일의 길이는 알 수 없으므로 무한루프로 구성
while True:
  # 파일의 내용을 한줄씩 읽음
  line = f_read.readline()
  # 더 이상 읽을 내용이 없다면 반복문을 탈출한다.
  if not line: break
  # 읽은 내용은 즉시 콘솔에 출력
  print(line)
# 작업을 마쳤다면 자원해제 
f_read.close()

# 기존 파일에 내용을 추가하기 위해 추가/텍스트 모드로 파일 오픈
f_add = open("./saveFiles/내파일01.txt", mode="at", encoding="utf-8")
# 한줄 추가(개행문자가 없으므로 줄바꿈은 되지 않음)
f_add.write("추가하는 내용니다.")
# 2개 이상의 문자열은 List를 통해 추가 가능
f_add.writelines(["줄바꿈은 되나요?\n", "안되면 개행문자를 넣어주세요."])
f_add.write("마지막 라인입니다.")
f_add.close()

print("="*30)
print("내파일02.txt")
print("="*30)
# 자동으로 파일객체를 open/close 할 수 있게 with~as를 사용
with open("./saveFiles/내파일02.txt", mode="wt", encoding="utf-8") as myfile:
  # 15줄의 문장을 입력하면 자동으로 close 된다.
  for i in range(1, 16):
    data = "%d라인 입력합니다.\n" % i
    myfile.write(data)
# 앞에서 생성된 파일을 읽기모드로 open한 뒤 내용 출력 
with open("./saveFiles/내파일02.txt", mode="rt", encoding="utf-8") as myfile:    
  line = None
  while line != "":
    line = myfile.readline()
    print(line.strip('\n'))   
    
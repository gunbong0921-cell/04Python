import pymysql

# 레코드 삭제를 위한 함수
def delete_record():
  conn = pymysql.connect(host='localhost', user='sample_user', password='1234',
          database='sample_db', charset='utf8', port=3306)
  curs = conn.cursor()
  # 무한루프 구성
  while True:
    iStr = input("삭제할일련번호(종료하려면 'exit' 입력):")
    # 대문자를 입력하더라도 하나의 조건으로 판단하기 위해 소문자로 변경 후 확인한다.
    if iStr.lower() == 'exit':
      print("프로그램을 종료합니다.")
      # 무한루프 탈출
      break
    # f-string 으로 쿼리문 작성
    sql = f"delete from board where num='{iStr}'"
    
    try:
      curs.execute(sql)
      conn.commit()
      print("1개의 레코드가 삭제됨")
    except Exception as e:
      conn.rollback()
      print("쿼리 실행시 오류발생:", e)
  # 함수 호출 후 delete 쿼리문 실행
  conn.close()
  
delete_record()        
  
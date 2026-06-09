import pymysql

conn = pymysql.connect(host='localhost', user='sample_user', password='1234',
          database='sample_db', charset='utf8', port=3306)
curs = conn.cursor()

# f-string을 통해 문자열 중간에 {}로 input() 함수 호출문장 삽입
sql = f"""INSERT INTO board (title, content, id, visitcount)
  VALUES ('{input('제목:')}', '{input('내용:')}', 'kosmo', 0)"""
try:
  # 쿼리문 실행
  curs.execute(sql)
  # 새로운 레코드가 입력되었으므로 commit() 함수 실행
  conn.commit()
  print("1개의 레코드가 입력됨")
except Exception as e:
  # 오류가 발생되면 롤백 처리
  conn.rollback()
  print("쿼리 실행시 오류발생", e)
  
# 모든 작업이 완료되면 자원해제 
conn.close()  
    
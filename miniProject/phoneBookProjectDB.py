import pymysql

conn = pymysql.connect(host='localhost', user='sample_user', password='1234',
                       database='sample_db', charset='utf8', port=3306)
curs = conn.cursor()
  
pList = [] 

while True:
    print("1.입력 2.출력 3.검색 4.수정 5.삭제 6.종료")
    
    try:
        no = int(input("선택: "))
    except ValueError:
        print("숫자만 입력해주세요.")
        continue
        
    if no == 1:
        print("{:-^50}".format("입력기능"))
        people = {}
        people["name"] = input("성명>>> ")
        people["phone"] = input("전화번호>>> ")
        people["addr"] = input("주소>>> ")
        
        sql = "INSERT INTO phonebook (name, phone, addr) VALUES (%s, %s, %s)"
        try:
            curs.execute(sql, (people["name"], people["phone"], people["addr"]))
            conn.commit()
            print("1개의 레코드가 입력됨")
        except Exception as e:
            conn.rollback()
            print("쿼리 실행시 오류발생", e)    
          
        print("주소 입력 완료")
        
    elif no == 2:
        print("{:-^50}".format("출력기능"))
        print("{:^3} {:^10} {:^15} {:^20}".format("번호","성명","전화","주소"))
        print("-"*53)
        
        sql = "SELECT * FROM phonebook ORDER BY idx DESC"
        curs.execute(sql)
        rows = curs.fetchall()
        for row in rows:
            print("{:^3} {:^10} {:^15} {:^20}".format(row[0], row[1], row[2], row[3]))
          
    elif no == 3:
        print("{:-^50}".format("검색기능"))
        name = input("검색할 이름: ")
        print("{:^3} {:^10} {:^15} {:^20}".format("번호","성명","전화","주소"))
        print("-"*53)
        
        sql = "SELECT * FROM phonebook WHERE name LIKE %s ORDER BY idx DESC"
        curs.execute(sql, (f"%{name}%",))
        rows = curs.fetchall()
        for row in rows:
            print("{:^3} {:^10} {:^15} {:^20}".format(row[0], row[1], row[2], row[3]))

    elif no == 4:
        print("{:-^50}".format("수정기능"))
        name = input("수정할 대상의 성명을 입력하세요: ")
        new_phone = input("새로운 전화번호: ")
        new_addr = input("새로운 주소: ")
        
        sql = "UPDATE phonebook SET phone=%s, addr=%s WHERE name=%s"
        try:
            curs.execute(sql, (new_phone, new_addr, name))
            conn.commit()
            if curs.rowcount == 0:
                print("수정할 이름이 존재하지 않습니다.")
            else:
                print(f"{curs.rowcount}개의 레코드가 수정됨")
        except Exception as e:
            conn.rollback()
            print("쿼리 실행시 오류발생", e)
          
    elif no == 5:
        print("{:-^50}".format("삭제기능"))
        name = input("삭제할 성명을 입력하세요: ")
        
        sql = "DELETE FROM phonebook WHERE name=%s"
        try:
            curs.execute(sql, (name,))
            conn.commit()
            if curs.rowcount == 0:
                print("삭제할 이름이 존재하지 않습니다.")
            else:
                print("1개의 레코드가 삭제됨")
        except Exception as e:
            conn.rollback()
            print("쿼리 실행시 오류발생:", e)  
        
    elif no == 6:
        print("{:-^50}".format("종료합니다."))
        break
    else:
        print("{:-^50}".format("번호를 잘못 입력하셨습니다."))
        
    print()

curs.close()
conn.close()
print("프로그램종료")
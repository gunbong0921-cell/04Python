import pandas as pd

# 데이터를 딕셔너리로 지정
data1 = {
  '이름' : [ '강백호', '서태웅', '채치수', '송태섭', '정대만'],
  '국어' : [ 100, 80, 90, 85, 95],
  '영어' : [ 80, 75, 60, 90, 80],
  '수학' : [ 90, 70, 55, 40, 80],
}

data2 = {
  '이름' : [ '알리스', '밥', '찰리', '데이비드', '이브'],
  '나이' : [ 25, 30, 28, 35, 27],
  '취미' : [ '독서', '등산', '요리', '사진 촬영', '게임'],
  '특기' : [ '피아노', '프로그래밍', '그림', '기타', '체스'],
  '생년월일' : [ '1998-03-15', '1993-07-22', '1995-01-10', '1988-11-02', '1996-06-18']
}
# 데이터프레임으로 변환 후 첫번째 컬럼인 '이름'을 인덱스로 지정
df1 = pd.DataFrame(data1)
df1.set_index('이름', inplace=True)
print(df1)
print('\n')

df2 = pd.DataFrame(data2)
df2.set_index('이름', inplace=True)
print(df2)
# 각 데이터프레임을  지정한 sheet에 저장
writer = pd.ExcelWriter("./saveFiles/sheetGubun.xlsx")
df1.to_excel(writer, sheet_name="sheet1")
df2.to_excel(writer, sheet_name="sheet2")
# sheet를 지정한 후 저장시에는 _save() 함수를 추가로 실행한다.
writer._save()
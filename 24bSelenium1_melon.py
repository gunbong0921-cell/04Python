# 셀레니움에서 웹드라이버 임포트
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd  # 임포트는 상단에 모아두는 것이 좋습니다.

# 크롬 로드. 이때 웹브라우저가 실행된다.
driver = webdriver.Chrome()

'''
셀레니움은 크롬 브라우저를 이용해서 크롤링 할 페이지를 띄운 후 데이터를
얻어온다. 이때 비동기 통신을 통해 데이터를 로드하는 경우 조금 늦게 로딩되는
경우가 있으므로, 셀레니움에서는 '암묵적대기'가 필요한 경우가 있다.
이런 경우 5초까지는 대기하겠다는 선언이다.
'''
driver.implicitly_wait(5)

# 멜론차트 페이지 크롤링을 위해 URL설정
url = 'https://www.melon.com/chart/index.htm'
# 셀레니움을 통해 페이지의 데이터(HTML원본소스)를 얻어온다.
driver.get(url)
html = driver.page_source

# 브라우저 작업이 끝났으므로 닫아줍니다. (자원 관리)
driver.quit()

# 뷰티풀숩을 임포트 한 후 얻어온 데이터를 Soup개체로 변환
soup = BeautifulSoup(html, 'html.parser')

# 파싱한 정보(순위, 곡 등)을 저장할 리스트 생성
song_data = []
rank = 1

# 셀렉터를 이용해서 반복되는 엘리먼트 <tr>을 얻어온다.
songs = soup.select('tbody > tr')

# 얻어온 갯수만큼 반복
for song in songs:
    try:
        # 노래제목
        title = song.select('div.ellipsis.rank01 > span > a')[0].text
        
        # 가수 (여러 명일 수 있으므로 해당 div 안의 모든 텍스트를 가져오거나 첫 번째 <a> 태그 지정)
        singer = song.select('div.ellipsis.rank02 > a')[0].text
        
        # 좋아요 갯수
        favo = song.select('td:nth-child(8) > div > button > span.cnt')[0].text
        # 좋아요 수 뒤에 붙는 '총건수' 글자나 공백 제거 및 줄바꿈 정리
        favo = favo.replace('총건수', '').strip()
        
        # 파싱한 내용을 콘솔에 출력해서 확인
        print(f"{rank}위 | {title} | {singer} | {favo}")
        
        # 리스트에 데이터 추가 (총 5개 데이터)
        song_data.append(['Melon', rank, title, singer, favo])
        
        # 순위는 1씩 증가
        rank += 1
    except IndexError:
        # 멜론 차트 테이블 안의 광고나 빈 행 처리를 위한 예외처리
        continue

# --- [주의] 여기서부터는 for문 바깥입니다. 반복이 모두 끝난 후 실행됩니다. ---

# 컬럼명 추가를 위해 리스트 생성 (데이터 개수 5개와 일치하도록 '가수' 추가)
columns = ['서비스', '순위', '타이틀', '가수', '좋아요']

# 데이터프레임으로 변환 시 앞에서 작성한 컬럼을 적용
pd_data = pd.DataFrame(song_data, columns=columns)

# 데이터프레임의 상위 5개 행을 출력해서 확인
print("\n--- 데이터프레임 상위 5개 행 ---")
print(pd_data.head())

# 엑셀로 저장 (saveFiles 폴더가 미리 생성되어 있어야 합니다)
import os
if not os.path.exists('./saveFiles'):
    os.makedirs('./saveFiles')

pd_data.to_excel('./saveFiles/melon_Chart.xlsx', index=False)
print("\n엑셀 파일 저장 완료!")
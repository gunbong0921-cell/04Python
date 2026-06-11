#셀레니움 임포트
from selenium import webdriver
#크롬 드라이버를 로드
driver = webdriver.Chrome()
#잠시 대기를 위해 time 모듈을 임포트
import time
#네이버로 접속
url = 'https://www.naver.com'
driver.get(url)
#5초간 대기 후 자동으로 창이 닫힘
time.sleep(5)
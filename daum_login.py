#셀레니움 모듈과 드라이버 로드
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


#셀레니움의 크롬 드라이버 로드
driver = webdriver.Chrome()
 
#다음 접속
url = 'https://www.daum.net/'
driver.get(url)


driver.find_element(By.XPATH, '//*[@id="loginMy"]/div/div[1]/div/a').click()
time.sleep(2)


driver.find_element(By.NAME, 'loginId').send_keys('gunbong1984@gmail.com')
time.sleep(2)
driver.find_element(By.NAME, 'password').send_keys('ldyjah42&')
time.sleep(2)
#입력을 마친 후 로그인 버튼을 클릭한다.
driver.find_element(By.XPATH, '//*[@id="mainContent"]/div/div[1]/form/div[4]/button[1]').click()
time.sleep(30)


driver.find_element(By.NAME, 'q').send_keys('비트코인')
time.sleep(2)


driver.find_element(By.CLASS_NAME, 'btn_ksearch').click()
time.sleep(10)
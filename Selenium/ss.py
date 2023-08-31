from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
# import time

options = Options()
options.add_experimental_option('detach', True) # 브라우저 바로 닫힘 방지

service = Service(ChromeDriverManager().install())

print(service)

driver = webdriver.Chrome(service=service, options=options)

driver.get('https://naver.com')


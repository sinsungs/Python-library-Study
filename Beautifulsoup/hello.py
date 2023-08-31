print('beautifulsoup')

from bs4 import BeautifulSoup
import requests

url = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query="

keyword = input("검색어를 입력하세요 : ")

search_url = base_url + keyword

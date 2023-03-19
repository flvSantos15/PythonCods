import time
# import requests
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import json

# 1. Pegar conteúdo HTML a partir da URL
url = "https://stats.nba.com/players/traditional/?PerMode=Totals&Season=2019-20&SeasonType=Regular%20Season&sort=PLAYER_NAME&dir=-1"

option = Options()
option.headless = True
driver = webdriver.Chrome(options=option)

driver.get(url)
time.sleep(10)

driver.find_element_by_xpath(
    "//div[@class='nba-stat-table']//table//head//tr//th[@data-field='PTS']").click()


# 2. Parsear o conteúdo HTML - BeaultifulSoup
# 3. Estruturar conteúdo em um Data Frame - Pandas
# 4. Transformar os Dados em um Dicionário
driver.quit()
# 5. Converter e salvar em um arquivo JSON

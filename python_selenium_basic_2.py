#coding=utf-8

'''
use selenium to search the specific stock status,
then parse the html result with beautifulsoup,
the result are the every-day stock price, 
mean price, max price, min price of the month.
'''

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import Select # 下拉式選單
from webdriver_manager.chrome import ChromeDriverManager # 自動安裝webdriver
import time
import os

#print(中文)
import io
import sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

wd = os.getcwd()

class Stock:
    def __init__(self, *stock_numbers): #tuple can store several parameter
        self.stock_numbers = stock_numbers
    def daily(self, month, year):
        ##############################################
        ### make the specific search with selenium ###
        ##############################################
        browser = webdriver.Chrome(ChromeDriverManager().install())
        browser.get("https://www.twse.com.tw/zh/page/trading/exchange/STOCK_DAY_AVG.html")
        select_year = Select(browser.find_element_by_name("yy"))
        select_year.select_by_value(year)
        select_month = Select(browser.find_element_by_name("mm"))
        select_month.select_by_value(month)
        stock_no = browser.find_element_by_name("stockNo")

        ###################################################
        ### parse the search result with beautiful soup ###
        ###################################################

        ''' parse only one specific stuck number '''
        stock_no.send_keys("2412")
        stock_no.submit()
        time.sleep(1)
        soup = BeautifulSoup(browser.page_source, features="lxml")
        table = soup.find("table", {"id": "report-table"})
        elements = table.find_all("td", {"class": "dt-head-center dt-body-center"})
        data = [element.getText() for element in elements]

        ''' parse several stuck number automatically '''
        result = []
        for stock_number in self.stock_numbers:
            stock_no.clear()
            stock_no.send_keys(stock_number)
            stock_no.submit()
            time.sleep(1)
            soup = BeautifulSoup(browser.page_source, features="lxml")
            table = soup.find("table", {"id": "report-table"})
            elements = table.find_all("td", {"class": "dt-head-center dt-body-center"})
            data = (stock_number,) + tuple(element.getText() for element in elements)
            stock_value = [data[i] for i in range(2, len(data), 2)]
            max_value = max(stock_value)
            min_value = min(stock_value)
            data = data + ("月最高價", max_value, "月最低價", min_value)
            result.append(data)
        browser.close()
        return result
stock_dict = {"2412": "中華電信", "2330": "台積電"}
stock_obj = Stock("2412", "2330")
stock_result = stock_obj.daily("1", "2021")
for stock_no in stock_result:
    print("stock: " + stock_no[0] + ", " + stock_dict[stock_no[0]])
    for data_no in range(1,len(stock_no),2):
        print(stock_no[data_no] + ", " + stock_no[data_no+1])
import scrapy
from scrapy.http import Request
from bs4 import BeautifulSoup

# from PrettyGirl.items import PrettygirlItem
# from PrettyGirl import settings

# from selenium import webdriver
import time
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import os


class MySpider(scrapy.Spider):
    name = 'PrettyGirl'
    allowed_domains = ['jandan.net']
    base_url = 'http://jandan.net/ooxx/'
    baseurl = '.html'
    headers = {
        "User-Agent":
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36",
        "Accept":
        "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"
    }

    def start_requests(self):
        yield Request(self.base_url, self.parse_urls, headers=self.headers)

    def parse_urls(self, response):
        soup = BeautifulSoup(response.text, 'lxml')
        imgs_url = soup.find_all('img')
        imgs_hash = soup.find_all('span', attrs={'class': ['img-hash']})

        f = open('D:\py\PeriPicture\PeriPicture.txt', 'a', encoding='utf-8')
        f.write(response.text)
        f.close()

        print(soup)
        return None

    def parse(self, response):
        print('sss')
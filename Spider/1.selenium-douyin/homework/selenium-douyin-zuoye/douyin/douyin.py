import time
from openpyxl import Workbook
from lxml import etree
from douyin.webbrowser import *


class DY:
    def __init__(self):
        self.driver = DriverCreate()
        self.driver.browser.get(self.driver.url)

    def close_login(self):
        self.driver.browser.implicitly_wait(5)
        close = self.driver.browser.find_element(By.CLASS_NAME, 'dy-account-close')
        close.click()

    def go_to_bottom(self):
        for i in range(10):
            self.driver.browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')
            time.sleep(1)

    def parse(self):
        wb = Workbook()
        ws1 = wb.create_sheet('数据', 0)
        ws1.append(['视频名字', '点赞数', '链接地址'])
        html = self.driver.browser.page_source
        ret = etree.HTML(html)
        person_name = ret.xpath('//*[@id="douyin-right-container"]/div[2]/div/div/div[1]/div[2]/div[1]//text()')[0]
        fans = ret.xpath('//*[@id="douyin-right-container"]/div[2]/div/div/div[1]/div[2]/div[3]/div[2]/div[2]/text()')[
            0]
        videos_list = ret.xpath('//*[@id="douyin-right-container"]/div[2]/div/div/div[2]/div[2]/div[2]/div[2]/ul//li')
        for li in videos_list:
            video_href = 'https://www.douyin.com' + li.xpath('./a/@href')[0]
            tittle = li.xpath('./a/p/text()')[0]
            likes = li.xpath('./a//span//text()')[0]
            ws1.append([tittle, likes, video_href])
            print(tittle, likes, video_href)
        wb.save(f'{person_name}_{fans}.xlsx')
        self.driver.browser.close()

    def run(self):
        try:
            self.close_login()
            self.go_to_bottom()
            self.parse()
        except:
            self.go_to_bottom()
            self.parse()

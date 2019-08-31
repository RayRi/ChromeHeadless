#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

from config.settings import DRIVER_PATH, DATA_PATH

init_url = "http://txzb.miit.gov.cn/DispatchAction.do?efFormEname=POIX14&pagesize=11"

class Login(webdriver.Chrome):
    def __init__(self, path=DRIVER_PATH, wait_times=30, time_out=5, headless=True):
        options = webdriver.ChromeOptions()
        # set headleass driver
        if headless:
            options.add_argument("headless")
        
        super(Login, self).__init__(executable_path=path, options=options)
        self.implicitly_wait(time_to_wait=wait_times)
        self.init_handle = self.window_handles[0]

    def __articles(self):
        # 获取到所页面的链接==>不断点击切换窗口==>保存页面内容==>关闭窗口==>再切换回原窗口
        pages = self.find_elements_by_xpath("//table[@id='newsItem']//a")
        
        for page in pages:
            page.click()
            self.switch_to.window(self.window_handles[-1])
            page_title = self.find_element_by_xpath('//*[@id="ef_region_inqu"]/div[1]/table/tbody/tr[1]/td')
            title = page_title.text
            with open(os.path.join(DATA_PATH, title+".html"), "w") as file:
                file.write(self.page_source)
            # close window
            self.close()
            # switch to origin window
            self.switch_to.window(self.init_handle)

    def parse_pages(self):
        # load first page
        self.get(init_url)

        # 一直点击下一页，当遇见下一页中有 span 元素时终止循环
        next_available = True
        while next_available:
            # parse articles
            self.__articles()
            time.sleep(4)
            # get next page
            next_page = self.find_elements_by_xpath("//td[@align='middle']")[2]
            # check the next page is validate
            try:
                next_page.find_element_by_tag_name('span')
                next_available = False
            except NoSuchElementException:
                next_page.click()
                time.sleep(60)
                
        # driver quit
        self.quit()

if __name__ == "__main__":
    test = Login()
    test.parse_pages()
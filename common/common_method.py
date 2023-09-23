# -*- encoding: utf-8 -*-
"""
@File    : util.py
@Time    : 2022/09/24 15:44:41
@Author  : DINGHAO
@Contact : 1562592517@qq.com
@Version : 1.0
@License : Apache License Version 2.0, January 2021
@Desc    : 存放公共方法
---------------------------------------------------
"""



import time
from typing import Union
import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select


class Method():


    def open_browse(self,url,driver):
        """打开对应的url
        Args:
            url (_type_): url
        """
        driver.maximize_window()
        driver.get(url = url)

    def locate(self,name,value,driver):
        """定位元素
        Args:
            name (_type_): 定位方法
            value (_type_): 值
        Raises:
            e: _description_
        Returns:
            _type_: 返回定位到的元素
        """
        try:
            wait = WebDriverWait(driver, timeout=10, poll_frequency=0.5)
            method = EC.visibility_of_element_located((name,value))
        except Exception as e:
            print(e)
        else:
            ele = wait.until(method = method,message = f'超时了,未能定位到{name}元素')
            return ele

    def input(self,name,value,text,driver):
        """定位到元素后,执行send_keys方法,输入内容
        Args:
            name (_type_): 定位方法
            value (_type_): 值
            text (_type_): 输入内容
        """
        ele = self.locate(name = name ,value = value,driver=driver)
        ele.clear()
        ele.send_keys(text)

    def click(self,name,value,driver):
        """定位元素后,执行click方法(鼠标左击)
        Args:
            name (_type_): 定位方法
            value (_type_): 值
        """
        ele = self.locate(name,value,driver)
        ele.click()

    @staticmethod
    def sleep(sec:float):
        """强制等待
        Args:
            sec (float): 等待时间
        """
        time.sleep(sec)

    def implicitly_sleep(self,sec:float,driver):
        """隐式等待,设置一次,全局生效
        Args:
            sec (_type_): 等待时间
        """
        driver.implicitly_wait(sec)
    
    def quit(self,driver):
        """关闭浏览器和driver
        """
        driver.quit()

    @staticmethod
    def execute_script(js ,driver):
        """执行js语句
        """
        driver.execute_script(js)

    def scroll_to_target_and_click(self,name,value,driver):
        """滑动滚动条到目标元素并点击
        """
        tar = self.locate(name,value,driver)
        js = "arguments[0].scrollIntoView();"
        driver.execute_script(js,tar)
        self.click(name,value,driver)
  
    def selector_by_value(self,name,value,t_value,driver):
        """通过值定位下拉框选项,必须是select标签
        Args:
            name (_type_): 定位方式
            value (_type_): 值
            sel_ (_type_): 下拉框选项的值
        """
        select = Select(sel=None)
        ele = self.locate(name = name,value = value,driver=driver)
        ele.click()
        select(ele).select_by_value(t_value)

    def switch_window(self,index,driver):
        """all_w为列表,根据下标切换窗口,-1为最新打开的窗口"""
        all_w = driver.window_handles
        driver.switch_to.window(all_w[index])

    def find_elements_by_index_and_click(self,name,value,index,driver):
        """返回列表,根据下标选择元素并单击"""
        try:
            ele = driver.find_elements(name,value)[int(index)]
            if ele.is_displayed():
                ele.click()
        except Exception as e:
            print(e)

    def find_elements_by_index_and_input(self,name,value,index,text,driver):
        """返回列表,根据下标选择元素并输入内容"""
        try:
            ele = driver.find_elements(name,value)[int(index)]
            if ele.is_displayed():
                ele.clear()
                ele.send_keys(text)
        except Exception as e:
            print(e)

    def screenshot_func(self, file: Union[str], driver):
        """截图函数"""
        try:
            driver.get_screenshot_as_file(file)
        except Exception as e:
            print(e)
    







        


#-*- encoding: utf-8 -*-
"""
@File    : test_sales
@Time    : 2022/10/11 20:00
@Author  : DINGHAO
@Contact : 1562592517@qq.com
@Version : 1.0
@License : Apache License Version 2.0, January 2021
@Desc    : 创建线索
-----------------------------------------------------
"""

import logging

import allure
import pytest
from common.common_method import Method
from tool import get_parent_dir, yaml_read

file = get_parent_dir+r'\data'+r'\sales.yaml'
file_data= yaml_read(file=file)
log = logging.getLogger(__name__)



@allure.feature('crm系统')
@allure.story('参数化实现创建线索')
@allure.severity('normal')
@allure.issue('https://www.tapd.cn/',name='TAPD')
@pytest.mark.parametrize(argnames='data',argvalues=file_data)
def test_create_sales(gd,test_login,data):
    """成功创建线索"""
    allure.dynamic.title(f'创建手机号为{data["phone_number"]["text"]}的线索')
    allure.dynamic.tag('登录')
    m = Method()
    #点击crm图标,进入crm系统
    log.info('定位{}元素,点击{}'.format(*data["crm"].values()))
    with allure.step('定位{}元素,点击{}'.format(*data["crm"].values())):
        m.click(**data['crm'],driver=gd)
    #切换窗口
    m.sleep(0.5)
    with allure.step('切换窗口'):
        m.switch_window(-1,gd)
    m.sleep(3)
    log.info('定位{}元素,点击{}'.format(*data["sales_management"].values()))
    # 点击线索管理
    m.click(**data['sales_management'],driver=gd)
    # 点击创建线索按钮
    m.click(**data['create_sales'],driver=gd)
    # 当前在主页,需要切换到创建线索页面
    m.switch_window(-1,gd)
    # 输入手机号
    m.sleep(0.5)
    m.input(**data['phone_number'],driver=gd)
    # 点击创建线索按钮
    m.sleep(0.3)
    m.click(**data['click_create_butt'],driver=gd)
    m.sleep(1)
    # 输入姓名
    m.find_elements_by_index_and_input(**data['customer'],driver=gd)
    m.sleep(0.2)
    # 点击一级渠道输入框,选择门店线下自拓
    m.click(**data['first_source'],driver=gd)
    m.execute_script(**data['first_source_value'],driver=gd)
    m.sleep(0.2)
    # 点击二级渠道输入框,选择地推
    m.click(**data['second_source'], driver=gd)
    m.sleep(0.1)
    m.click(**data['second_source_value'], driver=gd)
    m.sleep(0.2)
    # 点击三级渠道输入框,选择公共场所地推
    m.click(**data['third_source'], driver=gd)
    m.sleep(0.1)
    m.click(**data['third_source_value'], driver=gd)
    m.sleep(0.2)
    #点击意向并选择高意向
    m.click(**data['intention'],driver=gd)
    m.click(**data['intention_v'],driver=gd)
    #选择第一个客户经理
    m.sleep(0.1)
    m.click(**data['customer_manager'],driver=gd)
    m.execute_script(**data['customer_manager_v'],driver=gd)
    #选择第一个小区
    m.sleep(0.1)
    m.click(**data['commuinty'],driver=gd)
    m.execute_script(**data['community_v'], driver=gd)
    #输入门牌号
    m.input(**data['house_number'],driver=gd)
    #点击省下拉框并选择省
    m.sleep(0.2)
    m.click(**data['provinces'],driver=gd)
    m.execute_script(**data['provinces_v'],driver=gd)
    #选择市
    m.sleep(0.2)
    m.execute_script(**data['city_v'],driver=gd)
    # 选择区
    m.sleep(0.3)
    m.execute_script(**data['area_v'], driver=gd)
    #是否是区县客资
    m.sleep(0.1)
    m.find_elements_by_index_and_click(**data['customer_type'], driver=gd)
    #选择房屋类别
    m.sleep(0.2)
    m.execute_script(**data['community_type'],driver=gd)
    m.execute_script(**data['community_type_v'], driver=gd)
    # 是否期房
    m.sleep(0.1)
    m.find_elements_by_index_and_click(**data['qifang'], driver=gd)
    #选择房屋结构
    m.sleep(0.2)
    m.execute_script(**data['community_structure'], driver=gd)
    m.execute_script(**data['community_structure_v'], driver=gd)
    # 选择装修性质
    m.sleep(0.2)
    m.execute_script(**data['decoration_nature'], driver=gd)
    m.execute_script(**data['decoration_nature_v'], driver=gd)
    #输入面积
    m.sleep(0.3)
    m.input(**data['area'],driver=gd)
    # 输入几室
    m.sleep(0.1)
    m.execute_script(**data['room'], driver=gd)
    # 输入几厅
    m.execute_script(**data['hall'], driver=gd)
    # 输入几厨
    m.execute_script(**data['kitchen'], driver=gd)
    # 输入几卫
    m.execute_script(**data['toilet'], driver=gd)
    # 输入几阳台
    m.execute_script(**data['balcony'], driver=gd)
    #点击取消/确定按钮
    m.find_elements_by_index_and_click(**data['cancel_or_confirm'],driver=gd)










# -*- encoding: utf-8 -*-
# '''
# @File    : test_demo.py
# @Time    : 2022/09/23 21:44:07
# @Author  : DINGHAO
# @Contact : 1562592517@qq.com
# @Version : 1.0
# @License : Apache License Version 2.0, January 2021
# @Desc    : None
# ---------------------------------------------------
# '''

import logging
import pytest
from string import Template
from tool import yaml_read
log = logging.getLogger(__name__)

class Test_one:

    __name__ = 'dh'
    
    '''
    def setup_class(self):
        print('***每个类运行前执行一次')

    def teardown_class(self):
        print('***每个类运行后执行一次')

    def setup_method(self):
        print('***每个方法运行前执行一次')

    def teardown_method(self):
        print('***每个方法运行后执行一次')

    def setup(self):
        print('***每个方法运行前执行一次')

    def teardown(self):
         print('***每个方法运行后执行一次')
    '''
    #@pytest.mark.usefixtures('ff')
    #@pytest.mark.skip('666')
    # def test_add(self,x=2,y=3):
    #     assert x!=y
    
    #@pytest.mark.usefixtures('ff')
    #@pytest.mark.parametrize("name,age",[['dh',15],['df',22]])
    # def test_try(self,name,age):
    #     print(f'{name}--{age}')
    
    # data = [{'methord':'xpath'},{'value':'//[@class="input"]'}]
    # @pytest.fixture(scope='class',name='f3',params=data)
    # def test3(self,request):
    #     return request.param.get('value')
    
    # def test4(self,f3):
    #     print(f3)
    



    # @pytest.fixture
    # def test_4(self,request):
    #     res = f'当前登录的是{request.param[1]}'
    #     print(res)
    #     yield request
    #     print('over')
    #
    #
    # @pytest.mark.parametrize('test_4',[('dh','17826185420'),('dd',18896608505)],indirect=True)
    # def test_6(self,test_4):
    #     print(test_4.node)

    # @pytest.fixture()
    # def get(self,pytestconfig):
    #     return pytestconfig.getini('log_file')
    #
    # def test_get_config(self,get):
    #     print('返回的是',get)

    # @pytest.fixture()
    # def test_fixture_ini(self,pytestconfig):
    #     url = pytestconfig.getoption('--url')
    #     return url

    # def test_(self,test_fixture_ini):
    #     print(test_fixture_ini)
def test_1():
    print(666)
    log.info('whaha')


if __name__ == '__main__':
    pytest.main(['-sq','pytest_demo.py'])




    


   


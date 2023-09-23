import os
import shutil
from configparser import ConfigParser, NoOptionError, NoSectionError
from string import Template

import yaml
from webdriver_manager.microsoft import EdgeChromiumDriverManager


class Config:
    def __init__(self, file, encoding='utf-8') -> None:
        self.conf = ConfigParser()
        self.conf.read(filenames=file, encoding=encoding)

    def get_option_value(self, section=None, option=None):
        """返回给定section下option的值
        Args:
            section (_type_, optional): 节点名称 Defaults to None.
            option (_type_, optional): 选项名称 Defaults to None.
        """
        try:
            self.conf.has_option(section=section, option=option)
            value = self.conf.get(section=section, option=option)
            return value
        except (NoOptionError,NoSectionError) as e:
            print(e)

    def get_default_value(self):
        """获取默认的节点的值
        """
        value = self.conf.defaults()
        if len(value) ==0:
            return '未设置DEFAULT节点'
        else:
            return value


def yaml_read(file: str):
    '''读取yaml文件并返回数据'''
    try:
        with open(file=file, mode='r+',encoding='utf-8') as file:
            data = yaml.safe_load(stream=file)
            return data
    except FileNotFoundError as e:
        print(e)


def get_parent_dir():
    """返回路径"""
    base_dir = os.getcwd()
    return  base_dir

get_parent_dir=get_parent_dir()

def download_driver():
    """自动下载Edge驱动,并移动到python目录下"""
    try:
        package = EdgeChromiumDriverManager().install()
    except Exception as e:
        raise e
    else:
        src = os.path.abspath(package)
        shutil.copyfile(src=src,dst=r'D:\python\Scripts\msedgedriver.exe')
#download_driver()

def template(tem:str,**data):
    """设置模板进行值传递"""
    try:
        if not isinstance(tem,str):
            new_tem = repr(tem)
        else:
            new_tem = tem
    except Exception as e:
        raise e
    else:
        if data:
            templates = Template(new_tem).safe_substitute(data)
            return templates
        else:
            return new_tem


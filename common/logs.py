# -*- encoding: utf-8 -*-
"""
@File    : logs.py
@Time    : 2022/04/05 16:45:37
@Author  : DING HAO
@Contact : 17826185420
@Version : 1.0
@License : Apache License Version 2.0, January 2021
@Desc    : 日志模块
"""
import logging
import pathlib
from tool import config, path

# 读取配置文件
file = path.parent_dir.joinpath('conf.config')
conf = config(file=file)
# 处理器名称FileHandler或者StreamHandler
name = conf.get_value('LOG', 'handler')
# 日志等级,当前为info
level = conf.get_value('LOG', 'level')
# 日志名称
log_file = conf.get_value('LOG', 'log_file')



class log:

    #日志格式
    formatter = '>> %(asctime)s>> %(filename)s >>%(name)s>> 第%(lineno)d行>> %(levelname)s>> %(message)s'

    def __init__(self):
        self.name = name
        self.level = level
        self.log_file = log_file
        try:
            self.p = pathlib.WindowsPath(path.parent_dir, 'log', self.log_file)
            if self.p.exists():
                pathlib.WindowsPath(path.parent_dir, 'log').mkdir(exist_ok=True)
            else:
                pathlib.WindowsPath(path.parent_dir, 'log').mkdir()
                self.p.touch()
            self.logger = logging.getLogger(__name__)  # 创建日志器
            self.logger.setLevel(self.level)  # 设置日志器的等级info
            self.sh = getattr(logging, self.name)(self.p)  # 反射创建处理器,控制台/文件处理器
        except:
            raise FileExistsError('%s:文件已存在' % self.p)
        else:
            self.fr = logging.Formatter(self.formatter)  # 设置格式器
            self.sh.setFormatter(fmt=self.fr)  # 给处理器添加格式
            self.logger.addHandler(self.sh)  # 给日志器添加处理器

    def debug(self, message):  # 打印debug级别的日志
        self.logger.debug(message)

    def info(self, message):  # 打印info级别的日志
        self.logger.info(message)

    def warn(self, message):  # 打印warn级别的日志
        self.logger.warning(message)

    def error(self, message):  # 打印error级别的日志
        self.logger.error(message)

    def critical(self, message):  # 打印critical级别的日志
        self.logger.critical(message)


import allure
import pytest
from common.common_method import Method
from selenium import webdriver
from tool import Config, get_parent_dir, yaml_read

#读取配置文件
file = 'config.cfg'
conf = Config(file=file)
#驱动
type_driver = conf.get_option_value('DRIVER',option='driver')
#登录数据
login_data = get_parent_dir+r'\data'+r'\login.yaml'
#测试url
url = conf.get_option_value('ENV',option='env')


@allure.title(f'返回当前浏览器驱动为:{type_driver}')
@pytest.fixture(scope='session',name='gd')
def test_driver():
    '''根据上面option选择driver,默认是Edge'''
    try:
        driver = getattr(webdriver, type_driver,'Edge')()
    except Exception as e:
        print(e)
    else:
        yield driver
        driver.quit()


@allure.title('接收登录的数据给test_login使用')
@pytest.fixture(params=yaml_read(file=login_data))
def login_data(request):
    """返回登录的数据给test_login使用"""
    return request.param

@allure.title('登录门店系统')
@pytest.fixture(scope='function',name='test_login')
def test_login(gd,login_data):
    """登录操作"""
    m = Method()
    #将数据进行拆分,结合yaml的锚点与引用实现单用例参数化
    data,account,password,store = login_data.values()
    #打开网站
    m.open_browse(url=url,driver=gd)
    #输入登录账号
    m.input(**data['USERNAME'],text=account, driver=gd)
    #输入密码
    m.input(**data['PWD'],text=password,driver=gd)
    #点击登录按钮
    m.click(**data['BUTTON'],driver=gd)
    #点击门店按钮
    m.click(**data['SOMS_BUTT'],driver=gd)
    #点击下一步
    m.click(**data['NEXT_STEP'],driver=gd)
    m.sleep(0.2)
    #滑动滚动条到目标门店并点击
    m.scroll_to_target_and_click(**data['SELECTED_SOMS'],value=store,driver=gd)
    m.sleep(0.3)
    #滑动滚动条到进入按钮并点击
    m.scroll_to_target_and_click(**data['ENTER'],driver=gd)
    m.sleep(4)
    #断言并截图
    assert data['assert'] in gd.title
    m.screenshot_func(file=get_parent_dir+'/screenshot'+'/登录成功.png',driver=gd)
    allure.attach.file(source=get_parent_dir+'/screenshot'+'/登录成功.png',\
                       name='登录成功',attachment_type=allure.attachment_type.PNG)
    m.sleep(1)

def pytest_addoption(parser):
    """添加命令行参数/ini配置参数"""
    parser.addoption("--url",action="store",help="测试环境：test or online",default='md.test.jtljia.net')
    parser.addini(name='url', type=None, help='测试环境:test or online', default='test')








#抓取求职信息

# selenium:模拟人类操作浏览器抓取数据
# 1.安装selenium：pip install 
# 2.下载安装浏览器驱动：如chromedriver,得匹配本地浏览器版本
# 3.把浏览器驱动放到python.exe解释器所在文件夹
# 4.让selenium启动谷歌浏览器
# from selenium.webdriver import firefox #火狐驱动
from selenium.webdriver import Chrome  #谷歌驱动
from selenium.webdriver.common.by import By  #find_element_by_*语法已弃用。需要导入by依赖
from selenium.webdriver.common.keys import Keys

import time

# 1.创建浏览器对象
web=Chrome()

# 2.打开一个网址
web.get('https://www.lagou.com/')

# 3.找到需要点击的元素的xpath(By.ID /By.CLASS_NAME 也都可以)
el=web.find_element(By.XPATH,r'//*[@id="changeCityBox"]/p[1]/a')
el.click() #点击，在地区选择中 选中’全国‘

time.sleep(1)
#输入搜索关键字’python‘+点击搜索
input=web.find_element(By.XPATH,r'//*[@id="search_input"]').send_keys('python',Keys.ENTER)

time.sleep(5)   #浏览器等一下页面加载，再开始抓取
# 岗位卡片
job_list=web.find_elements(By.XPATH,r'//*[@id="jobList"]/div[1]/div[@class="item__10RTO"]')
for job in job_list:
    # 岗位名字
    job_name=job.find_element(By.CLASS_NAME,'p-top__1F7CL').find_elements(By.TAG_NAME,'a')[0].text
    # 企业
    job_company=job.find_element(By.CLASS_NAME,'company-name__2-SjF').find_elements(By.TAG_NAME,'a')[0].text
    # 薪酬
    job_price=job.find_element(By.CLASS_NAME,'money__3Lkgq').text
    print(job_name,job_company,job_price)
# 抓取子页面数据后关闭子页面
# 拉勾网为例
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By #by依赖
from selenium.webdriver.common.keys import Keys #键盘输入

import time
web=Chrome()
web.get('https://www.lagou.com/')


web.find_element(By.ID,'cboxClose').click()
time.sleep(1)

web.find_element(By.ID,'search_input').send_keys('python',Keys.ENTER)
time.sleep(3)

web.find_elements(By.CLASS_NAME,'item__10RTO')[0].click()

# 浏览器切换到新打开的子页面 window_handles=选项卡，-1=最后一个
web.switch_to.window(web.window_handles[-1])

# 抓取新窗口中的描述部分
job_detail=web.find_element(By.CLASS_NAME,'job_detail').text
print(job_detail)

# 提取成功后，关闭子页面
web.close()
# 返回第一个页面
web.switch_to.window(web.window_handles[0])

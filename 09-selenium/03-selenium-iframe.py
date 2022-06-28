# selenium 切换selenium
#91看剧网为例
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By #by依赖
from selenium.webdriver.common.keys import Keys #键盘输入

import time

web=Chrome()
web.get('http://www.91kanju.com/vod-play/54194-2-1.html')

time.sleep(3)
ifram=web.find_element(By.XPATH,'//*[@id="player_iframe"]')
# print(ifram.get_attribute('id'))
web.switch_to.frame(ifram)
time.sleep(10)
# # web.switch_to.default_content() # 切回原页面
print(web.find_element(By.XPATH,'//*[@id="sub-frame-error-details"]').text)
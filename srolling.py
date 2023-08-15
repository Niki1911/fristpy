import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver= webdriver.Chrome()
driver.get('https://unsplash.com/')
# driver.maximize_window()
# driver.find_element(By.CLASS_NAME,'w3-col l10 m12')
# y=1000
# for step in range (0,10):
#  driver.execute_script("window.scroll(0,"+str(y)+")")
#  y+=1000
#  time.sleep(20)

driver.execute_script("window.scrollTo(0,1000)")

time.sleep(2)
#
driver.execute_script("window.scrollTo(0,0)")
#
time.sleep(1)

from re import S
import selenium
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os 
import wget

###################################################################
#please download the chromedriver, and put the address in 'driver'#
###################################################################

driver = webdriver.Chrome('I need address')
driver.get("https://www.instagram.com/")

username = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "username"))    )  

password = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "password"))     )  

login=driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]')
username.clear()
password.clear()

##################################
##please enter your account here##
##################################

username.send_keys('')
password.send_keys('')

login.click()

search = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input'))     )  

search.clear()

#######################################
##please pick a keyword for searching##
#######################################

keyword=''

search.send_keys(keyword)
time.sleep(1)
search.send_keys(Keys.RETURN)
time.sleep(1)
search.send_keys(Keys.RETURN)

WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'FFVAD'))     )  

imgs=driver.find_elements_by_class_name('FFVAD')
path=os.path.join(keyword)
os.mkdir(path)
count=0
for img in imgs:
        save_as=os.path.join(path,keyword+str(count)+'.jpg')
        wget.download(img.get_attribute('src'),save_as)
        count+=1

 
driver.quit()

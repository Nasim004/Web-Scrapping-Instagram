from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
import time
import os



username_for_search = input("Enter Account Username :")

options = webdriver.ChromeOptions()
ChromeDriverManager().install()
driver = webdriver.Chrome()
insta_url = 'https://www.instagram.com/'
driver.get(insta_url)
driver.maximize_window()


username = WebDriverWait(driver,10).until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,"input[name='username']")))
password = WebDriverWait(driver,10).until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,"input[name='password']")))

username.clear()
password.clear()
pd = os.environ.get('password')
un = os.environ.get('username')
username.send_keys(un)
password.send_keys(pd)

login = WebDriverWait(driver,10).until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,"button[type='submit']"))).click()
not_now = WebDriverWait(driver,10).until(expected_conditions.element_to_be_clickable((By.XPATH,"//div[@role='button'][contains(.,'Not Now')]"))).click()
not_now = WebDriverWait(driver,10).until(expected_conditions.element_to_be_clickable((By.XPATH,"//button[contains(text(),'Not Now')]"))).click()

# search_button = WebDriverWait(driver,15).until(expected_conditions.element_to_be_clickable((By.XPATH,"//div[contains(text(),'Search')]"))).click()

driver.get(insta_url+username_for_search)
time.sleep(5)

posts =driver.find_element("xpath",'.//*[contains(text(),"posts")]/span')
print(posts.text+" Posts")
followers = driver.find_element("xpath",'.//*[contains(text(),"followers")]/span')
print(followers.text+" Followers")
following = driver.find_element("xpath",'.//*[contains(text(),"following")]/span')
print(following.text+" Following")
driver.quit()
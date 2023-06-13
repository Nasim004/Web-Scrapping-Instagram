from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

username = input("Enter the username : ")
main_url = 'https://www.instagram.com/'


ChromeDriverManager().install()
driver = webdriver.Chrome()
driver.get(main_url+username)
time.sleep(5)

# posts =driver.find_element("xpath",'.//*[contains(text(),"posts")]/span')
driver.execute_script("window.scrollTo(0,4000)")
images = driver.find_element(By.TAG_NAME,'img')
images = [image.get_attribute('src') for image in images]
driver.close()
driver.quit()

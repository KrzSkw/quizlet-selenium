from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
import time
PATH = "C:\\Program Files (x86)\\chromedriver.exe"

driver = webdriver.Chrome(PATH)

driver.get("https://quizlet.com/create-set")


try:
    button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "onetrust-accept-btn-handler")))
    time.sleep(2)
    button.click()
    print("button found")

except:
    print("button NOT found")
    time.sleep(10)
    driver.quit() #closes chrome

# searchForTitle = driver.find_element_by_class_name("AutoExpandTextarea-textarea")
# searchForTitle.send_keys("test quizlet title")
# searchForTitle.send_keys(Keys.TAB)
# searchForTitle.send_keys(Keys.TAB)




time.sleep(10)
driver.quit() #closes chrome
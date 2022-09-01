from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service

ser = Service('C:\Program Files (x86)\chromedriver.exe')
op = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=ser, options=op)

driver.get("https://clickspeedtest.com/")

i = 0

#Scrolling so the click will be registered
driver.execute_script("window.scrollTo(0, 500);")

#Just some random long number to loop over
while i < 1000000000000000000000:
    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'clicker'))
        )
        #Clicking a bunch of times
        for e in range(0, 10):
            element.click()
    except: pass
    
    #If checking if i is divisble by 100
    if i % 100 == 0:
        try:
            e = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, 'cscore'))
            )
            #Checking if the game is over
            if e.text:
                element = driver.find_element(By.CLASS_NAME, 'times')
                print(f"Clicks: {element.text}\nCPS: {e.text}")
                driver.close()
                break
        except: continue

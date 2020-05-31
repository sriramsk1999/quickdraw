from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

sleep(10)

#TEST CASE 1
with webdriver.Firefox() as driver:
    wait = WebDriverWait(driver, 10)
    driver.get("http://127.0.0.1:3000")

    how2play = driver.find_elements_by_link_text('How to Play')[0]
    how2play.click()
    sleep(10)
    homepage = driver.find_elements_by_class_name('navbar-brand')[0]
    homepage.click()
    sleep(10)

    mail2self = driver.find_elements_by_class_name('MailSelfButton')[0]
    mail2self.click()
    sleep(10)

    wait.until(expected_conditions.alert_is_present())
    alert = Alert(driver)
    alert.dismiss()

#TEST CASE 2
with webdriver.Firefox() as driver:
    sleep(10)
    wait = WebDriverWait(driver, 10)
    driver.get("http://127.0.0.1:3000")

    canvas = driver.find_element_by_class_name("TheCanvas")
    drawing = ActionChains(driver)\
        .click_and_hold(canvas)\
        .move_by_offset(30, 25)\
        .move_by_offset(20, -20)\
        .move_by_offset(-70, 25)\
        .release()
    drawing.perform()
    
    clearbtn = driver.find_elements_by_class_name('ClearButton')[0]
    clearbtn.click()
    sleep(10)

#TEST CASE 3
with webdriver.Firefox() as driver:
    wait = WebDriverWait(driver, 10)
    driver.get("http://127.0.0.1:3000")

    clearbtn = driver.find_elements_by_class_name('ClearButton')[0]
    clearbtn.click()
    newgamebtn = driver.find_elements_by_class_name('NewGameBUtton')[0]
    newgamebtn.click()
    clearbtn.click()
    sleep(10)

#TEST CASE 4
with webdriver.Firefox() as driver:
    wait = WebDriverWait(driver, 10)
    driver.get("http://127.0.0.1:3000")
    
    mail2self = driver.find_elements_by_class_name('MailSelfButton')[0]
    mail2self.click()

    sleep(10)
    wait.until(expected_conditions.alert_is_present())
    alert = Alert(driver)
    alert.send_keys("sriramsk1999@gmail.com")
    sleep(10)
    alert.accept()

    
#TEST CASE 5
with webdriver.Firefox() as driver:
    wait = WebDriverWait(driver, 10)
    driver.get("http://127.0.0.1:3000")

    canvas = driver.find_element_by_class_name("TheCanvas")
    drawing = ActionChains(driver)\
        .click_and_hold(canvas)\
        .move_by_offset(30, 25)\
        .move_by_offset(20, -20)\
        .move_by_offset(-70, 25)\
        .release()
    drawing.perform()

    sleep(5)
    clearbtn = driver.find_elements_by_class_name('ClearButton')[0]
    clearbtn.click()
    
    canvas = driver.find_element_by_class_name("TheCanvas")
    drawing = ActionChains(driver)\
        .click_and_hold(canvas)\
        .move_by_offset(30, 25)\
        .move_by_offset(20, -20)\
        .move_by_offset(-70, 25)\
        .release()
    drawing.perform()
    sleep(5)

#TEST CASE 6
with webdriver.Firefox() as driver:
    wait = WebDriverWait(driver, 10)
    driver.get("http://127.0.0.1:3000")

    canvas = driver.find_element_by_class_name("TheCanvas")
    drawing = ActionChains(driver)\
        .click_and_hold(canvas)\
        .move_by_offset(30, 25)\
        .move_by_offset(20, -20)\
        .move_by_offset(-70, 25)\
        .release()
    drawing.perform()
    
    newgamebtn = driver.find_elements_by_class_name('NewGameBUtton')[0]
    newgamebtn.click()
    
    canvas = driver.find_element_by_class_name("TheCanvas")
    drawing = ActionChains(driver)\
        .click_and_hold(canvas)\
        .move_by_offset(30, 25)\
        .move_by_offset(20, -20)\
        .move_by_offset(-70, 25)\
        .release()
    drawing.perform()
    sleep(10)

#TEST CASE 7
with webdriver.Firefox() as driver:
    wait = WebDriverWait(driver, 10)
    driver.get("http://127.0.0.1:3000")

    canvas = driver.find_element_by_class_name("TheCanvas")
    drawing = ActionChains(driver)\
        .click_and_hold(canvas)\
        .move_by_offset(30, 25)\
        .move_by_offset(20, -20)\
        .move_by_offset(-70, 25)\
        .release()
    drawing.perform()
    sleep(10)
    
    how2play = driver.find_elements_by_link_text('How to Play')[0]
    how2play.click()
    sleep(5)

#TEST CASE 8
with webdriver.Firefox() as driver:
    wait = WebDriverWait(driver, 10)
    driver.get("http://127.0.0.1:3000")
    
    canvas = driver.find_element_by_class_name("TheCanvas")
    drawing = ActionChains(driver)\
        .click_and_hold(canvas)\
        .move_by_offset(30, 25)\
        .move_by_offset(20, -20)\
        .move_by_offset(-70, 25)\
        .release()
    drawing.perform()
    sleep(5)
    
    how2play = driver.find_elements_by_link_text('How to Play')[0]
    how2play.click()
    sleep(5)

    driver.get("http://127.0.0.1:3000")

    canvas = driver.find_element_by_class_name("TheCanvas")
    drawing = ActionChains(driver)\
        .click_and_hold(canvas)\
        .move_by_offset(30, 25)\
        .move_by_offset(20, -20)\
        .move_by_offset(-70, 25)\
        .release()
    drawing.perform()
    sleep(5)
   
#TEST CASE 9
with webdriver.Firefox() as driver:
    wait = WebDriverWait(driver, 10)
    driver.get("http://127.0.0.1:3000")
    
    canvas = driver.find_element_by_class_name("TheCanvas")
    drawing = ActionChains(driver)\
        .click_and_hold(canvas)\
        .move_by_offset(30, 25)\
        .move_by_offset(20, -20)\
        .move_by_offset(-70, 25)\
        .release()
    drawing.perform()
    
    clearbtn = driver.find_elements_by_class_name('ClearButton')[0]
    clearbtn.click()

    sleep(10)
    mail2self = driver.find_elements_by_class_name('MailSelfButton')[0]
    mail2self.click()

    wait.until(expected_conditions.alert_is_present())
    alert = Alert(driver)
    alert.send_keys("sriramsk1999@gmail.com")
    sleep(10)
    alert.accept()

#TEST CASE 10
with webdriver.Firefox() as driver:
    wait = WebDriverWait(driver, 10)
    driver.get("http://127.0.0.1:3000")
    
    mail2self = driver.find_elements_by_class_name('MailSelfButton')[0]
    mail2self.click()

    wait.until(expected_conditions.alert_is_present())
    alert = Alert(driver)
    alert.dismiss()

    newgamebtn = driver.find_elements_by_class_name('NewGameBUtton')[0]
    newgamebtn.click()
    sleep(10)

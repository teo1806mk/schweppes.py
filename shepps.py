import time
import smtplib
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import random
import pywhatkit
from playsound import playsound
from datetime import datetime

p = "0"


def wach():
    timwH = int(time.strftime("%H"))
    tiemM = int(time.strftime("%M")) + 1
    print(timwH, tiemM)
    # syntax: phone number with country code, message, hour and minutes
    pywhatkit.sendwhatmsg('friend num', 'messeg', timwH, tiemM)


def email():
    gmail_user = 'yours@gmail.com'
    gmail_password = 'Password'

    sent_from = gmail_user
    to = ['friend email']
    subject = 'messeges'
    body = 'text'

    email_text = """\
    From: %s
    To: %s
    Subject: %s
    %s
    """ % (sent_from, ", ".join(to), subject, body)

    try:
        smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        smtp_server.ehlo()
        smtp_server.login(gmail_user, gmail_password)
        smtp_server.sendmail(sent_from, to, email_text)
        smtp_server.close()
        print("Email sent successfully!")
    except Exception as ex:
        print("Something went wrong….", ex)


def paraskevas():
    login = driver.find_element(by=By.ID, value="signInEmailAddress")
    login.click()
    login.send_keys("login email")
    pascod = driver.find_element(by=By.ID, value="currentPassword")
    pascod.click()
    pascod.send_keys("login Password")
    time.sleep(2)
    driver.find_element(by=By.CSS_SELECTOR, value="#ces-form-submit-ces-sign-in-form").click()
    time.sleep(3)
    dora = driver.find_element(by=By.CSS_SELECTOR,
                               value="#global-page-wrapper > div.scroll-content > main > div > div > div > div.split-layout__sidebar > div > div.default-sidebar__body > ul > li:nth-child(4) > a > div.label")
    time.sleep(3)
    dora.click()


driver = webdriver.Chrome(executable_path=r"path of driver")
driver.set_window_size(1024, 800)
url = (f"https://www.schweppes.gr/login.php")
driver.get(url)

time.sleep(5)
driver.find_element(by=By.ID, value="accept-recommended-btn-handler").click()
paraskevas()
k = 1
time.sleep(2)
pp = 0
while p == "0":

    time.sleep(36)
    try:
        # getting gifts
        print('getting gifts')
        gift_container = driver.find_element(by=By.ID, value='userListPrize')
        gifts = gift_container.find_elements(by=By.TAG_NAME, value='li')

        # for each gift
        for gift in gifts:
            class_name = gift.get_attribute('class')
            image_alt = gift.find_element(by=By.TAG_NAME, value='img').get_attribute('alt')
            if class_name == 'prize-list-item item-active' and image_alt == 'Mi Electric Scooter - Xiaomi':
                p = "1"
            # if class_name == 'prize-list-item item-active' and image_alt == 'Eva Fuda - μπρελόκ κίτρινο & μαύρο':
            #    p = '1'

    except:
        time.sleep(10)
        try:
            driver.find_element(by=By.CSS_SELECTOR,
                                value='#global-page-wrapper > div.scroll-content > main > div > div > div > div.split-layout__sidebar > div > div.default-sidebar__body > ul > li:nth-child(4) > a > div.label').click()
        except:
            try:
                time.sleep(2)
                driver.find_element(by=By.CSS_SELECTOR,
                                    value="#global-page-wrapper > div.scroll-content > div > div.container > div > div > div > a.btn.btn--md.btn--yellow.jsAgeButtonYes").click()
                time.sleep(6)
                driver.get(url)
                time.sleep(6)
                paraskevas()
            except:
                try:
                    time.sleep(6)
                    driver.get(url)
                    time.sleep(6)
                    paraskevas()
                except:
                    p = "0"

    if p != "0":
        email()
        wach()
        playsound("path of song")
    else:
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print(k, current_time)
        k += 1
        driver.refresh()

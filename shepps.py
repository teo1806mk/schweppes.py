import time
import smtplib
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import random
p="0"
from playsound import playsound

def email():


    gmail_user = 'karipidis2001theodor@gmail.com'
    gmail_password = 'ddytgvcefbgzjnsi'


    sent_from = gmail_user
    to = ['teo2005lol@gmail.com', 'karipidis73@gmail.com','mariannavourakii@gmail.com','pdimis01@gmail.com']
    subject = 'pare grigora thlefono ton thodori karypidi'
    body = 'PARETILEFONO TON THODORI'

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
    login = driver.find_element_by_id("signInEmailAddress")
    login.click()
    login.send_keys("hdjfic2001@gmail.com")
    pascod = driver.find_element_by_id("currentPassword")
    pascod.click()
    pascod.send_keys("18062001!Ka")
    time.sleep(2)
    booton = driver.find_element_by_id("ces-form-submit-ces-sign-in-form").click()
    time.sleep(3)
    dora = driver.find_element_by_css_selector("#global-page-wrapper > div.scroll-content > main > div > div > div > div.split-layout__sidebar > div > div.default-sidebar__body > ul > li:nth-child(4) > a > div.label")
    time.sleep(3)
    dora.click()


driver = webdriver.Chrome(executable_path=r"C:\Users\teo20\OneDrive\Υπολογιστής\bot sp\chromedriver.exe")

url = (f"https://www.schweppes.gr/login.php")
driver.get(url)

time.sleep(6)
cookes = driver.find_element_by_id("accept-recommended-btn-handler").click()
paraskevas()
k = 0
time.sleep(2)
pp = 0
while p == "0":
    print(k)
    time.sleep(2)
    try:

        poso = driver.find_element_by_xpath(f"/html/body/div[1]/div[1]/main/div/div/div/div[2]/div/div[2]/ul/li[11]/div[1]/div/span[2]").clear()
        print(poso , "poso")
        p = str(poso.text)
    except :
        time.sleep(10)
        try:
            driver.find_element_by_css_selector("#global-page-wrapper > div.scroll-content > div > div.container > div > div > div > a.btn.btn--md.btn--yellow.jsAgeButtonYes").click()
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

    k += 1
    if p != "0":
        #email()
        playsound("Rick_Astley_-_Never_Gonna_Give_You_Up_Official_Music_Video[ConConverter.com].mp3")
    else:
        print(k, time.time())
        k += 1
        driver.refresh()



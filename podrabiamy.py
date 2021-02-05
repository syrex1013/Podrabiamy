from discord import Client
from discord import File
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import os
import time
from io import BytesIO
from PIL import Image
import math

bot = Client()
browser = webdriver.Chrome()
# change keyword here
keyword = "RESPOND"
MATMA_2A2 = "https://odrabiamy.pl/matematyka/ksiazka-11493"
ANG_JK = "https://odrabiamy.pl/jezyk-angielski/ksiazka-11982"
emails = "remix3030303@hotmail.com"
passw = "Fpu6TVFsQfr3avj"
@bot.event
async def on_message(message):
      message_text = message.content.strip().upper()
      if "$MATMA" in message_text and "--" not in message_text:
            data = message_text.split()
            strona = data[1]
            zadanie_numer = data[2]
            try:
                Login(browser)
                await message.channel.send('Logged in as {0}'.format(emails))
            except:
                pass
            browser.get('{0}/strona-{1}'.format(MATMA_2A2,strona))
            await message.channel.send('Opened page {0}'.format(strona))
            AcceptCookie(browser)
            zadania = browser.find_elements_by_class_name("number")
            zadania_przyciski = browser.find_elements_by_class_name("exercise-number-link")
            linki = []
            for link in zadania_przyciski:
                href = link.get_attribute("href")
                linki.append(href)
            found = {None}
            if zadanie_numer == "WSZYSTKO":
                for lnk in linki:
                    browser.get(lnk)
                    content = browser.find_element_by_class_name("exerciseContainer")
                    viewport_height = browser.execute_script("return window.innerHeight")   
                    ilosc = math.ceil(content.size['height']/500)
                    print(content.size['height'])
                    for x in range(ilosc):                 
                        browser.save_screenshot("odp.png")
                        ScrollDown(browser)
                        await message.channel.send(file=File('odp.png'))
                    await message.channel.send('Whole exercise was sent!'.format(zadanie_numer))
            for zadanie in zadania:               
                if zadanie_numer == zadanie.text:
                    found = 1
                    zadanie.click()
                    await message.channel.send('Opened exercise {0}'.format(zadanie_numer))
                    content = browser.find_element_by_class_name("exerciseContainer")
                    viewport_height = browser.execute_script("return window.innerHeight")   
                    ilosc = math.ceil(content.size['height']/500)
                    print(content.size['height'])
                    for x in range(ilosc):                 
                        browser.save_screenshot("odp.png")
                        ScrollDown(browser)
                        await message.channel.send(file=File('odp.png'))
                    await message.channel.send('Whole exercise was sent!'.format(zadanie_numer))
            if found == 0:
                await message.channel.send('No exercise {0} on page {1}'.format(zadanie_numer,strona))
            else:
                found = 0
      elif "$ANGIELSKI" in message_text and "--" not in message_text:
            data = message_text.split()
            strona = data[1]
            zadanie_numer = data[2]
            try:
                Login(browser)
                await message.channel.send('Logged in as {0}'.format(emails))
            except:
                pass
            browser.get('{0}/strona-{1}'.format(ANG_JK,strona))
            await message.channel.send('Opened page {0}'.format(strona))
            AcceptCookie(browser)
            zadania = browser.find_elements_by_class_name("number")
            zadania_przyciski = browser.find_elements_by_class_name("exercise-number-link")
            linki = []
            for link in zadania_przyciski:
                href = link.get_attribute("href")
                linki.append(href)
            found = {None}
            if zadanie_numer == "WSZYSTKO":
                for lnk in linki:
                    browser.get(lnk)
                    content = browser.find_element_by_class_name("exerciseContainer")
                    viewport_height = browser.execute_script("return window.innerHeight")   
                    ilosc = math.ceil(content.size['height']/500)
                    print(content.size['height'])
                    for x in range(ilosc):                 
                        browser.save_screenshot("odp.png")
                        ScrollDown(browser)
                        await message.channel.send(file=File('odp.png'))
                    await message.channel.send('Whole exercise was sent!'.format(zadanie_numer))
            found = 0
            for zadanie in zadania:
                if zadanie_numer == zadanie.text:
                    found = 1
                    zadanie.click()
                    await message.channel.send('Opened exercise {0}'.format(zadanie_numer))
                    answer = browser.find_element_by_class_name("solution-area")
                    content = browser.find_element_by_class_name("exerciseContainer")
                    body = browser.find_element_by_class_name("container-content")
                    answer.click()
                    viewport_height = browser.execute_script("return window.innerHeight")   
                    ilosc = math.ceil(content.size['height']/500)
                    print(content.size['height'])
                    for x in range(ilosc):                 
                        browser.save_screenshot("odp.png")
                        ScrollDown(browser)
                        await message.channel.send(file=File('odp.png'))
                    await message.channel.send('Whole exercise was sent!'.format(zadanie_numer))
            if found == 0:
                await message.channel.send('No exercise {0} on page {1}'.format(zadanie_numer,strona))
            else:
                found = 0 
      elif "$KSIAZKA" in message_text and "--" not in message_text:
            data = message_text.split()
            link = data[1]
            strona = data[2]
            zadanie_numer = data[3]
            
            try:
                Login(browser)
                await message.channel.send('Logged in as {0}'.format(emails))
            except:
                pass
            browser.get('{0}/strona-{1}'.format(link,strona))
            await message.channel.send('Opened page {0}'.format(strona))
            AcceptCookie(browser)
            zadania = browser.find_elements_by_class_name("number")
            zadania_przyciski = browser.find_elements_by_class_name("exercise-number-link")
            linki = []
            for link in zadania_przyciski:
                href = link.get_attribute("href")
                linki.append(href)
            found = {None}
            if zadanie_numer == "WSZYSTKO":
                for lnk in linki:
                    browser.get(lnk)
                    content = browser.find_element_by_class_name("exerciseContainer")
                    viewport_height = browser.execute_script("return window.innerHeight")   
                    ilosc = math.ceil(content.size['height']/500)
                    print(content.size['height'])
                    for x in range(ilosc):                 
                        browser.save_screenshot("odp.png")
                        ScrollDown(browser)
                        await message.channel.send(file=File('odp.png'))
                    await message.channel.send('Whole exercise was sent!'.format(zadanie_numer))
            found = 0
            for zadanie in zadania:
                if zadanie_numer == "WSZYSTKO":
                    found = 1
                    zadanie.click()
                    await message.channel.send('Opened exercise {0}'.format(zadanie_numer))
                    answer = browser.find_element_by_class_name("solution-area")
                    content = browser.find_element_by_class_name("exerciseContainer")
                    body = browser.find_element_by_class_name("container-content")
                    answer.click()
                    viewport_height = browser.execute_script("return window.innerHeight")   
                    ilosc = math.ceil(content.size['height']/500)
                    print(content.size['height'])
                    for x in range(ilosc):                 
                        browser.save_screenshot("odp.png")
                        ScrollDown(browser)
                        await message.channel.send(file=File('odp.png'))
                    await message.channel.send('Whole exercise {0} was sent!'.format(zadanie_numer))
                elif zadanie_numer == zadanie.text:
                    found = 1
                    zadanie.click()
                    await message.channel.send('Opened exercise {0}'.format(zadanie_numer))
                    answer = browser.find_element_by_class_name("solution-area")
                    content = browser.find_element_by_class_name("exerciseContainer")
                    body = browser.find_element_by_class_name("container-content")
                    answer.click()
                    viewport_height = browser.execute_script("return window.innerHeight")   
                    ilosc = math.ceil(content.size['height']/500)
                    print(content.size['height'])
                    for x in range(ilosc):                 
                        browser.save_screenshot("odp.png")
                        ScrollDown(browser)
                        await message.channel.send(file=File('odp.png'))
                    await message.channel.send('Whole exercise was sent!'.format(zadanie_numer))
            if found == 0:
                await message.channel.send('No exercise {0} on page {1}'.format(zadanie_numer,strona))
            else:
                found = 0
      elif "$HELP" in message_text  and "--" not in message_text:
            await message.channel.send(
            '''
            Komendy:
    ***$MATMA***  <numer strony>  <numer zadania> -- Wysyła na kanał zdjęcia odpowiedzi w podanym zadaniu.
    ***$ANGIELSKI***  <numer strony>  <numer zadania> -- Wysyła na kanał zdjęcia odpowiedzi w podanym zadniu.
    ***$KSIAZKA***  <link do ksiazki na odrabiamy>  <numer strony>  <numer zadania> -- Wysyła na kanał zdjęcia odpowiedzi w podanym zadniu.
            
Informacje:
    W miejscu ***<numer zadania>*** mozna wpisac również ***"WSZYSTKO"*** co spowoduje zrobienie screenów każdego zadania.
            ''')
def ScrollDown(driver):
    body = driver.find_element_by_css_selector('body')
    body.click()
    body.send_keys(Keys.PAGE_DOWN) 
def Login(driver):
    driver.get('https://odrabiamy.pl/II-liceum?signIn=true')
    email = driver.find_element_by_name("login")
    password = driver.find_element_by_name("password")
    email.send_keys(emails)
    password.send_keys(passw)
    button_login = driver.find_element_by_id("qa-login")
    button_login.click()
def AcceptCookie(driver):
    try:
        accept = driver.find_element_by_xpath('//button[text()="Przejdź do Odrabiamy"]')
        accept.click()
    except:
         pass
#https://odrabiamy.pl/api/v1.3/sessions.json
#{"user":{"login":"remix3030303@hotmail.com","password":"Fpu6TVFsQfr3avj"}}

bot.run("ODA2OTcxODEzNzA4MDM4MTY1.YBxNEQ.l0QBSwFaAMM4RkdeGbCyHD2lSos")
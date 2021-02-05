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
            #GET DATA FROM CHAT
            data = message_text.split()
            strona = data[1]
            zadanie_numer = data[2]

            #LOGIN
            Login(browser)
            await message.channel.send('Logged in as {0}'.format(emails))
            OpenWebPage(browser,'{0}/strona-{1}'.format(MATMA_2A2,strona))
            await message.channel.send('Opened page {0}'.format(strona))

            #ACCEPT COOKIES
            AcceptCookie(browser)

            #GET EXERCISES FROM WHOLE PAGE
            if zadanie_numer == "WSZYSTKO":
                linki = GetLinksToAllExercises(browser)
                for lnk in linki:
                    OpenWebPage(browser,lnk)
                    ilosc = CalculateAmountOfScroll(browser)
                    for x in range(ilosc):                 
                        browser.save_screenshot("odp.png")
                        ScrollDown(browser)
                        await message.channel.send(file=File('odp.png'))
                    await message.channel.send('Whole exercise was sent!')
            #GET EXERCISE BY NUMBER
            else:
                zadanie = GetExerciseByNumber(browser,zadanie_numer)
                zadanie.click()
                await message.channel.send('Opened exercise {0}'.format(zadanie_numer))
                ilosc = CalculateAmountOfScroll(browser)
                for x in range(ilosc):                 
                    browser.save_screenshot("odp.png")
                    ScrollDown(browser)
                    await message.channel.send(file=File('odp.png'))
                await message.channel.send('Exercise {0} was sent!'.format(zadanie_numer))
      elif "$ANGIELSKI" in message_text and "--" not in message_text:
            #GET DATA FROM CHAT
            data = message_text.split()
            strona = data[1]
            zadanie_numer = data[2]

            #LOGIN
            Login(browser)
            await message.channel.send('Logged in as {0}'.format(emails))
            OpenWebPage(browser,'{0}/strona-{1}'.format(ANG_JK,strona))
            await message.channel.send('Opened page {0}'.format(strona))

            #ACCEPT COOKIES
            AcceptCookie(browser)

            #GET EXERCISES FROM WHOLE PAGE
            if zadanie_numer == "WSZYSTKO":
                linki = GetLinksToAllExercises(browser)
                for lnk in linki:
                    OpenWebPage(browser,lnk)
                    ilosc = CalculateAmountOfScroll(browser)
                    for x in range(ilosc):                 
                        browser.save_screenshot("odp.png")
                        ScrollDown(browser)
                        await message.channel.send(file=File('odp.png'))
                    await message.channel.send('Whole exercise was sent!')
            #GET EXERCISE BY NUMBER
            else:
                zadanie = GetExerciseByNumber(browser,zadanie_numer)
                zadanie.click()
                await message.channel.send('Opened exercise {0}'.format(zadanie_numer))
                ilosc = CalculateAmountOfScroll(browser)
                for x in range(ilosc):                 
                    browser.save_screenshot("odp.png")
                    ScrollDown(browser)
                    await message.channel.send(file=File('odp.png'))
                await message.channel.send('Exercise {0} was sent!'.format(zadanie_numer)) 
      elif "$KSIAZKA" in message_text and "--" not in message_text:
            #GET DATA FROM CHAT
            data = message_text.split()
            link = data[1]
            strona = data[2]
            zadanie_numer = data[3]

            #LOGIN
            Login(browser)
            await message.channel.send('Logged in as {0}'.format(emails))
            OpenWebPage(browser,'{0}/strona-{1}'.format(link,strona))
            await message.channel.send('Opened page {0}'.format(strona))

            #ACCEPT COOKIES
            AcceptCookie(browser)

            #GET EXERCISES FROM WHOLE PAGE
            if zadanie_numer == "WSZYSTKO":
                linki = GetLinksToAllExercises(browser)
                for lnk in linki:
                    OpenWebPage(browser,lnk)
                    ilosc = CalculateAmountOfScroll(browser)
                    for x in range(ilosc):                 
                        browser.save_screenshot("odp.png")
                        ScrollDown(browser)
                        await message.channel.send(file=File('odp.png'))
                    await message.channel.send('Whole exercise was sent!')
            #GET EXERCISE BY NUMBER
            else:
                zadanie = GetExerciseByNumber(browser,zadanie_numer)
                zadanie.click()
                await message.channel.send('Opened exercise {0}'.format(zadanie_numer))
                ilosc = CalculateAmountOfScroll(browser)
                for x in range(ilosc):                 
                    browser.save_screenshot("odp.png")
                    ScrollDown(browser)
                    await message.channel.send(file=File('odp.png'))
                await message.channel.send('Exercise {0} was sent!'.format(zadanie_numer))
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
    try:
        driver.get('https://odrabiamy.pl/II-liceum?signIn=true')
        email = driver.find_element_by_name("login")
        password = driver.find_element_by_name("password")
        email.send_keys(emails)
        password.send_keys(passw)
        button_login = driver.find_element_by_id("qa-login")
        button_login.click()
    except:
        pass
def AcceptCookie(driver):
    try:
        accept = driver.find_element_by_xpath('//button[text()="Przejdź do Odrabiamy"]')
        accept.click()
    except:
         pass
def GetLinksToAllExercises(driver):
    zadania = driver.find_elements_by_class_name("number")
    zadania_przyciski = driver.find_elements_by_class_name("exercise-number-link")
    linki = []
    for link in zadania_przyciski:
        href = link.get_attribute("href")
        linki.append(href)
    return linki
def GetExerciseByNumber(driver, number):
    zadania = driver.find_elements_by_class_name("number")
    for zadanie in zadania:
        if number == zadanie.text:
            return zadanie
def CalculateAmountOfScroll(driver):
    content = driver.find_element_by_class_name("exerciseContainer")
    viewport_height = driver.execute_script("return window.innerHeight")   
    ilosc = math.ceil(content.size['height']/500)
    return ilosc
def OpenWebPage(driver,link):
    driver.get(link)
#https://odrabiamy.pl/api/v1.3/sessions.json
#{"user":{"login":"remix3030303@hotmail.com","password":"Fpu6TVFsQfr3avj"}}

bot.run("ODA2OTcxODEzNzA4MDM4MTY1.YBxNEQ.l0QBSwFaAMM4RkdeGbCyHD2lSos")
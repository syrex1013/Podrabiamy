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
import re

bot = Client()
browser = webdriver.Chrome()
# change keyword here
emails = "remix3030303@hotmail.com"
passw = "Fpu6TVFsQfr3avj"
token = "ODA2OTcxODEzNzA4MDM4MTY1.YBxNEQ.l0QBSwFaAMM4RkdeGbCyHD2lSos"
@bot.event
async def on_message(message):
      message_text = message.content.strip().upper()
      if "$KSIAZKA" in message_text and "--" not in message_text:
            #GET DATA FROM CHAT
            data = message_text.split()
            if len(data) < 4 or len(data) > 4:
                await message.channel.send('Please supply all arguments! If you don`t remember commands, here they are: $HELP')
            link = data[1]
            strona = data[2]
            zadanie_numer = data[3]

            #LOGIN
            Login(browser)
            await message.channel.send('Logged in as ***{0}***'.format(emails))
            OpenWebPage(browser,'{0}/strona-{1}'.format(link,strona))
            await message.channel.send('Opened page ***{0}***'.format(strona))

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
                if zadanie == None:
                    await message.channel.send('Exercise ***{0}*** not found on page ***{1}***!'.format(zadanie_numer,strona))
                zadanie.click()
                await message.channel.send('Opened exercise ***{0}***'.format(zadanie_numer))
                ilosc = CalculateAmountOfScroll(browser)
                for x in range(ilosc):                 
                    browser.save_screenshot("odp.png")
                    ScrollDown(browser)
                    await message.channel.send(file=File('odp.png'))
                await message.channel.send('Exercise ***{0}*** was sent!'.format(zadanie_numer))
      elif "$PODRABIAMY" in message_text and "--" not in message_text:
            #GET DATA FROM CHAT
            data = message_text.split()
            if len(data) < 5 or len(data) > 5:
                await message.channel.send('Please supply all arguments! If you don`t remember commands, here they are: $HELP')
            nazwa_ksiegi = data[1]
            klasa = data[2]
            strona = data[3]
            zadanie_numer = data[4]

            #LOGIN
            Login(browser)
            await message.channel.send('Logged in as ***{0}***'.format(emails))
            
            #CHOOSE SCHOOL
            if "podstaw" in klasa.lower():
                numer_klasy = re.findall("\d+", klasa)[0]
                nazwa_parametru = int(numer_klasy)+"-szkoly-podstawowej"
                OpenWebPage(browser,"https://odrabiamy.pl/{0}".format(nazwa_parametru))                
                await message.channel.send('Searching in primary school books!')
            elif "liceum" in klasa.lower():
                numer_klasy = re.findall("\d+", klasa)[0]
                roman_numeral = int(numer_klasy)*"I"
                nazwa_parametru = roman_numeral+"-liceum"
                OpenWebPage(browser,"https://odrabiamy.pl/{0}".format(nazwa_parametru))
                await message.channel.send('Searching in High-School books!')
            elif "technikum" in klasa.lower():
                numer_klasy = re.findall("\d+", klasa)[0]
                roman_numeral = int(numer_klasy)*"I"
                nazwa_parametru = roman_numeral+"-technikum"
                OpenWebPage(browser,"https://odrabiamy.pl/{0}".format(nazwa_parametru))
                await message.channel.send('Searching in technical institute books!')
            
            #ACCEPT COOKIES
            AcceptCookie(browser)

            #SEARCH FOR BOOK
            searchfield = browser.find_element_by_class_name("search-field")
            items = nazwa_ksiegi.split('_')
            searchfield.send_keys(' '.join(items))
            
            bookswrapper = browser.find_element_by_class_name("books-wrapper")
            try:
                book = bookswrapper.find_elements_by_class_name("book")[0]
            except:
                await message.channel.send('Cannot find book with supplied name!')
            bookname = book.find_element_by_class_name("book-cover-title")
            await message.channel.send('Opening book "{0}"!'.format(bookname.text))
            book.click()

            #OPEN PAGE
            OpenWebPage(browser,browser.current_url+"/strona-{0}".format(strona))
            await message.channel.send('Opened page "{0}"!'.format(strona))

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
                if zadanie == None:
                    await message.channel.send('Exercise ***{0}*** not found on page ***{1}***!'.format(zadanie_numer,strona))
                zadanie.click()
                await message.channel.send('Opened exercise ***{0}***'.format(zadanie_numer))
                ilosc = CalculateAmountOfScroll(browser)
                for x in range(ilosc):                 
                    browser.save_screenshot("odp.png")
                    ScrollDown(browser)
                    await message.channel.send(file=File('odp.png'))
                await message.channel.send('Exercise ***{0}*** was sent!'.format(zadanie_numer))
      elif "$HELP" in message_text  and "--" not in message_text:
            await message.channel.send(
            '''
            Komendy:
    ***$KSIAZKA***  <link do ksiazki na odrabiamy>  <numer strony>  <numer zadania> -- Wysyła na kanał zdjęcia odpowiedzi w podanym zadniu.
    ***$PODRABIAMY***  <nazwa ksiazki>  <klasa> <numer strony>  <numer zadania> -- Wysyła na kanał zdjęcia odpowiedzi w podanym zadniu.
            
Informacje:
    W miejscu ***<numer zadania>*** mozna wpisac również ***"WSZYSTKO"*** co spowoduje zrobienie screenów każdego zadania.
    W miejscu ***<nazwa ksiazki>*** wpisujemy zamiast spacji ***_***. Nazwa książki ***nie musi*** być dokładna!!!
    W miejscu ***<klasa>*** wpisujemy klase bez spacji np. liceum2, podstawowa1, technikum2
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

bot.run(token)
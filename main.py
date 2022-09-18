from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from art import *
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import getpass

import warnings
warnings.filterwarnings("ignore")
 

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)

pagarba = 0
lygis = 0
#a









def start():
 tprint("TUZAS#")
 print('Suvesk prisijungimo duomenis')
 useris = getpass.getpass("Suvesk slapyvardi: ")
 if not useris:
   print('Suvesk neteisingai!')
 else:
   passwordas = getpass.getpass('Ivesk slaptazodi: ')
   if not passwordas:
    print('Suvesk neteisingai!')
   else:
     driver.get("https://mafija.draugas.lt/auth/login")
     driver.find_element("xpath", '//*[@id="login-content"]/form/table/tbody/tr[2]/td/table/tbody/tr/td[1]/label/span').click()
     driver.find_element("xpath", '//*[@id="usr"]').send_keys(useris)
     driver.find_element("xpath", '//*[@id="login-content"]/form/table/tbody/tr[1]/td[2]/span/span/input').click()
     driver.implicitly_wait(3)
     driver.find_element("xpath", '//*[@id="pwd"]').send_keys(passwordas)
     driver.find_element("xpath", '//*[@id="login-content"]/form/table/tbody/tr[1]/td[2]/span/span/input').click()
     driver.implicitly_wait(2)
     menu() 



 

 
 
def menu():
    loop = True
    while loop:
        print("1 - PASIRINK PRIESININKO PAGARBOS KIEKI\n2 - PASIRINKT PRIESININKO LYGI\n3 - PASIRINK ATAKAS")
        pagrindinis = input("Pasirink: ")

        if pagrindinis == '1':
            pagarbaa = input("Pasirink: ")
            global pagarba
            pagarba = pagarbaa
              
        elif pagrindinis == '2':
            lygiss = input('Pasirink: ')
            global lygis
            lygis = lygiss
        elif pagrindinis == '3':
            home_act2()

        else:
            print("'1 - IVESTI PRIESININKO PAGARBOS KIEKI\', \'2 - PASIRINKT ATAKAS\'")

def home_act1():
    print("Suvesk prisijungimo duomenis cia:")
    global nickas
    global passas
    nickass = input("Suvesk slapyvardi: ")
    if not nickass:
        print('Suvesk teisingai!')
    else:
        psw = input('Ivesk slaptazodi: ')
        if not psw:
            print('Suvesk teisingai!')
        else:
            nickas = nickass
            passas = psw
                   

def home_act2():
    print("Ar noresite atlikti atakas su limituotu kiekiu? Jei taip rasykite 1, jei ne 2")
    pasirinkimas = input("Pasirink: ")
    if pasirinkimas == '1':
        print('Irasykite ataku kieki')
        kiekis = input("Pasirink: ")
        kiekiss = int(kiekis)
        looper(1, kiekiss)
    if pasirinkimas == '2':
        looper(9999999, 999999)    
    exit()
    
    
def uzduotys():
    #https://mafija.draugas.lt/quest?z=eX2
    driver.get('https://mafija.draugas.lt/quest?z=eX2')
    driver.find_element(By.XPATH, '//*[@id="qDiff1"]/td[2]/form/input[3]').click()
    
    pass    

def loop(value):
    global pagarba
    global lygis
    for n in range(value):
        #//*[@id="matchmaker"]/table/tbody/tr[1]/td/input
        driver.find_element("xpath", '//*[@id="cwrapper"]/div[3]/div[1]/a[3]/span').click()
        driver.find_element("xpath", '//*[@id="matchmaker"]/table/tbody/tr[1]/td/input').clear()
        driver.find_element("xpath", '//*[@id="matchmaker"]/table/tbody/tr[1]/td/input').send_keys(lygis)
        driver.find_element("xpath", '//*[@id="matchmaker"]/table/tbody/tr[3]/td/input').clear()
        driver.find_element("xpath", '//*[@id="matchmaker"]/table/tbody/tr[3]/td/input').send_keys(pagarba)
        driver.find_element("xpath", '//*[@id="matchmaker"]/div/span/button').click()
        driver.implicitly_wait(2)
        driver.find_element("xpath", '//*[@id="cwrapper"]/div[3]/div[3]/div/div/div/div[2]/table/tbody/tr/td[3]/a').click()
        driver.implicitly_wait(1)
        try:
         driver.find_element("xpath", '//*[@id="msgbox"]/div/div/div/table/tbody/tr/td[2]/form/input[2]').click()
         driver.implicitly_wait(1)
         driver.find_element("xpath", '//*[@id="cwrapper"]/div[3]/div[3]/div/div/div/div/div/div[2]/div/div[1]/div/div[3]/a').click()
         try:
             driver.find_element("xpath", '//*[@id="msgbox"]/div/div/div/a')
             driver.find_element("xpath", '//*[@id="cheader"]/a').click()
             print('Neturi pinigu!')
             menu()
             break
         except:    
          driver.find_element("xpath", '//*[@id="cheader"]/a').click()
          continue       
        except:    
          try:
           driver.find_element("xpath", '//*[@id="windows-modal"]/div[1]/div/a').click()
           # KAVA
           kiekisss = (WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="cwrapper"]/div[2]/div[1]/table/tbody/tr[1]/td[3]/a/u'))).get_attribute("innerHTML"))
           kiekiz = int(kiekisss)    
           if kiekiz < 50:    
            driver.find_element("xpath", '//*[@id="map"]/a[47]').click()
            driver.implicitly_wait(1)
            driver.find_element("xpath", '//*[@id="menu_46"]/tbody/tr[5]/th/a').click()
            # PABAIGA KAVA
            driver.implicitly_wait(3)
            driver.find_element("xpath", '//*[@id="cheader"]/a').click()
           else:
              pass
              driver.find_element("xpath", '//*[@id="cheader"]/a').click() 
          except:
           print('Ataka nepavyko')
           n += 1
           driver.implicitly_wait(15)
           driver.find_element("xpath", '//*[@id="cheader"]/a').click()
    else:
        menu() 

def looper(loop_amount, loop_value):
    for n in range(loop_amount):
        loop(loop_value)

#

start()
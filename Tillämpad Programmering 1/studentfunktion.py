from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import personfunktion
import main

#student funktion

urlperson = "https://johan.nicklason.se/personnummergenerator/"
startnmr = "040613"
urlcola = "https://coke.studentkortet.se/"
nmrcomp = "200406135103"

while True:
    driver=webdriver.Chrome(executable_path="C:\\Users\\otalc\\OneDrive\\Dokument\\cola energy bot\\chromedriver.exe")
    driver.get(urlcola)
    username = driver.find_element_by_id("personal_number")
    username.send_keys(nmrcomp)
    driver.find_element_by_id("personal_number").send_keys(Keys.ENTER)
    
    if driver.current_url == "https://coke.studentkortet.se/":
        print("hello")
        driver.close()
    else:
        #spara kod
        kod = driver.find_element_by_class_name("number").text
        kodnospace = kod.replace(' ', '')
        break
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#personnummer funktion

def personnummer(urlperson, startnmr):
    #Öppna Personnmr Sida
    driver=webdriver.Chrome(executable_path="C:\\Users\\otalc\\OneDrive\\Dokument\\cola energy bot\\chromedriver.exe")
    driver.get(urlperson)

    #välj låda skriv nummer o press enter
    username = driver.find_element_by_name('number')
    username.send_keys(startnmr)
    driver.find_element_by_name("number").send_keys(Keys.ENTER)

    #Kopiera personnummer och gör om texten

    nmr = driver.find_element_by_xpath("""//*[@id="home"]/div/p[1]/b""").text

    nmrnobind = nmr.replace('-', '')

    nmrcomp = ("20" + (nmrnobind))

    return(nmrcomp)


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pandas as pd
Yazar_Linkleri = []

Sozluk = {"isim":[],"dogumTarihi":[],"DogumYeri":[]}

def login(the_driver):
    Login_Button=the_driver.find_element(By.CSS_SELECTOR,"div.col-md-4 p a")
    Login_Button.click()
    KullaniciText=the_driver.find_element(By.ID,"username")
    KullaniciText.send_keys("Naber")
    Sifre = the_driver.find_element(By.ID,"password")
    Sifre.send_keys("123456")
    Button = the_driver.find_element(By.CSS_SELECTOR,"form input[value = 'Login']")
    Button.click()
    
def Yazar_Linkleri_scrape(driver):
    while(True):
        Dosya = driver.find_elements(By.XPATH,"//a[text()='(about)']")
        for i in Dosya:
            Yazar_Linkleri.append(i.get_attribute("href"))
        try:
            Continue_button= driver.find_element(By.CSS_SELECTOR,"ul.pager li.next a")
            Continue_button.click()
        except:
            break

    
    











service = Service("C:\Drivers\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service)
url = "https://quotes.toscrape.com/"
Options = webdriver.ChromeOptions()
Options.add_argument("--start-maximized")
driver.get(url)
login(driver)
Yazar_Linkleri_scrape(driver)
Liste =set(Yazar_Linkleri)
for i in Liste:
    driver.get(i)
    Sozluk["isim"].append(driver.find_element(By.CSS_SELECTOR,"div.author-details h3").text)
    Sozluk["dogumTarihi"].append(driver.find_element(By.CSS_SELECTOR,"div.author-details p span.author-born-date").text)
    Sozluk["DogumYeri"].append(driver.find_element(By.CSS_SELECTOR,"div.author-details p span.author-born-location").text)

df = pd.DataFrame(Sozluk)
df.to_excel("Sozluk.xlsx")
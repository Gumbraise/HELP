from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
from datetime import datetime
import json
 
print("\n\n     Oslogram v.1.0     \n")
# Lancement du driver Chrome
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
print("[" + current_time + "] Lancement du driver Chrome")
chrome_options = Options()
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=chrome_options, executable_path="../utilitaire/chromedriver")
# Accès à Instagram
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
print("[" + current_time + "] Accès à Instagram")
driver.get("https://www.instagram.com/accounts/login/?next=/explore/people/suggested/")
driver.implicitly_wait(3)
 
# Récupérations des identifiants de connexions fournis dans le fichier identifiants.json
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
print("[" + current_time + "] Récupérations des identifiants de connexions fournis dans le fichier identifiants.json")
with open("../config/identifiants.json") as identifiants:
    data = json.load(identifiants)
 
# Connexion à Instagram
driver.find_element_by_xpath(("//input[@name=\"username\"]"))\
    .send_keys((data["username"]))
driver.find_element_by_xpath(("//input[@name=\"password\"]"))\
    .send_keys((data["password"]))
sleep(1)
driver.find_element_by_xpath(("//button[@class=\"sqdOP  L3NKy   y3zKF     \"]"))\
    .click()
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
print("[" + current_time + "] Connexion à Instagram")
# Accès à la page de suggestions
driver.implicitly_wait(3)
sleep(1)
driver.find_element_by_xpath(("//button[@class=\"sqdOP yWX7d    y3zKF     \"]"))\
    .click()
# Boucle d'abonnement aux suggestions d'amis
while True:
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("[" + current_time + "] Boucle d'abonnement aux suggestions d'amis")
    for i in range(30):
        driver.find_element_by_xpath(("//button[@class=\"sqdOP  L3NKy   y3zKF     \"]"))\
            .click()
        sleep(1)
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("[" + current_time + "] Pause de 3 minutes pour éviter la détection du bot par Instagram")
    sleep(180)

# Creado por Bani Montoya 2016-2017


from selenium import webdriver
import time
import secrets

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--no-startup-window')
chrome_options.add_argument("--mute-audio")
chrome_options.add_argument("--Referer=https://www.facebook.com")
driver = webdriver.Chrome(
    executable_path="/Users/pbsoft/bot_bitmagnet/chromedriver", chrome_options=chrome_options)

urls = []

urls.append("https://www.link1.com")
urls.append("https://www.link2.com")
# urls.append("etc...")

ran = secrets.SystemRandom().randrange(0, 15, 5)


def navegador(url):

    time.sleep(ran)
    driver.get(url)
    time.sleep(ran)

for url in urls:
    navegador(url)
driver.close()

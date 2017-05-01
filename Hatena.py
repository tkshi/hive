from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
chrome_options = Options()

class Hatena:
    def __init__(self,username,password,proxyserver):
        cp = webdriver.ChromeOptions()
        cp.add_argument('--proxy-server={}'.format(proxyserver))
        self.__driver = webdriver.Chrome(chrome_options=cp)
        self.__driver.implicitly_wait(1)
        self.__driver.get("https://www.hatena.ne.jp/login")
        usernameElem = self.__driver.find_element_by_css_selector("#login-name")
        passwordElem = self.__driver.find_element_by_css_selector("#container > div > form > div > div:nth-child(2) > div > input")
        enterElem = self.__driver.find_element_by_css_selector("#option > input")
        usernameElem.send_keys(username)
        passwordElem.send_keys(password)
        enterElem.click()
        waitElem = self.__driver.find_element_by_css_selector('#aside > div.profile-box.for-pc > div > a.username')
    def close(self):
        self.__driver.close()
    def bookmark(self,url):
        self.__driver.get('http://b.hatena.ne.jp/mako83/add.confirm?url={}'.format(url))
        saveElem = self.__driver.find_element_by_css_selector("#submit-button")
        saveElem.click()

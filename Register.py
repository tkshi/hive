from selenium import webdriver

class Register:
    def __init__(self,proxyserver):
        cp = webdriver.ChromeOptions()
        cp.add_argument('--proxy-server={}'.format(proxyserver))
        self.__driver = webdriver.Chrome(chrome_options=cp)
        self.__driver.implicitly_wait(1)
        self.__driver.get("https://10minutemail.com/")
        self.__emailAdress = self.__driver.find_element_by_css_selector('#mailAddress').get_attribute('value')
    def getEmailAdress(self):
        return self.__emailAdress
    def clickHatenaRegisterLink(self):
        self.__driver.get("https://10minutemail.com/")
        self.__driver.find_element_by_css_selector('#ui-id-1').click()
        self.__driver.find_element_by_css_selector('#ui-id-2 > div > p > a:nth-child(9)').click()

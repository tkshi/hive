from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

chrome_options = Options()

cp = webdriver.ChromeOptions()
cp.add_argument('--proxy-server=23.19.83.210:8800')
driver = webdriver.Chrome(chrome_options=cp)
driver.get("https://www.cman.jp/network/support/go_access.cgi")
# assert "Python" in driver.title
# elem = driver.find_element_by_name("q")
# elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
driver.close()

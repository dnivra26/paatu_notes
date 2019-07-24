from selenium import webdriver
import os
import time
from selenium.webdriver.chrome.options import Options  
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

chrome_options = Options()  
chrome_options.add_argument("--headless")  

browser = webdriver.Chrome(executable_path=os.path.abspath("chromedriver"), options=chrome_options)
browser.get("http://web.archive.org/web/20190628165326/http://www.tfmpage.com/notes/")

iframe = browser.find_element_by_tag_name("iframe")


browser.switch_to.default_content()
browser.switch_to.frame(iframe)
iframe_source = browser.page_source


print(iframe_source) #returns iframe source
# print(browser.current_url) #returns iframe URL


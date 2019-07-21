# -*- coding: utf-8 -*-
"""
Created on Thu May 16 06:13:40 2019

@author: Sahil
"""
"""
http://forsk.in/images/Forsk_logo_bw.png"

Download the image from the url above and store in your workking diretory with the same
name as the image name.

Do not hardcode the name of the image


"""

import urllib.request
from selenium import webdriver

source ="http://forsk.in/images/Forsk_logo_bw.png"


driver = webdriver.Firefox(executable_path=r'G:/geckodriver.exe')
driver.get(source)

image = driver.find_element_by_xpath("/html/body/img")

src = image.get_attribute('src')

urllib.request.urlretrieve(src, "Forsk_logo_bw.png")

driver.close()
   


"----------------------------------------------"

from selenium import webdriver

source ="http://forsk.in/images/Forsk_logo_bw.png"


driver = webdriver.Firefox(executable_path=r'G:/geckodriver.exe')
driver.get(source)
image = driver.get_screenshot_as_file("Forsk_logo_bw2.png")


"------------------------------------------"



"""


take a screenshot

from selenium import webdriver

driver = webdriver.Firefox()
driver.get('https://moscowsg.megafon.ru/ps/scc/php/cryptographp.php?PHPSESSID=mfc540jkbeme81qjvh5t0v0bnjdr7oc6&ref=114&w=150')

driver.save_screenshot("screenshot.png")

driver.close()
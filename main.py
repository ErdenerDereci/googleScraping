import os
import selenium
from selenium import webdriver
import time
import urllib.request
import numpy as np
from tqdm import tqdm
sleeps = [1,0.5,1.5,0.7]
import io
import requests

from selenium.common.exceptions import ElementClickInterceptedException
DRIVER_PATH = "C:\\Users\\x\\Desktop\\chromedriver"
driver = webdriver.Chrome(executable_path=DRIVER_PATH)


search_url='https://www.google.com/search?q={q}&tbm=isch&tbs=sur%3Afc&hl=en&ved=0CAIQpwVqFwoTCKCa1c6s4-oCFQAAAAAdAAAAABAC&biw=1251&bih=568'
driver.get(search_url.format(q='orchid flowers'))

#Scroll to the end of the page
page_scroll_sleep = 2

#Get scroll heigh
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
        # Scroll down to bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Wait to load page
        time.sleep(page_scroll_sleep)

        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")

        if new_height == last_height:
        #break #insert press load more
            try:
                element = driver.find_elements_by_class_name('mye4qd') #returns list
                element[0].click()
            except:
                break
        last_height = new_height

#image linkleri aliniyor
image_links = driver.find_elements_by_class_name('rg_i.Q4LuWd')

src_links = [image_links[i].get_attribute('src') for i in range(len(image_links))]
data_src_links = [image_links[i].get_attribute('data-src') for i in range(len(image_links))]

print(len(data_src_links))

# urllib save images into folder and renames using data_name string
for i, link in enumerate(tqdm(data_src_links)):
    if link is not None:
        name = "orchidFlower" + f'{i}.jpeg'
        urllib.request.urlretrieve(link, name)
        time.sleep(np.random.choice(sleeps))

driver.quit()
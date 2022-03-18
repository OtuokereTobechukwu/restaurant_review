import pandas as pd
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

import time

# Get the chrome driver nad wait for the page to load
print('Getting the content of the webpage ........')
driver = webdriver.Chrome(executable_path='/Users/Toby_Py/Documents/chromedriver')
driver.get('https://www.tripadvisor.com/Restaurants-g304026-Lagos_Lagos_State.html')

time.sleep(10)

# For every item in the list of restarants:
table = driver.find_element(by=By.XPATH,value= '//*[@id="component_2"]/div')

restaurant_list = table.find_elements(by=By.CLASS_NAME, value = 'OhCyu')

ActionChains(driver).move_to_element(restaurant_list[0]).key_down(Keys.COMMAND).click(restaurant_list[0]).key_up(Keys.COMMAND).perform()
print('Pressed')

# print(restaurant_list)
#     # Get name of restaurant
#         # Restaurant name class attribute : 'OhCyu'
#     # Click(go the the restataurant details) and get:
#         # number of reviews -> <a class="dUfZJ" href="#REVIEWS">481 reviews</a>
#         # Rating -> <span class="fdsdx">4.5<!-- -->&nbsp;</span>
#         # Comments -> <p class="partial_entry">Awesome place with great ambience. 


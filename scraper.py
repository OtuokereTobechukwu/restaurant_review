import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
import time

# Get the chrome driver nad wait for the page to load
print('Getting the content of the webpage ........')
driver = webdriver.Chrome(executable_path='/Users/Toby_Py/Documents/chromedriver')
driver.get('https://www.tripadvisor.com/Restaurants-g304026-Lagos_Lagos_State.html')


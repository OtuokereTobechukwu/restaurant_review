import pandas as pd
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

# Get the chrome driver nad wait for the page to load
driver = webdriver.Chrome(executable_path='/Users/Toby_Py/Documents/chromedriver')
# Open the url
driver.get('https://www.tripadvisor.com/Restaurants-g304026-Lagos_Lagos_State.html')

# Save the restaurant window
def get_restaurant_window():
    restaurant_window = driver.window_handles[0]
    return restaurant_window
# driver.switch_to.window()




def fetchRestaurantDetails(parent):
    names = []
    reviews = []
    ratings = []

    restaurant_list = parent.find_elements(by=By.CLASS_NAME, value = 'OhCyu')

    for restaurant in restaurant_list:
        ActionChains(driver).move_to_element(restaurant).key_down(Keys.COMMAND).click(restaurant).key_up(Keys.COMMAND).perform()
        driver.switch_to.window(driver.window_handles[1])
        time.sleep(2)

        restaurant_details = driver.find_element(by=By.CLASS_NAME, value= 'page') # Details mainpage

        # Fetch those Damn attributes
        name = restaurant_details.find_element(by=By.CLASS_NAME, value='fHibz').text
        review = restaurant_details.find_element(by=By.CLASS_NAME, value='dUfZJ').text
        rating = restaurant_details.find_element(by=By.CLASS_NAME, value='fdsdx').text

        names.append(name)
        reviews.append(review)
        ratings.append(rating)

        driver.close()
        driver.switch_to.window(get_restaurant_window())

    return names, reviews, ratings


def transformToDataframe(details):
    names,review,ratings = details
    restaurant_data = {'name':[], 'reviews':[], 'ratings':[]}

    restaurant_data['name'] = names
    restaurant_data['reviews'] = review
    restaurant_data['ratings'] = ratings

    data = pd.DataFrame.from_dict(restaurant_data)

    return data



# Main Program
# ----------------------------------------------------------------

# Parent table with restaurant listings
parent_table = driver.find_element(by=By.XPATH,value= '//*[@id="component_2"]/div')

# Fetch the details of the restaurant
details = fetchRestaurantDetails(parent_table)

# Transform the details of the restaurant into a dataframe
data = transformToDataframe(details)


print(data)







# print(restaurant_list)
#     # Get name of restaurant
#         # Restaurant name class attribute : 'OhCyu'
#     # Click(go the the restataurant details) and get:
#         # number of reviews -> <a class="dUfZJ" href="#REVIEWS">481 reviews</a>
#         # Rating -> <span class="fdsdx">4.5<!-- -->&nbsp;</span>
#         # Comments -> <p class="partial_entry">Awesome place with great ambience. 


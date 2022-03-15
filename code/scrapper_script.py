# This script scrapes google images for pictures based on the search term
# Run this script in the directory where the images are to be downloaded

# Imports Packages
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Opens Firefox
driver = webdriver.Firefox()

def scroll_down():
    # Keeps scrolling down google images until it reaches the end of the webpage
    last_height = driver.execute_script('return document.body.scrollHeight')
    while True:
        driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
        time.sleep(2)
        new_height = driver.execute_script('return document.body.scrollHeight')
        try:
            driver.find_element_by_xpath('//*[@id="islmp"]/div/div/div/div/div[5]/input').click()
            time.sleep(5)
        except:
            pass
        if new_height == last_height:
            break
        last_height = new_height

# gets the images from google
def download_images(search_term):
    # Go to google images
    driver.get('https://www.google.ca/imghp?hl=en&tab=ri&authuser=0&ogbl')

    
    # Go to search bar, enter search term & get results
    box = driver.find_element_by_xpath("/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div[2]/div[2]/input")
    box.send_keys(search_term)
    box.send_keys(Keys.ENTER)

    print("Downloading images for search term ***"+search_term+"***")

    # Scroll to the end o the page 
    scroll_down()

    # Download images
    for i in range(1, 100):
        try:
            driver.find_element_by_xpath('/html/body/div[2]/c-wiz/div[3]/div[1]/div/div/div/div[1]/div[1]/span/div[1]/div[1]/div['+str(i)+']/a[1]/div[1]/img').screenshot(search_term+'-'+str(i)+'.png')
            print(i, " images downloaded")
            time.sleep(1)
        except:
            pass


# ---------------------------------MAIN-------------------------------------
terms = ["glasses", "eyeware", "medicated glasses", "spectacles", "spectacle frames"]

for t in terms:
    download_images(t)

# Close the browser after all the scraping
driver.close()
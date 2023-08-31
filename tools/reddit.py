import argparse, urllib.request, datetime, os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def download_reddit(video_url, save_directory):
    options = webdriver.ChromeOptions()

    # Hide all selenium informations 
    options.add_argument('--headless')
    options.add_experimental_option('excludeSwitches', ['enable-logging'])

    browser = webdriver.Chrome(options=options)
    browser.get(video_url)

    title = get_title(video_url)

    #get video source from link
    try:
        video_link = (browser.find_element(By.TAG_NAME, 'shreddit-player')).get_attribute("src")
        urllib.request.urlretrieve(video_link, save_directory+ "\\" + title+".mp4")
        
    except:
        print("Video host elsewere")
        video_link = (browser.find_element(By.TAG_NAME, 'a')).get_attribute("href")
        print(video_link)
        input("is this link valid ?")
        return 0

    browser.quit()
    return 1
    
def get_title(video_url):
    title_temp = video_url.split("/")
    title = title_temp[7]
    return title

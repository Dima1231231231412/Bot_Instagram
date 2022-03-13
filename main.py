from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from auth_data import username,password
import time
import random
from selenium.webdriver.common.by import By

def login(username,password):
    browser = webdriver.Chrome('chromedriver/chromedriver.exe')
    try:
        browser.get('https://www.instagram.com')
        time.sleep(random.randrange(3,5))

        username_input = browser.find_element(By.NAME,'username')
        username_input.clear()
        username_input.send_keys(username)
        time.sleep(2)
        password_input = browser.find_element(By.NAME,'password')
        password_input.clear()
        password_input.send_keys(password)

        password_input.send_keys(Keys.ENTER)
        time.sleep(10)
        browser.close()
        browser.quit()
    except Exception as _ex:
        print(_ex)
        browser.close()
        browser.quit()

def hashtag_search(username,password,hashtag):
    browser = webdriver.Chrome('chromedriver/chromedriver.exe')
    try:
        browser.get('https://www.instagram.com')
        time.sleep(random.randrange(3, 5))

        username_input = browser.find_element(By.NAME,'username')
        username_input.clear()
        username_input.send_keys(username)
        time.sleep(2)
        password_input = browser.find_element(By.NAME,'password')
        password_input.clear()
        password_input.send_keys(password)

        password_input.send_keys(Keys.ENTER)
        time.sleep(10)


        try:
            browser.get(f'https://www.instagram.com/explore/tags/{hashtag}/')
            time.sleep(5)

            # for i in range(1,4):
            #     browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            #     time.sleep(random.randrange(3,5))

            hrefs = browser.find_elements_by_tag_name('a')

            posts_urls = []
            for item in hrefs:
                href = item.get_attribute('href')
                if "/p/" in href:
                    posts_urls.append(href)
                    print(posts_urls)

            for url in posts_urls[0:50]:
               try:
                    browser.get(url)
                    time.sleep(10)
                    like_button = "/html/body/div[1]/section/main/div/div[1]/article/div/div[2]/div/div[2]/section[1]/span[1]/button"
                    browser.find_element(By.XPATH,like_button).click()

               except Exception as ex:
                   print(ex)


            browser.close()
            browser.quit()

        except Exception as _ex:
            print(_ex)
            browser.close()
            browser.quit()

    except Exception as _ex:
        print(_ex)
        browser.close()
        browser.quit()

hashtag_search(username,password,'surfing')
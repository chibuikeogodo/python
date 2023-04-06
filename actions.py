import undetected_chromedriver as uc
from selenium.webdriver.support.ui import WebDriverWait
import json
import os
from random import choice
import profile

from csv import DictReader
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from user_agent import UserAgents
import random

Random_UserAgent = random.randint(0, 20)

ip_check = 'https://www.whatismyip.com/'
home = 'https://www.youtube.com'
login = 'https://accounts.google.com/AddSession/identifier?continue=https%3A%2F%2Fwww.youtube.com%2Fsignin%3Faction_handle_signin%3Dtrue%26app%3Ddesktop%26hl%3Den%26next%3D%252F&hl=en&passive=false&service=youtube&uilel=0&flowName=GlifWebSignIn&flowEntry=AddSession'
channel = 'https://www.youtube.com/channel/UCL6a78YrKYlFHHYP7nOGizA/videos'


class Bot:
    def __init__(self, username, password, user_agent, cooki):
        self.username = username
        self.password = password
        self.user_agent = user_agent
        self.cooki = cooki

    def get_user(self):
        return self.username

    def get_password(self):
        return self.password

    def get_user_agent(self):
        return self.user_agent

    def get_cooki(self,):
        return self.cooki

    def StartBot(self):
        options = {
            'proxy': {
                'http': 'http://dccqufed:y28brsn1p7ee@154.95.32.23:5076',
                'https': 'https://dccqufed:y28brsn1p7ee@154.95.32.23:5076',
            }
        }
        driver = uc.Chrome(use_subprocess=True, seleniumwire_options=options)
        driver.execute_cdp_cmd('Network.setUserAgentOverride', {
            "userAgent": self.user_agent})
        print(driver.execute_script("return navigator.userAgent;"))

        driver.get('https://www.google.com/')

        time.sleep(40)
        print('Checking for saved cookies.......')
        if os.path.exists(self.cooki):
            with open(self.cooki) as cookie_file:
                cookies = json.loads(cookie_file.read())
            for cookie in cookies:
                driver.add_cookie(cookie)
            driver.refresh()
            print('I have logged in successful using my saved cookies.......... ')
        else:
            print('Sorry, No cookies was saved, let me login and save my cookies for next time Login...........')
            driver.get(login)
            driver.find_element_by_name('identifier').send_keys(self.username)
            driver.find_element_by_xpath('//*[@id="identifierNext"]/div/button/span').click()
            time.sleep(3)
            driver.find_element_by_name('password').send_keys(self.password)
            driver.find_element_by_xpath('//*[@id="passwordNext"]/div/button/span').click()
            time.sleep(3)
            print('Login was successful.........')
            print("Now Let's save my cookies for next time..........")
            cookies = driver.get_cookies()
            with open(self.cooki, 'w', newline='') as outputdata:
                json.dump(cookies, outputdata)
                print('Cookies saved............')

        time.sleep(3)
        driver.get(channel)
        time.sleep(random.randint(3, 5))
        videos = driver.find_elements_by_class_name('style-scope ytd-grid-renderer')
        videos2 = driver.find_elements_by_xpath('//*[@id="app"]/div[1]/ytm-browse/ytm-single-column-browse-results-renderer/div[2]/div[2]/ytm-section-list-renderer/lazy-list/ytm-item-section-renderer/lazy-list/ytm-compact-video-renderer[1]')
        for video in videos2:
            title = video.find_element_by_class_name('compact-media-item-headline')
            title.click()
        time.sleep(150)

user1 = Bot('Femismart565@gmail.com', 'Smart123@', 'Mozilla/5.0 (Linux; Android 9; TECNO CC6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.79 Mobile Safari/537.36', 'cookies13.json')
user2 = Bot('nwamenemicheal@gmail.com', 'Micheal123', 'Mozilla/5.0 (Linux; Android 11; SM-G998W) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Mobile Safari/537.36', 'cookies12.json')

#user1.StartBot()
user2.StartBot()

time.sleep(random.randint(2, 4))
        if os.path.exists(f'cookies/{self.cookies}'):
            with open(f'cookies/{self.cookies}') as cookie_file:
                cookies = json.loads(cookie_file.read())
            for cookie in cookies:
                driver.add_cookie(cookie)
            driver.refresh()
        else:
            print('Sorry, No cookies was saved, let me login and save my cookies for next time Login...........')
            driver.get(login)
            driver.find_element_by_name('identifier').send_keys(username)
            driver.find_element_by_xpath('//*[@id="identifierNext"]/div/button/span').click()
            time.sleep(3)
            driver.find_element_by_name('password').send_keys(password)
            driver.find_element_by_xpath('//*[@id="passwordNext"]/div/button/span').click()
            time.sleep(3)
            print('Login was successful.........')
            print("Now Let's save my cookies for next time..........")
            cookies = driver.get_cookies()
            with open(f'cookies/{self.cookies}', 'w', newline='') as outputdata:
                json.dump(cookies, outputdata)
                print('Cookies saved............')
        time.sleep(2)
        driver.get(random.choice(videos_channels))
        time.sleep(2)
        try:
            # This is to play videos on Mobile phones
            videos2 = driver.find_elements_by_xpath(
                '//*[@id="app"]/div[1]/ytm-browse/ytm-single-column-browse-results-renderer/div[2]/div[2]/ytm-section-list-renderer/lazy-list/ytm-item-section-renderer/lazy-list/ytm-compact-video-renderer[1]')
            for video in videos2:
                title = video.find_element_by_class_name('compact-media-item-headline')
                title.click()
        except:
            print('This is not mobile')
        else:
            # This is to play videos on Desktop
            videos = driver.find_elements_by_class_name('style-scope ytd-grid-renderer')
            for video in videos:
                title = video.find_element_by_xpath('//*[@id="video-title"]')
                title.click()
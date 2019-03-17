from datetime import datetime, time
from getpass import getpass
from selenium import webdriver
from time import sleep

username = ''
password = ''
reserver_code = ''
with open('credential.txt') as f:
    username = f.readline().strip()
    password = f.readline().strip()
with open('reserver.js') as f:
    reserver_code = f.read()
driver = webdriver.Chrome()
driver.get('http://hi.hana.hs.kr')
username_box = driver.find_element_by_name('login_id')
username_box.send_keys(username)
password_box = driver.find_element_by_name('login_pw')
password_box.send_keys(password)
password_box.submit()
start_time = 13 if datetime.today().weekday() < 5 else 12
print('waiting until %d PM' % (start_time))
while time(start_time, 0) >= datetime.today().time():
    sleep(0.1)
driver.execute_script(reserver_code)

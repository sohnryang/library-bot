import requests

from colorama import init, Fore, Back, Style
from datetime import datetime, time
from sys import exit
from time import sleep

init()

username = ''
password = ''
with open('../credential.txt') as f:
    username = f.readline().strip()
    password = f.readline().strip()
baseurl = 'http://hi.hana.hs.kr'
login_url = '/proc/login_proc.asp'
sess = requests.Session()

def login(second=False):
    if second:
        print(Fore.BLUE + 'Relogging in' + Style.RESET_ALL)
    else:
        print(Fore.BLUE + 'Logging in' + Style.RESET_ALL)
    data = {'login_id': username, 'login_pw': password}
    response = sess.post(baseurl + login_url, data=data)
    if int(response.headers['Content-Length']) < 1000:
        print(Fore.RED + 'Failed to login' + Style.RESET_ALL)
        exit(1)
    print(Fore.GREEN + 'Logged in' + Style.RESET_ALL)

login()

start_time = 13 if datetime.today().weekday() < 5 else 12
print(Fore.YELLOW + 'Waiting until doomsday' + Style.RESET_ALL)
while time(start_time, 0) >= datetime.today().time():
    sleep(0.1)
print('Ready to flood the server')

library_url = '/SYSTEM_Plan/Lib_System/Lib_System_Reservation' + \
              '/reservation_exec.asp'
if datetime.today().weekday() < 5:
    time_codes = {1, 4}
else:
    time_codes = {6, 7, 8, 9, 10}

try:
    for reserve_time in time_codes:
        print(Fore.CYAN + \
              ('Trying time code %d' % (reserve_time)) + Style.RESET_ALL)
        for seat in range(1, 73):
            print('  for seat #%d... ' % (seat), end='')
            data = {'code': '001', 's_code': seat, 't_code': reserve_time}
            response = sess.post(baseurl + library_url, data=data)
            print(response.text[:55] + \
                  (response.text[:55] and '..') + ' ', end='')
            if '되었습니다' in response.text and '비정상' not in response.text:
                print(Fore.GREEN + 'OK' + Style.RESET_ALL)
                break
            elif '비정상' in response.text or '로그아웃' in response.text:
                print(Fore.YELLOW + 'RETRY' + Style.RESET_ALL)
                login(second=True)
            else:
                print(Fore.RED + 'FAIL' + Style.RESET_ALL)
except InterruptedError:
    print(Fore.YELLOW + 'Aborting the bot' + Style.RESET_ALL)

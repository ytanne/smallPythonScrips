import requests

login = 'yerzhan.orazayev' #enter login
password = 'Infinitive27' #enter password

URL = 'https://my.nu.edu.kz/wps/portal/hidden/login/!ut/p/b1/04_Sj9CPykssy0xPLMnMz0vMAfGjzOKd3R09TMx9DAwsfNxNDTwdPUKDLAONjQ1czYEKIoEKDHAARwNC-sP1o_AqCTSBKsBjhZ9Hfm6qfkFuhEGWiaMiAFWLnI8!/dl4/d5/L2dBISEvZ0FBIS9nQSEh/pw/Z7_2OQEAB1A0GNQE0Q8VHS8J11082/act/id=0/411224603167/-/?login=' + login + '&password=' + password + '&loginSubmit=Login'
photo_url = 'https://my.nu.edu.kz/.AccountPage/GetPhoto?uid=201416473'

PARAMS = {'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
          'Accept-Encoding':'gzip, deflate, br',
          'Accept-Language':'en-US,en;q=0.5',
          'Connection':'keep-alive',
          'Cookie':'JSESSIONID=0000s1HwpwMLJaaD1CamWilE-zu:18mmbeoo2',
          'DNT':'1',
          'Host':'my.nu.edu.kz',
          'Referer':'https://my.nu.edu.kz/wps/myportal/student/home/homeinfo/!ut/p/b1/04_Sj9Q1tLQ0MzAwMjS20I_Qj8pLLMtMTyzJzM9LzAHxo8zijfwDXR2dDB0N3H0MzQwcvb0CTd3MLY2cfU2BCiKBCgxwAEcDQvrD9aPwKTFwMYEqwGOFn0d-bqp-blSOpaeuoyIAWrd3Qw!!/dl4/d5/L2dBISEvZ0FBIS9nQSEh/',
          'Upgrade-Insecure-Requests':'1',
          'User-Agent':'Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:63.0) Gecko/20100101 Firefox/63.0'
          }

response_json = requests.get(url = photo_url)#, params = PARAMS)

session = requests.Session()

response_json2 = session.get(URL)

print(response_json)
'''

with requests.Session() as s:
    p = s.get(url = URL, params = PARAMS)
    
    r = s.get('http://my.nu.edu.kz/.AccountPage/StudentCard?uid=201747150')
    
    print(r.cookies)

'''
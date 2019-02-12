import requests

login = 'N4M3' #enter login
password = 'P4SSW0RD' #enter password

URL = 'https://my.nu.edu.kz/wps/portal/student/!ut/p/b1/04_Sj9CPykssy0xPLMnMz0vM0Q_0yU9PT03xLy0BSUWZxRv5B7o6Ohk6Grj7GJoZOHp7BZq6mVsaGYQYAhVEAhUY4ACOBoT0h-tH4VXiYwZVgMcKP4R7CzJyLD11HRUBTJ2PsA!!/dl4/d5/L2dBISEvZ0FBIS9nQSEh/pw/Z7_2OQEAB1A0GUP70Q8T8QUCT00G5/act/id=0/405190959087/-/?login=' + login + '&password=' + password + '&loginSubmit=Login'

PARAMS = {'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
          'Accept-Encoding':'gzip, deflate, br',
          'Accept-Language':'en-US,en;q=0.5',
          'Connection':'keep-alive',
          'Host':'my.nu.edu.kz',
          'Referer':'https://my.nu.edu.kz/wps/myportal/student/home/homeinfo/!ut/p/b1/04_Sj9Q1tLQ0MzAwMjS20I_Qj8pLLMtMTyzJzM9LzAHxo8zijfwDXR2dDB0N3H0MzQwcvb0CTd3MLY2cfU2BCiKBCgxwAEcDQvrD9aPwKTFwMYEqwGOFn0d-bqp-blSOpaeuoyIAWrd3Qw!!/dl4/d5/L2dBISEvZ0FBIS9nQSEh/',
          'Upgrade-Insecure-Requests':'1',
          'User-Agent':'Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:63.0) Gecko/20100101 Firefox/63.0'
          }

with requests.Session() as s:
    p = s.get(url = URL, params = PARAMS)
    
    r = s.get('http://my.nu.edu.kz/.AccountPage/StudentCard?uid=201747150')
    
    print r.text
    

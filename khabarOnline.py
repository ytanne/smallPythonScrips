import requests

r = requests.get('https://api.zero.kz/reports/get_online/?data={"site_ids":[55975]}&_=1547795824619')

resp_json = r.json()

peopleOnline = resp_json['result'][0]['clients'];

print('Number of people currently online is: ' + str(peopleOnline));

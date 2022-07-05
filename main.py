#this was made by fknMega on github
import requests


user = input("Enter the tag (username#1234): ")
combotype = input("Enter a number to select combo type, 1 for combo (user:pass:token) or 2 for normal (token): ")

def get_cookies_and_send_friend_request(token, username, discriminator):

    r = requests.Session()
    # gets cookies (100% delicious 😋)
    url = "https://discord.com/api/v9/experiments"
    k = r.get(url)
    
    # sends sex request
    url = "https://discord.com/api/v9/users/@me/relationships"
    headers = {"accept": "/",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "en-US,en-CH;q=0.9,en-GB;q=0.8",
    "authorization": token,
    "content-length": "0",
    "origin": "",
    "referer": "",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.669 Chrome/91.0.4472.164 Electron/13.6.6 Safari/537.36",
    "x-debug-options": "bugReporterEnabled",
    "x-discord-locale": "hu",
    "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJjYW5hcnkiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC42NjkiLCJvc192ZXJzaW9uIjoiMTAuMC4xOTA0MyIsIm9zX2FyY2giOiJ4NjQiLCJzeXN0ZW1fbG9jYWxlIjoiZW4tVVMiLCJjbGllbnRfYnVpbGRfbnVtYmVyIjoxMzMwOTgsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9"
    }
    body = {"username": username, "discriminator": discriminator}
    
    # Send the friend request
    res = r.post(url, headers=headers, json=body)
    

    #print the response

    
    
    return res.status_code


#run the send_friend_request function for every line in the text file
f = open("tokens.txt", "r")
for line in f:
     username = user.split("#")[0]
     discriminator = user.split("#")[1]
     token = ""
     if combotype == "1":
        token = line.split(":")[2].replace("\n", "")
     else:
        token = line.replace("\n", "")

     res = send_friend_request(token, username, discriminator)

     if res == 204:
       print('+ Friend Req sent from: ' + token)
     else:
       if res == 401:
          print('- Token is dead: ' + token)
       else:
          print('- Rate Limit/Verification Required: ' + token)
    



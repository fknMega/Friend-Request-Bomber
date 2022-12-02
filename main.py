# This was made by fknMega on github
# Code upgraded by TKirishima

# Imports
import requests


def send_friend_request(token: str, username: str, discriminator: str) -> int:

    """ Send a friend request by information """


    # Gets cookies 
    r = requests.Session()

    url = "https://discord.com/api/v9/experiments"
    r.get(url)
    
    # Sends friend request
    url = "https://discord.com/api/v9/users/@me/relationships"

    headers = {
        "accept": "/",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "en-US,en-CH;q=0.9,en-GB;q=0.8",
        "authorization": token,
        "content-length": "0",
        "origin": "https://discord.com",
        "referer": "https://discord.com/channels/@me",
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
    

    # Return the response status
    return res.status_code



def main() -> None:

    """ Main program"""

    username, discriminator = input("Enter the tag (username#1234): ").split("#")
    with open("tokens.txt", "r") as f:
        for line in f:
            token = line.split(":")[-1].rstrip("\n")
            res = send_friend_request(token, username, discriminator)

            if res == 204:
                print('\033[32m+\033[0m Friend Req sent from: ' + token)
            elif res == 401:
                print('\033[31m-\033[0m Token is dead: ' + token)
            else:
                print('\033[31m-\033[0m Rate Limit/Verification Required: ' + token)


if __name__ == '__main__':
    main()

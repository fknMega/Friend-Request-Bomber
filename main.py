import requests


user = input("Enter the tag (username#1234): ")
combotype = input("Enter a number to select combo type, 1 for combo (user:pass:token) or 2 for normal (token): ")


def send_friend_request(token, username, discriminator):


    url = "https://discord.com/api/v9/users/@me/relationships"
    headers = {"Content-Type": "application/json", "Authorization": token}
    body = {"username": username, "discriminator": discriminator}
    
    # Send the friend request
    res = requests.post(url, headers=headers, json=body)
    

    #print the response
    print('token: ' + token + ' code: ' + str(res.status_code) + ' message: ' +res.text)

    
    
    return True


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

     send_friend_request(token, username, discriminator)

    

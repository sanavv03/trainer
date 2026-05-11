import random

responses={

    "hi":["hi ! hello how are you doing ... "],
    "bye":["bye....! hope we get to see you again soon...."],
    "default":["you have choosen out of scope reponse pls try again ...sorry for the inconvience "]
}

def get_bot_response(user_message):
    if  user_message in response:
        return ranom.choice(response[user_maessage])
    else :
        return random.choice(response["default"])

while True :
    user_message=input("you : ")
    if user_message.lower() =="quit":
        break
    bot_response=get_bot_response(user_message).lower()
    print(f"bot: {bot_response}")    

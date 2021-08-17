import requests
import string
import random


#-----get string data------#
lc = string.ascii_lowercase
uc = string.ascii_uppercase
num = string.digits


#-----start infinit loop-------#
def loop():
    all = "".join(random.choice(lc + uc + num)for i in range(16))
    nitro  = "https://discord.gift/" + all




    #-------CHECKER-------#
    respond = requests.get("https://discordapp.com/api/v6/entitlements/gift-codes/" + nitro + "?with_application=false&with_subscription_plan=true")


    #----if code valid save it in a file------#
    if respond.status_code == 200:
        print("valid | " + nitro)
        vc = open("valid codes.txt", "a")
        vc.write(nitro + "\n")
        vc.close
        loop()

    else:
        print("Invalid | " + nitro)
        loop()

loop()
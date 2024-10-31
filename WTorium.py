from  colorama import init, Fore
import requests, time, os, random, fade
def webhokshit():
    color = Fore.LIGHTMAGENTA_EX
    color2 = Fore.LIGHTRED_EX
    # This code was a reuse from my multitool and really shit but ion care :P
    # use it if you want but dont skid it cause its ass
    os.system("cls")
    uwupancake = """
░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓████████▓▒░▒▓██████▓▒░░▒▓███████▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓██████████████▓▒░  
░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░  ░▒▓█▓▒░  ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░  ░▒▓█▓▒░  ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░  ░▒▓█▓▒░  ░▒▓█▓▒░░▒▓█▓▒░▒▓███████▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░  ░▒▓█▓▒░  ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░ pancake was here
░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░  ░▒▓█▓▒░  ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░ 
 ░▒▓█████████████▓▒░   ░▒▓█▓▒░   ░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░ 
                                                                                                   
                                                                                                   
"""
    uwuprint = fade.water(uwupancake)
    print(uwuprint)
    print(f" {color}1: webhook spammer\n 2: webhook deleter\n 3: webhook checker{Fore.RESET}")
    analpornhub = input("option: ")
    sexboy9 = int(analpornhub)
    def webhookspam1():
        url = input("url; ")
        spamtext = input("message to spam: ")
        delays = input("delay: ")
        randomusernam = input("random usernames? (y or n)")
        sexdelay = float(delays)
        if randomusernam in ["y","Y","yes","Yes","YES"]: # my girl be sayin this (ion got one)
            with open("whusers.txt" , "r") as sexanal:
                sexanus = sexanal.read()
                whnames = sexanus.split("\n")
                while True:
                    whname = random.choice(whnames)
                    headers = {
                        "username": whname,
                        "content": spamtext
                        }
                    time.sleep(sexdelay)
                    sexyboyrape = requests.post(url, data=headers)
                    if sexyboyrape.status_code == 204:
                        print(f"sent message to webhook as {whname}")
                    elif sexyboyrape.status_code == 429:
                        print(f"{color2}ratelimit{Fore.RESET}")
        else:
            headers = {
                "content": spamtext # spam text >-<
                }
        while True:
            time.sleep(sexdelay)
            sexyboyrape = requests.post(url, data=headers)
            if sexyboyrape.status_code == 204:
                print("sent message to webhook")
            elif sexyboyrape.status_code == 429:
                print(f"{color2}ratelimit{Fore.RESET}")
    def webhookdeleterxd():
        sexurl = input("url: ")
        os.system(f"Curl -X DELETE {sexurl}")
        print("webhook deleted.")
        time.sleep(2)
        os.system("cls")
        webhokshit()
    def webhookcheck():
        urlxd = input("url: ")
        analsex = requests.get(urlxd)
        yes = analsex.status_code
        if yes == 200:
            print("webhook is alive")
        elif yes == 403:
            print("webhook alive")
        elif yes == 404:
            print(f"{color2}webhook is deleted{Fore.RESET}") # Retarded ass code but oh well
        time.sleep(3)
        os.system("cls")
        webhokshit()
    if sexboy9 == 1:
        webhookspam1() # Hitler sucks my dick
    if sexboy9 == 2:
        webhookdeleterxd()
    if sexboy9 == 3:
        webhookcheck()
webhokshit()
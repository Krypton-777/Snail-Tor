#!/usr/bin/env python
# -*- encoding: utf-8 -*-

#Set color
R = '\033[31m' # Red
N = '\033[1;37m' # White
G = '\033[32m' # Green
O = '\033[0;33m' # Orange
B = '\033[1;34m' #Blue
def force_to_unicode(text):
	"If text is unicode, it is returned as is. If it's str, convert it to Unicode using UTF-8 encoding"
	return text if isinstance(text, unicode) else text.decod.decode('utf8')

print
print (""+R+"          ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
print (""+R+"          ┃"+N+"03."+N+"            Edit hidden service"+R+"      ┃")
print (""+R+"          ┃"+N+"02."+N+"            Create hidden service"+R+"    ┃")
print (""+R+"          ┃"+N+"01."+N+"            Config"+R+"                   ┃")
print (""+R+"          ┃"+N+"00."+N+"            Exit"+R+"                     ┃")
print (""+R+"          ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛\033[0m")
print
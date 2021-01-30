import json
import urllib.request
from os import R_OK 

filename = open('C:\\Users\\jasse\\OneDrive\\Skrivbord\\Python\\SDKTestApp.json',) 
data = json.load(filename) 
a =[]
exec(open('time.py').read())
for i in data["URLsScanned"]: 
 #print(i)
 a.append(i)
  #Closing file
filename.close()

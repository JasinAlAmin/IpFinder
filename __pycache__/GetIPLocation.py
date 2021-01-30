import json
import urllib.request
from SDKread import a

for i in a :
 try:
    GEO_IP_API_URL  = 'http://ip-api.com/json/'
    IP_TO_SEARCH    = i
    req             = urllib.request.Request(GEO_IP_API_URL+IP_TO_SEARCH)
    response        = urllib.request.urlopen(req).read()
    json_response   = json.loads(response.decode('utf-8'))
    print(json_response['country'] )
 except:
    print(i)
print("Finally finished!")
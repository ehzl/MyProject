import os
import sys
import urllib.request
client_id = "ua6foji7mJ2LXqgjmSju"
client_secret = "er9DdnSZwt"
encText = urllib.parse.quote("번역할 문장을 입력하세요")
data = "source=ko&target=en&text=" + encText
url = "https://openapi.naver.com/v1/language/translate"
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request, data=data.encode("utf-8"))
rescode = response.getcode()
if(rescode==200):
    response_body = response.read()
    print(response_body.decode('utf-8'))
else:
    print("Error Code:" + rescode)

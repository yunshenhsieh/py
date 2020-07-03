from urllib import request

url = 'http://ea4b5b22.ngrok.io/hello_get?name=Allen'
res=request.urlopen(url)
bstr=res.read()
html=bstr.decode('utf-8')
print(html)
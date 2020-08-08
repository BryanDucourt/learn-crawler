from urllib import request
res = request.urlopen('https://www.sogou.com')
print(res.read())
request.urlretrieve('https://www.sougou.com','sogou.html')
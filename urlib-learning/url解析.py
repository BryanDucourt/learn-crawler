from urllib import parse

url = 'https://www.hitwh.edu.cn/sywh/list.htm'
res = parse.urlparse(url)
print(res.scheme)
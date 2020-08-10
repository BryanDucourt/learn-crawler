from urllib import request
# import requests
# url = 'https://piaofang.maoyan.com/dashboard-ajax?orderType=0&uuid=173d235cb17c8-07a2cef3f3025-58321541-144000-173d235cb17c8&riskLevel=71&optimusCode=10 '
#
# header = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.48 Safari/537.36 Edg/85.0.564.23'
# }
#
# #
# rq = request.Request(url, headers=header)
# resp = request.urlopen(rq)
# print(resp.read().decode('utf-8'))
url = 'https://www.biedoul.com/index/3348/'
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.48 Safari/537.36 Edg/85.0.564.23'
}

rq = request.Request(url, headers=header)
resp = request.urlopen(rq)
print(resp.read().decode('utf-8'))
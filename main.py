import requests
import os
import random
import time
from multiprocessing.pool import ThreadPool
from tqdm import tqdm
import urllib3
user_agents = ['Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11',
                    'Opera/9.25 (Windows NT 5.1; U; en)',
                    'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)',
                    'Mozilla/5.0 (compatible; Konqueror/3.5; Linux) KHTML/3.5.5 (like Gecko) (Kubuntu)',
                    'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.12) Gecko/20070731 Ubuntu/dapper-security Firefox/1.5.0.12',
                    'Lynx/2.8.5rel.1 libwww-FM/2.14 SSL-MM/1.4.1 GNUTLS/1.2.9',
                    "Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.7 (KHTML, like Gecko) Ubuntu/11.04 Chromium/16.0.912.77 Chrome/16.0.912.77 Safari/535.7",
                    "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:10.0) Gecko/20100101 Firefox/10.0 ",
]
header = {
    'origin': 'https://www.vlive.tv/',
    'referer': 'https://www.vlive.tv/video/205680',
    'user-agent': random.choice(user_agents),
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6,da;q=0.5,zh-TW;q=0.4',
    'accept': '*/*',
    'accept-encoding': 'gzip, deflate, br',
    'host':'globalv-rmcnmv.akamaized.net',
    'connection':'keep-alive'
}
proxies = ['187.60.46.229:8080','88.87.79.20:8080','139.217.110.76:3128']
  #随机选取一个IP

path = "D:\\spider"
if os.path.exists(path+"vlive200804/"):
    pass
else:
    os.makedirs(path+"vlive200804/")

failure_list = []



def download(num,flag=0):
    url = 'https://globalv-rmcnmv.akamaized.net/c/read/v2/VOD_ALPHA/global_v_2020_08_05_492/hls/84fb4168-d683-11ea-ad8b-246e96398ca5-00{:0>4d}.ts?__gda__=1596606376_56ad3a4725a8cd397d3357d015906fb2'.format(num)
    with open(path + 'vlive200804/'+str(url).split('?')[-2][-7:],'wb') as f:
        try:
            time.sleep(5)
            proxy = {'HTTP': random.choice(proxies)}
            print(proxy)
            header_=header
            print(header_['user-agent'])
            r = requests.get(url , headers=header_, timeout=5)
            r.raise_for_status()
            r.encoding = 'utf-8'
            print('正在下载第{}个片段'.format(num))
            f.write(r.content)
            # r = urllib3.Request(url,headers = header)
            # response = urllib3.urlopen(r)
            # buffer = response.read(1024*256)
            # if not buffer:
            #     raise

            if flag==1:
                failure_list.remove(num)

        except Exception as ex:
            print(ex)
            if num not in failure_list:
                failure_list.append(num)


def get_video():
    files = os.listdir(path + "vlive200804/")
    for file in tqdm(files, desc="transforming:"):
        if os.path.exists(path+"vlive200804/"+file):
            if os.path.getsize('D:\\spidervlive200804\\'+file)==0:
                download(int(file[0:4]))
        #     with open(path + "vlive200804/"+file,'rb') as f1:
        #         with open(path + "vlive200804.mp4",'ab') as f2:
        #             f2.write(f1.read())
        # else:
        #     print('transform failed')


def check_ts():
    print('start to check:')
    while failure_list:
        for num in failure_list:
            download(num, 1)
    print('download successfully')
    get_video()


# if __name__ == '__main__':
#     pool = ThreadPool(100)
#     results = pool.map(download, range(1, 1060+1))
#     pool.close()
#     pool.join()
#
# check_ts()
get_video()
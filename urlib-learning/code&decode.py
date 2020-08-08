from urllib import  parse
#
data = {'name':'杜禹辰','age':18,'greet':'hello world'}
qs = parse.urlencode(data)
print(qs)
print(parse.parse_qs(qs))

# from urllib import request

# data = {'q':'桥本环奈'}
#
# qs1 = parse.urlencode(data)
#
# url = 'https://cn.bing.com/search?'+qs1+'form=ANSPH1&refig=d5aeb54421794921820d83bc539d1785&mkt=zh-cn&pc=U531&sp=-1&pq=qiao%27ben%27huan%27nai&sc=8-17&qs=n&sk=&cvid=d5aeb54421794921820d83bc539d1785'


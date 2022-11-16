import requests
import json
import time
import os
import shutil

d1 = time.strftime('%m.%d',time.localtime(time.time()))
filename = "Z1912核酸截图({})".format(d1)
url = "https://api.huoban.com/v2/item/table/2100000018877814/view/0/filter" # 疫情防控
# url="https://api.huoban.com/v2/item/table/2100000017881517/view/0/filter" # 作业收集

headers = {
    'authorization': 'Bearer IY2vF0iFlXtJ1lhMcdnWfJ9GWy4ZfJEDhtMi3l9n001',
    # 'cookie': '',
    # 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.54 Safari/537.36',
    # 'x-huoban-sensors': '%7B%22visit_type%22%3A%22%E5%86%85%E9%83%A8%E7%B3%BB%E7%BB%9F%22%2C%22client_id%22%3A%221%22%2C%22platform_type%22%3A%22Web%E6%B5%8F%E8%A7%88%E5%99%A8%22%2C%22client_version%22%3A%22v4%22%2C%22is_register%22%3Atrue%2C%22env%22%3A%22prod%22%2C%22_distinct_id%22%3A%222624133%22%2C%22application_url%22%3A%22https%3A%2F%2Fapp.huoban.com%2Ftables%2F2100000018877814%3FviewId%3D0%22%2C%22company_id%22%3A%225100000000315964%22%2C%22space_id%22%3A%224000000003012070%22%7D'
}

data = {
    'limit': '47',
    'offset': '0',
    'field': '2200000177129138',
    'sort': "asc"
}
try:
    os.mkdir('/Users/zhengyunlong/Desktop/{}'.format(filename))
except:
    pass

count = 0
num = 6
dic1 = {}  # 存放 ID:链接
dic2 = {}  # 存放 ID:文件名
dic3 = {}  # 存放 ID:重命名

def kuke():
    url = 'https://api.huoban.com/paasapi/login'#网址
    data = {'username': '15895333618',
            'password': 'Apple778899'}
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.108 Safari/537.36', }
    session = requests.session()
    cookie_jar = session.post(url=url, data=data, headers=headers).cookies
    cookie_t = requests.utils.dict_from_cookiejar(cookie_jar)
    return cookie_t

def spider():
    r = requests.post(url=url, data=json.dumps(data), headers=headers).json()

    for i in range(0, 47):
        try:
            ids = r["items"][i]["fields"][1]["values"][0]["value"]
            name = r["items"][i]["fields"][2]["values"][0]["value"]
            rec1 = r["items"][i]["fields"][num]["values"][0]["link"]["source"]
            rec_name = r["items"][i]["fields"][num]["values"][0]["name"]
            dic1[i + 1] = rec1
            dic2[i + 1] = rec_name
            dic3[i + 1] = str(ids) + "-" + name
        except:

            pass


def begin(b):  # 接收到ID号
    nums = dic2[b]  # 找到dic2中该ID对应的文件名
    strs = ''.join(nums).rindex('.')  # 判断文件名中.的位置
    r = requests.get(dic1[b])  # 取出dic1中该ID对应的链接进行爬取

    with open('/Users/zhengyunlong/Desktop/{}/{}.{}'.format(filename, dic3[b], nums[strs + 1:]), "wb") as code:
        code.write(r.content)


def main_answers():
    global num
    num = 0
    for j in dic3:  # 遍历dic3取出ID
        num = num + 1
        begin(j)

def theend():
    zipfile_path = '/Users/zhengyunlong/Desktop/Z1912今日核酸{}人 ({})'.format(num,d1) # 生成压缩包路径
    # zipfile_path = '/Users/zhengyunlong/Desktop/Z1912作业2'  # 生成压缩包路径
    Date_file = '/Users/zhengyunlong/Desktop/{}'.format(filename) # 原文件夹路径
    shutil.make_archive(zipfile_path, 'zip', Date_file)


start = time.time()
# cook = kuke()
# cookie = "visit_token=1667920889522; HUOBAN_SESSIONID={}; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%222624133%22%2C%22first_id%22%3A%2218457d505df71a-0e1936b62f5651-18525635-1484784-18457d505e0346%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfbG9naW5faWQiOiIyNjI0MTMzIiwiJGlkZW50aXR5X2Nvb2tpZV9pZCI6IjE4NDU3ZDUwNWRmNzFhLTBlMTkzNmI2MmY1NjUxLTE4NTI1NjM1LTE0ODQ3ODQtMTg0NTdkNTA1ZTAzNDYifQ%3D%3D%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%24identity_login_id%22%2C%22value%22%3A%222624133%22%7D%2C%22%24device_id%22%3A%2218457d505df71a-0e1936b62f5651-18525635-1484784-18457d505e0346%22%7D; user_id=2624133; access_token=IY2vF0iFlXtJ1lhMcdnWfJ9GWy4ZfJEDhtMi3l9n001; Hm_lvt_29e645b6615539290daae517d6a073c9=1667920889,1668169980; Hm_lpvt_29e645b6615539290daae517d6a073c9=1668170073; HUOBAN_AUTH={}; HUOBAN_DATA={}".format(cook['HUOBAN_SESSIONID'],cook['HUOBAN_AUTH'],cook['HUOBAN_DATA'])

spider()
main_answers()
end = time.time()
print(end - start)
theend()




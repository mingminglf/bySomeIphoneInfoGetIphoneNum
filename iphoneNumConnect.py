str1="136"
str2="80"
import requests
from phone import Phone
# url="https://tcc.taobao.com/cc/json/mobile_tel_segment.html"
# headers = {
#   "Referer": "https://tcc.taobao.com/",
#   "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
#                 "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36",
# }
p = Phone()
# print(len(str1+str2))
lens=11-len(str1+str2)
size=0
for i in range(10**lens):

    # print(str(i).zfill(6))
    phone=(str1+str(i).zfill(6)+str2)
    if p.find(phone)['city']=='湖南':
        size+=1
        print(phone)
    # print(p.find(phone)['city']=='周口')
print("总数"+str(size))















    # response = requests.get(url, {"tel":phone }, headers=headers,timeout=50)
    # print(response.text)
    # if(response.text.find("河南")):
    #     print(phone)

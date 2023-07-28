import requests

url="https://tcc.taobao.com/cc/json/mobile_tel_segment.html"
headers = {
  "Referer": "https://tcc.taobao.com/",
  "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36",
}
response=requests.get(url,{"tel":12345678910},headers=headers)
print(response.text)
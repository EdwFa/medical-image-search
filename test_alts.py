import requests
import re

url_img = 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/a7/React-icon.svg/1200px-React-icon.svg.png'

print("--- Testing Yandex ---")
yandex_url = f"https://yandex.ru/images/search?rpt=imageview&url={url_img}"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"}
try:
    r_y = requests.get(yandex_url, headers=headers)
    print("Yandex Status:", r_y.status_code)
    # look for signs of captcha
    if "captcha" in r_y.text.lower():
        print("Yandex returned CAPTCHA")
    else:
        # try to find images
        matches = re.findall(r'<img.*?src="(//avatars.mds.yandex.net/get-images-cbir/.*?)"', r_y.text)
        print(f"Yandex found {len(matches)} images")
except Exception as e:
    print("Yandex Error:", e)

print("\n--- Testing Bing ---")
bing_url = f"https://www.bing.com/images/search?q=imgurl:{url_img}&view=detailv2&iss=sbi"
try:
    r_b = requests.get(bing_url, headers=headers)
    print("Bing Status:", r_b.status_code)
    matches = re.findall(r'murl&quot;:&quot;(.*?)&quot;', r_b.text)
    print(f"Bing found {len(matches)} images")
except Exception as e:
    print("Bing Error:", e)

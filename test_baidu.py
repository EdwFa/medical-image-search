import requests
url_img = 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/a7/React-icon.svg/1200px-React-icon.svg.png'
baidu_urls = [
    f"https://graph.baidu.com/details?isfrom=1&source=&image={url_img}",
    f"https://image.baidu.com/search/index?tn=baiduimage&objurl={url_img}"
]
for u in baidu_urls:
    try:
        r = requests.get(u, headers={'User-Agent': 'Mozilla/5.0'})
        print(f"URL: {u[:40]} -> {r.status_code}, len={len(r.text)}")
    except Exception as e:
        print(f"Error: {e}")

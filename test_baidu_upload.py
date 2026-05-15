import requests

url = 'https://graph.baidu.com/upload'
files = {'image': ('test.png', b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x01\x00\x00\x00\x01\x08\x06\x00\x00\x00\x1f\x15\xc4\x89\x00\x00\x00\nIDATx\x9cc\x00\x01\x00\x00\x05\x00\x01\r\n-\xb4\x00\x00\x00\x00IEND\xaeB`\x82', 'image/png')}
data = {'tn': 'pc', 'from': 'pc', 'image_source': 'PC_UPLOAD_SEARCH_FILE', 'extUiData[isLogoShow]': '1'}

r = requests.post(url, files=files, data=data)
print(r.status_code)
print(r.text)

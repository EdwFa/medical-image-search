import requests

url = 'https://openi.nlm.nih.gov/api1?m=1&req=4'
files = {'file': ('test.png', b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x01\x00\x00\x00\x01\x08\x06\x00\x00\x00\x1f\x15\xc4\x89\x00\x00\x00\nIDATx\x9cc\x00\x01\x00\x00\x05\x00\x01\r\n-\xb4\x00\x00\x00\x00IEND\xaeB`\x82', 'image/png')}

r = requests.post(url, files=files, allow_redirects=False)
print("Status Code:", r.status_code)
print("Headers:", r.headers)
print("Text:", r.text[:200])

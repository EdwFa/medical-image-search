import requests
import re
import json

url = 'https://lens.google.com/uploadbyurl?url=https://upload.wikimedia.org/wikipedia/commons/thumb/a/a7/React-icon.svg/1200px-React-icon.svg.png&hl=en'
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
}
cookies = {
    'SOCS': 'CAESHAgBEhJnd3NfMjAyMzA4MTAtMF9SQzIaAmVuIAEaBgiA_LyaBg'
}
r = requests.get(url, headers=headers, cookies=cookies)
with open("lens_test_final.html", "w", encoding="utf-8") as f:
    f.write(r.text)

# Let's search for "encrypted-tbn" inside the text
images = re.findall(r'https://encrypted-tbn0.gstatic.com/images\?q=tbn:[^"\\]+', r.text)
print(f"Found {len(images)} thumbnail images")

# Let's search for "AF_initDataCallback"
matches = re.findall(r'AF_initDataCallback', r.text)
print(f"Found {len(matches)} AF_initDataCallback")

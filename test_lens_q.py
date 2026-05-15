import requests
r = requests.get('https://lens.google.com/uploadbyurl?url=https://upload.wikimedia.org/wikipedia/commons/thumb/a/a7/React-icon.svg/1200px-React-icon.svg.png&q=site:ncbi.nlm.nih.gov', headers={'User-Agent': 'Mozilla/5.0'})
print(r.status_code)
print(len(r.text))

import requests
import json



keyword = "milk"
headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Referer': 'https://www.amazon.com/',
    'Origin': 'https://www.amazon.com',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.96 Safari/537.36',
}
params = (
    # ('session-id', '138-5360927-5076949'),
    # ('customer-id', ''),
    # ('request-id', 'B3SX1MKWFVPY1CCQQZTN'),
    ('page-type', 'Gateway'),
    ('lop', 'en_US'),
    ('site-variant', 'desktop'),
    ('client-info', 'amazon-search-ui'),
    ('mid', 'ATVPDKIKX0DER'),
    ('alias', 'aps'),
    ('suggestion-type', 'keyword'),
    # ('b2b', '0'),
    # ('fresh', '0'),
    ('ks', '75'),
    ('prefix', keyword),
)
response = requests.get('https://completion.amazon.com/api/2017/suggestions', headers=headers, params=params)
js = json.loads(response.text)
# print(js["suggestions"])
for kw in js["suggestions"]:
    if kw['value'] != keyword:
        print(kw['value'])
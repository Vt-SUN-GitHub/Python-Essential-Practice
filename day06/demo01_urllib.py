import urllib.request

url = 'http://47.93.129.77'

response = urllib.request.urlopen(url)

if response.getcode() == 200:
    print(response.info())
    html_text = response.read().decode("utf-8")
    with open("htmlText.html", mode='w', encoding='utf-8') as fp:
        fp.write(html_text)
        ...
    ...



import requests
from lxml import etree

# 伪装头
headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36",
}

# 下载
url = 'http://www.147xiaoshuo.com/book/8254/123812.html'
res = requests.get(url, headers=headers)
res.encoding = res.apparent_encoding  # 万能编码

# 解析
html = etree.HTML(res.text, etree.HTMLParser())
novels_url = html.xpath('//p/text()')
# print(novel_url)

# 保存
for novel in novels_url:
    # print(novel)
    with open('xx.txt', 'a+', encoding='utf8')as f:
        f.writelines(novel)
        f.write("\n")


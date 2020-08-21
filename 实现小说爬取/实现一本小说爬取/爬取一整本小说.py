import requests
from lxml import etree
import time
# from pachong_tools.url_headers import *

# 伪装头
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
}
# proxies = proxies
n = 1
for i in range(7698, 8386):
    # 下载
    time.sleep(5)
    print('第%s章正在下载中...' % n)
    n += 1
    print('休息一下,5秒钟呦...')
    url = 'http://www.douluodalu1.com/douluodalu/%s.html' % i
    # res = requests.get(url, headers=headers,proxies=proxies)
    res = requests.get(url, headers=headers)
    res.encoding = res.apparent_encoding  # 万能编码

    # 解析
    html = etree.HTML(res.text, etree.HTMLParser())
    novels_url = html.xpath('//p/text()')
    # print(title_txt)

    # 保存
    for novel in novels_url:
        # print(novel)
        title_txt = html.xpath('//title/text()')  # 小说章节名字
        with open('%s.txt' % title_txt[0], 'a+', encoding='utf8')as f:
            # print('章节名:',title_txt)
            f.writelines(novel)
            f.write("\n")

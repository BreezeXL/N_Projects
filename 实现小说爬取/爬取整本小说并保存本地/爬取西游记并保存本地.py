import requests
import os
import time
from lxml import etree

headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36",
}

# 标题和简介
url = 'http://www.shicimingju.com/book/xiyouji.html'
# url = 'http://www.shicimingju.com/book/hongloumeng.html'
res = requests.get(url, headers=headers)
res.encoding = res.apparent_encoding

html = etree.HTML(res.text, etree.HTMLParser())
# 文件夹名字
dir_name = html.xpath('//h1/text()')[0]

# 没有这个文件夹就创建
if not os.path.exists(dir_name):
    os.mkdir(dir_name)

# 简介
intro_url = html.xpath('//p/text()')

# 保存
for intro in intro_url:
    with open(dir_name + '/' + '简介.txt', 'a+', encoding='utf8')as f:
        f.writelines(intro)
        f.write("\n")

# 内容
n = 1
for i in range(1, 101):
    time.sleep(3)
    print('第%s章正在下载...' % n)
    n += 1
    url2 = 'http://www.shicimingju.com/book/xiyouji/%s.html' % i
    # url2 = 'http://www.shicimingju.com/book/hongloumeng/%s.html' % i
    res2 = requests.get(url2, headers=headers)
    res2.encoding = res2.apparent_encoding

    html2 = etree.HTML(res2.text, etree.HTMLParser())
    novels_url = html2.xpath('//p/text()')

    # 保存
    for novel in novels_url:
        # 小说章节名字
        title_txt = html2.xpath('//h1/text()')
        # 保存在文件夹里面
        with open(dir_name + '/' + '%s.txt' % title_txt[0], 'a+', encoding='utf8')as f:
            f.writelines(novel)
            f.write("\n")

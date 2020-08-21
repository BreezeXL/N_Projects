import requests
import re
import os

headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36",
}

response = requests.get('https://www.vmgirls.com/12985.html', headers=headers)
# print(response.text)
html = response.text

# 文件夹名
dir_name = re.findall('<h1 class="post-title h3">(.*?)</h1>', html)[-1]
# 这个文件夹不存在就创建
if not os.path.exists(dir_name):
    os.mkdir(dir_name)
# 图片解析
urls = re.findall('<a href="(.*?)" alt=".*?" title=".*?">', html)
print(urls)

# 保存图片
for url in urls:
    # 图片名字
    file_name = url.split('/')[-1]
    response = requests.get(url, headers=headers)
    # 把图片保存在文件夹中
    with open(dir_name + '/' + file_name, 'wb')as f:
        f.write(response.content)
        n = 1
        print('--------------------->', n)
        n += 1

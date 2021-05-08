from bs4 import BeautifulSoup
import requests

# 访问网页
resp = requests.get('http://www5.ncwu.edu.cn/channels/5.html')
# 设定html文件编码
resp.encoding = resp.apparent_encoding
# 解析为可用的html树
bs = BeautifulSoup(resp.text, "html.parser")

# 查找news-item节点
for item in bs.find_all(class_='news-item'):
    # 输出子节点年月
    print(item.find(class_='month').text, end='-')
    # 输出子节点日期
    print(item.find(class_='day').text, end=': ')
    # 输出子节点标题
    print(item.find(class_='detail').text.strip())


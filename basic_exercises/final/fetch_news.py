from typing import List

from bs4 import BeautifulSoup
import requests

from basic_exercises.final.entity import News


def fetch_page(page_size: int) -> List[News]:
    """
    按页面数获取新闻

    :param page_size: 页面数
    :return: 新闻数组
    """
    news = []
    for i in range(1, page_size + 1):
        suffix = '' if i == 1 else f'_{i}'
        # 访问网页
        resp = requests.get(f'https://www5.ncwu.edu.cn/channels/5{suffix}.html')
        # 设定html文件编码
        resp.encoding = resp.apparent_encoding
        # 解析为可用的html树
        bs = BeautifulSoup(resp.text, "html.parser")
        news += fetch_news(bs)
    print("完成网页信息爬虫")
    return news


def fetch_news(bs: BeautifulSoup) -> List[News]:
    """
    对一个页面的信息爬虫获取新闻

    :param bs: 已解析的网页
    :return: 新闻数组
    """
    news = []
    # 查找news-item节点
    for item in bs.find_all(class_='news-item'):
        # 获取子节点年月日
        time = item.find(class_='month').text + '-'
        time += item.find(class_='day').text
        # 输出子节点部门、标题
        a_list = item.find_all('a')
        url = a_list[1].get('href')
        department = a_list[0].text.strip()
        info = a_list[1].text.strip()
        news.append(News(url, time, department, info))
    return news

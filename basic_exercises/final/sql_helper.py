from typing import List, Dict

import pymysql

from basic_exercises.final.entity import News

mysql_conn = pymysql.connect(
    host='127.0.0.1',
    port=3306,
    user='test',
    password='test',
    db='ncwu_news'
)


def select_all() -> List[News]:
    sql = """
    select * from news;
    """
    news = []
    try:
        with mysql_conn.cursor() as cursor:
            cursor.execute(sql)
            select_result = cursor.fetchall()
            for row in select_result:
                news.append(News(row[0], row[1], row[2], row[3]))
            print(select_result)
    except Exception as e:
        print(e)
    return news


def insert_all(news: List[News]):
    sql = """
    insert into news(id, time, department, info)
    values('{0}', '{1}', '{2}', '{3}');
    """
    for n in news:
        try:
            with mysql_conn.cursor() as cursor:
                cursor.execute(sql.format(n.id, n.time, n.department, n.info))
            mysql_conn.commit()
        except Exception:
            mysql_conn.rollback()
    print("完成数据库信息插入")


def group_department() -> Dict[str, int]:
    sql = """
    select department, count(*)
    from news
    group by department;
    """
    dic = {}
    try:
        with mysql_conn.cursor() as cursor:
            cursor.execute(sql)
            select_result = cursor.fetchall()
            for row in select_result:
                dic[str(row[0])] = int(row[1])
    except Exception as e:
        print(e)
    return dic

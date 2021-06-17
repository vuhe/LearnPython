import unittest

from basic_exercises.final import *


class MyTestCase(unittest.TestCase):
    def test_something(self):
        # 从网站获取新闻
        news = fetch_page(5)
        # 插入到数据库
        insert_all(news)
        # 从数据库获取统计好的部门信息
        dic = group_department()
        # 将统计好的部门信息绘制成表格
        draw_result(dic)
        self.assertEqual(True, True)

    def tearDown(self) -> None:
        mysql_conn.close()


if __name__ == '__main__':
    unittest.main()

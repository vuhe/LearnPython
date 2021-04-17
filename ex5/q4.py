# 示例数据
dd = {'a': 0, 0: 'd', 1: 2}

print(dd.keys())
print(dd.values())
print(dd.items())
print(dd.get(3, 'null'))
print(dd.pop('a', 'null'))
print(dd.popitem())
print('c' in dd)
del dd[0]
print(dd)
dd.clear()
print(dd)

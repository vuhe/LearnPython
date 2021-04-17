# 示例数据
ss = {'a', '我爱学习', (123, 'b'), ' ', 'i lv python'}
tt = {'c'}

print(ss.difference(tt))
print(ss.difference_update(tt), end=' ')
print(ss.intersection(tt), end=' ')
print(ss.intersection_update(tt), end=' ')
print(ss.symmetric_difference(tt))
print(ss.symmetric_difference_update(tt), end=' ')
print(ss.union(tt), end=' ')
print(ss.update(tt), end=' ')
print(ss.issubset(tt), end=' ')
print(ss.issuperset(tt))

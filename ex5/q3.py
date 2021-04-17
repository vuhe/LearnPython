# 示例数据
ls = ['a', 1, [123], ('a', 'b', 'c'), {}]
lt = [1, 2, 3]
x = 3 + 4j

ls[1] = x
print(ls)
ls[1: 4] = lt
print(ls)
ls[0: 5: 2] = lt
print(ls)
del ls[0:2]
print(ls)
del ls[0:3:2]
print(ls)
ls += lt
print(ls)
ls *= 2
print(ls)

ls.append(x)
print(ls)
ls.clear()
print(ls, end=' ')
print(ls.copy(), end=' ')
ls.insert(0, x)
print(ls, end=' ')
print(ls.pop(0), end=' ')
ls += lt
ls.remove(2)
print(ls, end=' ')
ls.reverse()
print(ls)

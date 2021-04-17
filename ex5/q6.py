import jieba

# 示例数据
tx = '我爱学习"python!"'

print(jieba.cut(tx))
print(jieba.cut(tx, cut_all=True))
print(jieba.cut_for_search(tx))
print(jieba.lcut(tx))
print(jieba.lcut(tx, cut_all=True))
print(jieba.lcut_for_search(tx))
print(jieba.add_word(tx))

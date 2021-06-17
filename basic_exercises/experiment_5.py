import jieba


def test(test0, test1):
    print('1' in test0, end=' ')
    print('p' not in test0)
    print(test0 + test1)
    print(test0 * 2)
    print(test0[0], end=' ')
    print(test0[1:3], end=' ')
    print(test0[0:4:2])
    print(len(test0), end=' ')
    print(min(test0), end=' ')
    print(max(test0), end=' ')
    print(test0.index(test0[3]), end=' ')
    print(test0.count(test0[3]), end='\n\n')


def question_1():
    # 示例数据
    test_str = '1234'
    test_o_str = '5'
    test_tuple = (1, 2, 3, 4)
    test_o_tuple = (5, 6)
    test_list = [1, 2, 3, 4]
    test_o_list = [5, 6]

    test(test_tuple, test_o_tuple)
    test(test_list, test_o_list)
    test(test_str, test_o_str)


def question_2():
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


def question_3():
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


def question_4():
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


def question_5():
    d = {'张三': 88, '李四': 90, '王五': 73, '赵六': 82}

    d['钱七'] = 90
    d['王五'] = 93
    del d['赵六']
    print(d)


def question_6():
    # 示例数据
    tx = '我爱学习"python!"'

    print(jieba.cut(tx))
    print(jieba.cut(tx, cut_all=True))
    print(jieba.cut_for_search(tx))
    print(jieba.lcut(tx))
    print(jieba.lcut(tx, cut_all=True))
    print(jieba.lcut_for_search(tx))
    print(jieba.add_word(tx))


def check_for_repetition(a_list) -> bool:
    check = set(a_list)
    return len(check) != len(a_list)


def question_7():
    test_list = [1, 2, 3, 4, 5, 5]
    print(check_for_repetition(test_list))


def question_8():
    s = """Gur Mra bs Clguba, ol Gvz Crgref
    Ornhgvshy vf orggre guna htyl.
    Rkcyvpvg vf orggre guna vzcyvpvg.
    Fvzcyr vf orggre guna pbzcyrk.
    Pbzcyrk vf orggre guna pbzcyvpngrq.
    Syng vf orggre guna arfgrq.
    Fcnefr vf orggre guna qrafr.
    Ernqnovyvgl pbhagf.
    Fcrpvny pnfrf nera'g fcrpvny rabhtu gb oernx gur ehyrf.
    Nygubhtu cenpgvpnyvgl orngf chevgl.
    Reebef fubhyq arire cnff fvyragyl.
    Hayrff rkcyvpvgyl fvyraprq.
    Va gur snpr bs nzovthvgl, ershfr gur grzcgngvba gb thrff.
    Gurer fubhyq or bar-- naq cersrenoyl bayl bar --boivbhf jnl
    gb qb vg.
    Nygubhtu gung jnl znl abg or boivbhf ng svefg hayrff lbh'er
    Qhgpu.
    Abj vf orggre guna arire.
    Nygubhtu arire vf bsgra orggre guna *evtug* abj.
    Vs gur vzcyrzragngvba vf uneq gb rkcynva, vg'f n onq vqrn.
    Vs gur vzcyrzragngvba vf rnfl gb rkcynva, vg znl or n tbbq
    vqrn.
    Anzrfcnprf ner bar ubaxvat terng vqrn -- yrg'f qb zber bs
    gubfr!"""

    # 解密
    d = {}
    for c in (65, 97):
        for i in range(26):
            d[chr(i + c)] = chr((i + 13) % 26 + c)
    text = "".join([d.get(c, c) for c in s])

    # 统计词频
    words = text.split()
    counts = {}
    for word in words:
        counts[word] = counts.get(word, 0) + 1
    items = list(counts.items())
    items.sort(key=lambda x: x[1], reverse=True)
    for i in range(10):
        word, count = items[i]
        print("{0:<10}{1:>5}".format(word, count))

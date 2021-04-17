# 示例数据
test_str = '1234'
test_o_str = '5'
test_tuple = (1, 2, 3, 4)
test_o_tuple = (5, 6)
test_list = [1, 2, 3, 4]
test_o_list = [5, 6]


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


test(test_tuple, test_o_tuple)
test(test_list, test_o_list)
test(test_str, test_o_str)

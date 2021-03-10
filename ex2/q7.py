# 返回原字符串的副本，其首个字符大写，其余为小写
print(str.capitalize('vuhe'), end=' ')
# 返回原字符串消除大小写的副本
print(str.casefold('Vuhe'), end=' ')
# 如果字符串中的所有字符都是字母或数字且至少有一个字符，
# 则返回 True ， 否则返回 False
print(str.isalnum('vuhe1'))
# 如果字符串中的所有字符都是字母，并且至少有一个字符，
# 返回 True ，否则返回 False
print(str.isalpha('vuhe1'), end=' ')
# 返回原字符串的副本，其所有区分大小写的字符均转换为小写
print(str.lower('VUHE'), end=' ')
# 返回原字符串的副本，其所有区分大小写的字符均转换为大写
print(str.upper('vuhe'))


import time

# 作用是格式化时间戳为本地的时间
print(time.localtime())
# 作用是格式化时间戳为本地的时间
print(time.asctime())
time.sleep(2 + 3)
# 作用是格式化时间戳为本地的时间
print(time.ctime())
# 1970纪元后经过的浮点秒数
print(time.time())
print(time.process_time() / time.process_time_ns())

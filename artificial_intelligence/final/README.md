## 使用说明

1. 由于Google对于 `tensorflow` 框架的大改， `1.x` 和 `2.x` 不兼容，本项目使用的是 `2.x`
   
2. `/artificial_intelligence/final/mnist_data/` 路径下的文件过大，已作忽略处理
   
3. 请确保在运行之前 `/artificial_intelligence/final/mnist_data/`有如下文件
    - train-images-idx3-ubyte.gz
    - train-labels-idx1-ubyte.gz
    - t10k-images-idx3-ubyte.gz
    - t10k-labels-idx1-ubyte.gz
    
4. 运行时间可能较长，请耐心等待

5. `__init__.py` 文件中是系统处理文件（缺失类库），与实验无关，可以作为已知条件使用

6. 缺失文件官网[下载地址](http://yann.lecun.com/exdb/mnist/)

7. 输出信息存于 `/artificial_intelligence/final/mnist_data/log.txt`
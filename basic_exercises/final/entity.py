class News:
    # 允许绑定的对象
    __slots__ = ('__id', '__time', '__department', '__info')

    # 构造函数
    def __init__(self, url, time, department, info):
        self.__id = url
        self.__time = time
        self.__department = department
        self.__info = info

    @property
    def id(self):
        return self.__id

    @property
    def time(self):
        return self.__time

    @time.setter
    def time(self, new_value):
        self.__time = new_value

    @property
    def department(self):
        return self.__department

    @department.setter
    def department(self, new_value):
        self.__department = new_value

    @property
    def info(self):
        return self.__info

    @info.setter
    def info(self, new_value):
        self.__info = new_value

    def __eq__(self, other):
        return self.time == other.time \
               and self.department == other.department \
               and self.info == other.info

    def __hash__(self):
        return hash((self.time, self.department, self.info))

    def __str__(self):
        return "时间: %s, 部门: %s, 信息: %s" % (self.time, self.department, self.info)

    def __repr__(self):
        return "时间: %s, 部门: %s, 信息: %s" % (self.time, self.department, self.info)


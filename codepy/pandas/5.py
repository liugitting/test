# 首先定义一个类，要有__init__
class SN:
    def __init__(self):
        self.data = ""
        self.datalen = ""
        self.datatype = ""

# 开始初始化结构体
a = SN()
a.data = "233333"
a.datalen = len(a.data)
a.datatype = type(a.data)

print(
    f"a.data: {a.data}\n"
    f"a.datalen: {a.datalen}\n"
    f"a.datatype: {a.datatype}\n"
)

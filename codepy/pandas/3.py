import psycopg2
import pandas as pd

# 连接参数设置
database = 'pandas'
username = 'postgres'
password = '123456'  # 建议保密
host = "localhost"
port = "5432"

try:
    gongsi_conn = psycopg2.connect(database=database, user=username,
                                   password=password, host=host, port=port)
    data = pd.read_sql("select * from public.gw;", con=gongsi_conn)
    if not data.empty:
        line1 = data.iloc[0]  # 使用 iloc 来安全地获取第一行
        print(line1)
    else:
        print("查询结果为空！")
except Exception as e:
    print("发生错误：", e)
finally:
    if 'gongsi_conn' in locals():  # 确保连接存在
        gongsi_conn.close()  # 正确关闭数据库连接

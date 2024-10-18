import psycopg2
import pandas as pd
# 连接参数设置

# con = psycopg2.connect(database="pandas", user="postgres", password="123456", host="localhost", port="5432")
database = 'pandas' # 指定数据库名
username = 'postgres' # 指定用户名
password = '123456' # 指定用户密码 ,保密，不对外公布了，以*代替了
host = "localhost" # 指定数据库的服务器（ip）地址,同密码，保密
port = "5432" # 指定数据库端口号
gongsi_conn = psycopg2.connect(database=database,user=username,
                               password=password,host=host,port=port)
# gongsi_cursor = gongsi_conn.cursor()
data = pd.read_sql("select * from public.gw;",con=gongsi_conn)
gongsi_conn.close # 关闭数据库连接
line1=data.iloc[0]
print(data)
print(line1[0])
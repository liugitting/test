import csv
import caculate
import numpy as np
import matplotlib.pyplot as plt
import psycopg2

with open(r"D://code//GF_MW//bjfs0750.23o",'r') as f:
    lines=f.readlines()

d_line=len(lines)

times=[]
s_name=[]
s_date=[]
l1=[]
l2=[]
c1=[]
p1=[]
p2=[]
s1=[]
s2=[]
s_date.append([])
dates=[]

for i in range(23,d_line):
    dates.append(lines[i])
# print(dates)
s=0
m=0
n=34

# print(dates[m][1:3])

while n<len(dates):
    s_add=int(dates[m][30:32])
    s=s+s_add
    # print(s)
    # print(s_add)
    for k in range(0,s_add):
        times.append(dates[m][1:26])
        # print(times)
        l1.append(dates[m+2+2*k][1:16].replace(' ','0'))
        l2.append(dates[m + 2 + 2 * k][17:32].replace(' ','0'))
        c1.append(dates[m + 2 + 2 * k][34:46].replace(' ','0'))
        p1.append(dates[m + 2 + 2 * k][50:62].replace(' ','0'))
        p2.append(dates[m + 2 + 2 * k][66:78].replace(' ','0'))
        s1.append(dates[m + 3 + 2 * k][8:14].replace(' ','0'))
        s2.append(dates[m + 3 + 2 * k][24:30].replace(' ','0'))
        if k<12:
            s_name.append(dates[m][32+3*k:35+3*k])
        else:
            s_name.append(dates[m+1][3*k-4:3*k-1])

    m=m+s_add*2+2
    n=m+s_add*2+2

                                                                            # 分割数据csv
sumdates=[]
for o in range(0,len(times)):
    sumdates.append([times[o],s_name[o],l1[o],l2[o],c1[o],p1[o],p2[o],s1[o],s2[o]])
# print(sumdates)

header = ['times', 'name', 'l1', 'l2','c1', 'p1', 'p2', 's1','s2']
with open('sumdates.csv', 'w', encoding='UTF8',newline='') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    for data in sumdates:
        writer.writerow(data)
    print("succed")

mwresult=[]
gfresult=[]

for i in range(0,len(s_name)):
    # print(l1[0],l1[1])
    l1[i]=caculate.ifnull(l1[i])
    l2[i] = caculate.ifnull(l2[i])
    p1[i] = caculate.ifnull(p1[i])
    p2[i] = caculate.ifnull(p2[i])
    mwresult.append(caculate.mwcaculate(float(l1[i]),float(l2[i]),float(p1[i]),float(p2[i])))
    gfresult.append(caculate.gfcaculate(float(l1[i]),float(l2[i])))
                                                                            #输出MW-GF结果csv
# sumdates=[]
# for o in range(0,len(times)):
#     sumdates.append([times[o],s_name[o],l1[o],l2[o],c1[o],p1[o],p2[o],s1[o],s2[o],mwresult[o],gfresult[o]])
# header = ['times', 'name', 'l1', 'l2','c1', 'p1', 'p2', 's1','s2','mwresult','gfresult']
# with open('sumdates2.csv', 'w', encoding='UTF8',newline='') as f:
#     writer = csv.writer(f)
#     writer.writerow(header)
#     for data in sumdates:
#         writer.writerow(data)
#     print("succed")
# # x_show1 = []
# y_show1 = []
# x_show2 = []
# y_show2 = []
# choose=input("请输入您需要绘制卫星图形的名称：")
# t = 0
# # print(choose)
# for i in range(0,len(s_name)):
#     if s_name[i]==choose:            #此处输入需要画图的卫星名称
#         x_show1.append(t)
#         y_show1.append(mwresult[i])
#         x_show2.append(t)
#         y_show2.append(gfresult[i])
#         t=t+1
# # print(t)
# a=''
# if t>0:
#     # print(t)
#     choose2=input("请输入方法：0-MW,1-GF，2-all:")
#     if choose2=='0':
#         plt.plot(x_show1, y_show1, label='mw', color='red', linewidth=1)
#         a=' MW '
#     if choose2=='1':
#         plt.plot(x_show1, y_show1, label='gf', color='red', linewidth=1)
#         a=' GF'
#     if choose2=='2':
#         plt.plot(x_show1, y_show1, label='mw', color='red', linewidth=1)
#         plt.plot(x_show2, y_show2, label='gf', color='blue', linewidth=1)
#         a=' MW-GF '

#     plt.legend() # 显示标签
#     plt.title(choose+a+str(t))  # 设置图片标题
#     plt.xlabel("times")  # 横轴名字
#     plt.ylabel("devation")  # 纵轴名字
#     plt.savefig(choose+a+str(t)+'.png')  # 保存图片
#     plt.show()
# else:print("没有所输入卫星的名称！")


con = psycopg2.connect(database="pandas", user="postgres", password="123456", host="localhost", port="5432")
#调用游标对象
cur = con.cursor()
#用cursor中的execute 使用DDL语句创建一个名为 STUDENT 的表,指定表的字段以及字段类型
cur.execute('''CREATE TABLE GW
      ( times text,
        names char(3),
        l1 decimal,
        l2 decimal,
        c1 decimal,
        p1 decimal,
        p2 decimal,
        s1 decimal,
        s2 decimal
            );''')
# con.commit()
# con.close()
# def rep(s):
#     if s[0:1]=='0':
#         return s[1:]
#     else: return s

print('----------------分割线----------------')
for i in range(0,len(l1)-1):
    ti=times[i]
    na=s_name[i]
    l11=float(caculate.ifnull(l1[i]))
    l22=float(caculate.ifnull(l2[i]))
    # print(l22)
    # print(i)
    c11=float(caculate.ifnull(c1[i]))
    p11=float(caculate.ifnull(p1[i]))
    p22=float(caculate.ifnull(p2[i]))
    s11=float(caculate.ifnull(s1[i]))
    s22=float(caculate.ifnull(s2[i]))
    cur.execute("INSERT INTO GW (times, names, l1, l2, c1, p1, p2, s1, s2) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)", (ti, na, l11, l22, c11, p11, p22, s11, s22))



#提交更改，增添或者修改数据只会必须要提交才能生效
con.commit()
con.close()

print("succed")


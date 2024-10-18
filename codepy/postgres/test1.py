import psycopg2
#建立数据库连接
con = psycopg2.connect(database="liudate", user="postgres", password="123456", host="localhost", port="5432")
#调用游标对象
cur = con.cursor()
#用cursor中的execute 使用DDL语句创建一个名为 STUDENT 的表,指定表的字段以及字段类型
# cur.execute('''CREATE TABLE dates
#       (ADMISSION INT PRIMARY KEY     NOT NULL,
#       NAME           TEXT            NOT NULL,
#       AGE            INT             NOT NULL,
#       COURSE        CHAR(50),
#       DEPARTMENT        CHAR(50));''')


# #提交更改，增添或者修改数据只会必须要提交才能生效


#在表中插入一条数据
# cur.execute("INSERT INTO dates (ADMISSION,NAME,AGE,COURSE,DEPARTMENT) VALUES (3420, 'John', 18, 'Computer Science', 'ICT')");
# con.commit()
# con.close()

cur.execute("SELECT admission, name, age, course, department from dates")
rows = cur.fetchall()

for row in rows:
    print("ADMISSION =", row[0])
    print("NAME =", row[1])
    print("AGE =", row[2])
    print("COURSE =", row[3])
    print("DEPARTMENT =", row[4], "\n")

print("Operation done successfully")

cur.execute("UPDATE dates set AGE = 20 where ADMISSION = 3420")
print("Total updated rows:", cur.rowcount)
con.commit()

con.close()


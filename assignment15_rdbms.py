import pymysql



print("Question no 01")
db=pymysql.connect("localhost","root","rahul","rahul")
cursor=db.cursor()
qr1="create table book1(bookid int,titleid  int,location char(10),genere char(10))"
qr2="create table title(titleid int,title char(10),ISBN int,publisher_id int,publication_year int)"
qr3="create table publishers(publishers_id int,name char(10),street_address char(10),suite_no int,zip_code int)"
qr4="create table zip_codes(zip_code_id int,city char(20),state char(10),zip_code int)"
qr5="create table Authors_title(author_title_id int,author_id int,title_id int)"
qr6="create table Authors(author_id int,first_name char(10),middle_name char(10),last_name char(10))"
cursor.execute(qr1)
cursor.execute(qr2)
cursor.execute(qr3)
cursor.execute(qr4)
cursor.execute(qr5)
cursor.execute(qr6)
db.close()


print("question no 02")
db=pymysql.connect("localhost","root","rahul","rahul")
cursor=db.cursor()
qr1="insert into book1 values(102,103,'haryana','ninth')"
qr2="insert into title values(101,'revolution',602,103,2018)"
qr3="insert into publishers values(101,'cheatan','new delhi',201,140075)"
qr4="insert into zip_codes values(101 ,'ambala','haryana',133203)"
qr5="insert into  Authors_title values(104,101,103)"
qr6="insert into Authors values(101,'rahul' ,'kumar','tiwari')"
try:
    cursor.execute(qr1)
    cursor.execute(qr2)
    cursor.execute(qr3)
    cursor.execute(qr4)
    cursor.execute(qr5)
    cursor.execute(qr6)
    db.commit()
except:
    db.rollback()
db.close()



print("question no 03")
db=pymysql.connect("localhost","root","rahul","rahul")
cursor=db.cursor()
qr="select * from title"
qr1="update title set title = '2states' where titleid=101"
cursor.execute(qr)
print(cursor.fetchall())
try:
    cursor.execute(qr1)
    db.commit()
except:
    db.rollback()
cursor.execute(qr)

db.close()






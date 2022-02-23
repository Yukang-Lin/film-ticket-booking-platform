# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 20:21:29 2020

@author: msi
"""
import numpy as np
import random
from flask import Flask
from flask import render_template,request
import pymysql

signup=False
User=None
movie=None
cinema=None
hall=None
time=None
src=None
prize=None

app = Flask(__name__)
# 连接mysql字符串
db = pymysql.connect("localhost", "root", "123456", "mysql")
# 新建游标
cursor = db.cursor()
# 执行sql语句


# cursor.execute("select * from film")
# data = cursor.fetchone()
# while 1:
#     res = cursor.fetchone()
#     if res is None:
#     # 表示已经取完结果集
#         break
#     print(res)


# sql = "SELECT * FROM film "
# cursor.execute(sql)
# u = cursor.fetchall()

# # 关闭游标
# cursor.close()
# # 提交事务
# db.commit()
# # 关闭数据库连接
# db.close()
# print("sql语句执行成功！")




@app.route('/')
def home():
    db = pymysql.connect("localhost", "root", "123456", "mysql")
    # 新建游标
    cursor = db.cursor()    
    # 执行sql语句
    sql = "SELECT * FROM film "
    cursor.execute(sql)
    c =  cursor.fetchall()
    # 关闭游标
    cursor.close()
    # 提交事务
    db.commit()
    # 关闭数据库连接
    db.close()
    return render_template('index.html',c=c)

@app.route('/cinema')
def cinema():
    db = pymysql.connect("localhost", "root", "123456", "mysql")
    # 新建游标
    cursor = db.cursor()
    # 执行sql语句
    sql = "SELECT * FROM cinema "
    cursor.execute(sql)
    c =  cursor.fetchall()
    # 关闭游标
    cursor.close()
    # 提交事务
    db.commit()
    # 关闭数据库连接
    db.close()
    return render_template('cinema.html',c=c)

@app.route('/movie/<num>',methods=['GET','POST'])
def movie(num):
    db = pymysql.connect("localhost", "root", "123456", "mysql")
    # 新建游标
    cursor = db.cursor()
    # 执行sql语句
    sql1 = "SELECT * FROM film where fno="+num
    cursor.execute(sql1)
    c=cursor.fetchone()
    # 关闭游标
    sql2 = "SELECT cname,starttime,scroom,fprice,filmsche.fno,cinema.cno FROM filmsche,cinema where cinema.cno=filmsche.cno And filmsche.fno ="+num
    cursor.execute(sql2)
    b = cursor.fetchall()
    cursor.close()
    # 提交事务
    db.commit()
    # 关闭数据库连接
    db.close()
    return render_template('movieintro.html',c=c,b=b)

@app.route('/book/<num>/<cno>')
def book(num,cno):
    db = pymysql.connect("localhost", "root", "123456", "mysql")
    # 新建游标
    cursor = db.cursor()
    # 执行sql语句
    sql1 = "SELECT * FROM film  where fno="+num
    cursor.execute(sql1)
    c =  cursor.fetchone()
    # 关闭游标
    sql2 = "SELECT url FROM cinema where cno="+cno
    cursor.execute(sql2)
    b = cursor.fetchone()
    cursor.close()
    r= np.random.rand(91)
    t=np.zeros(90)
    j=0;
    for i in range(1,91):
        if r[i]>0.5:
            t[j]=int(i)
            j=j+1
    
    # 提交事务
    db.commit()
    # 关闭数据库连接
    db.close()
    print(b[0])
    return render_template('book.html',c=c,b=b,r=t)



@app.route('/login',methods=['GET','POST'])
def login():
    db = pymysql.connect("localhost", "root", "123456", "mysql")
    # 新建游标
    cursor = db.cursor()
    sql = "SELECT * FROM film "
    cursor.execute(sql)
    c =  cursor.fetchall()
    # 关闭游标
    if request.method =='POST': 
        un=request.form.get('text1')
        pw=request.form.get('text2')
        try:
            sql="SELECT * FROM admin WHERE Admin_ID="+str(un)+" AND Admin_Password="+str(pw) 
            cursor.execute(sql)
            temp=cursor.fetchall()
            if temp[0]==None:
                return ("账号或密码输入错误！")
            else:
                return render_template('index.html',c=c)    
        except:
            return ("账号或密码输入错误！")
    cursor.close()
    # 提交事务
    db.commit()
    # 关闭数据库连接
    db.close()
    return render_template('login.html')

@app.route('/signup',methods=['GET','POST'])
def signup():
    db = pymysql.connect("localhost", "root", "123456", "mysql")
    # 新建游标
    cursor = db.cursor()
    sql = "SELECT * FROM film "
    cursor.execute(sql)
    c =  cursor.fetchall()

    # 关闭游标
    if request.method =='POST': 
        un=request.form.get('text1')
        pw1=request.form.get('text2')
        pw2=request.form.get('text3')
        em=request.form.get('text4')
        if pw1==pw2:
            return render_template('index.html',c=c)
        else:
            return ("两次密码输入错误！")
    cursor.close()
    # activaacac
    db.commit()
    # 关闭数据库连接
    db.close()
    return render_template('signup.html')

@app.route('/top')
def top():
    db = pymysql.connect("localhost", "root", "123456", "mysql")
    # 新建游标
    cursor = db.cursor()
    sql1 = "SELECT * FROM top100"
    cursor.execute(sql1)
    c =  cursor.fetchall()

    # 关闭游标

    cursor.close()
    # 提交事务
    db.commit()
    # 关闭数据库连接
    db.close()
    return render_template('top.html',c=c)
@app.route('/CG')
def CG():

    return render_template('CG.html')

if __name__ == '__main__':
    app.run()
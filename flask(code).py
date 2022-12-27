from flask import Flask,render_template,request,redirect
import pymysql
app=Flask(__name__)
@app.route('/')
def home():
   try: 
       db=pymysql.connect(host="localhost",user="root",password="",database="flowershop")
       cus=db.cursor()
       ssql="select * from flowerdetail"
       cus.execute(ssql)
       data=cus.fetchall()
       db.commit()
       print(data)
       return render_template("urlink.html",d=data)
   except Exception as e:
        print("Error:",e)
       
@app.route('/form')
def vi():
    return render_template("exa.html")

@app.route('/home',methods=['POST'])
def store():
    
    a=request.form['title']
    b=request.form['detail']
    d=request.form['count']
    c=request.form['date']
    d=request.form['price']
    #return a+b+c
    try:
       db=pymysql.connect(host="localhost",user="root",password="",database="flowershop")
       cus=db.cursor()
       insql="insert into flowerdetail(flowername,flowercolor,count,importdate,price) values ('{}','{}','{}','{}','{}')".format(a,b,d,c,d)
       cus.execute(insql)
       #data=cus.fetchall()
       db.commit()
       return redirect('/')     
    except Exception as e:
        print("Error:",e)
        
@app.route('/delete/<rid>')
def delete(rid):
    try:
        db=pymysql.connect(host="localhost",user="root",password="",database="flowershop")
        cus=db.cursor()
        dsql="delete from flowerdetail where flowerid={}".format(rid)
        cus.execute(dsql)
        #data=cus.fetchall()
        db.commit()
        return redirect('/')
    except Exception:
        print("Error is ",Exception)

@app.route('/edit/<rid>')
def edit(rid):
    #return "ID is:"+rid
    try:
        db=pymysql.connect(host="localhost",user="root",password="",database="flowershop")
        cu=db.cursor()
        sql="select * from flowerdetail where flowerid= '{}'".format(rid)
        cu.execute(sql)
        data=cu.fetchone()
        return render_template('editform.html',d=data)
        
    except Exception as e:
        print("Error:",e)

@app.route('/update/<rid>',methods=['POST'])
def update(rid):
    #return "ID to be  update in db is:"+rid
    t=request.form['title']
    dt=request.form['detail']
    ys=request.form['count']
    d=request.form['date']
    st=request.form['price']
    #return t+dt+d
    try:
        db=pymysql.connect(host="localhost",user="root",password="",database="flowershop")
        cu=db.cursor()
        sql="update flowerdetail SET flowername='{}',flowercolor='{}',count='{}',importdate='{}',price='{}' where flowerid='{}'".format(t,dt,ys,d,st,rid)
        cu.execute(sql)
        db.commit()
        return redirect('/')
    except Exception as e:
        print("Error:",e)

app.run(debug=True)

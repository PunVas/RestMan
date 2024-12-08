"""   ||Jaye Ganeshaye Namah||    """                                                 
                                                                                                                                                                               
import pandas as pd                                    
import numpy as np                                            
import pyperclip as clipb                                                
import webbrowser as web                                              
import text_to_image as tti                                
import maskpass as mp                    
                                                                                                                                                    
part11 = """            <html>
    <head>
        <title>Dashboard</title>
        <style>
            html::-webkit-scrollbar {
            width: 20px; 
            
            }
            html::-webkit-scrollbar-track {
           background:black; 
            }
            html::-webkit-scrollbar-thumb {
            background-image:  linear-gradient(0deg, rgba(255, 0, 0, 1) 0%,\
                                               rgba(7, 0, 211, 1) 100%);
            box-shadow: 0px 0px 0px 100vh black;
            border-radius: 10px;
            }

            .parent {
            display: flex;
            flex-wrap: wrap;
            }
            .child {
            flex: 1 0 45%;
            margin: 5px;
            height: auto;
            justify-content: center;
            background-color: rgb(119, 40, 73);
            border-radius: 20px 20px 20px 20px;
            background-color: rgb(119, 40, 73);
            border-radius: 20px 20px 20px 20px;
            }
            #topHead {
            text-align: center;
            color: rgb(255, 255, 255);
            font-family: Verdana;
            font-size: 12vh;
            font-weight: bolder margin-bottom:35x;
            }
            img {
            border-style: solid;
            border-width: 1vw;
            margin-left: auto;
            margin-right: auto;
            width: 35vw;
            border-radius: 10px;
            margin-bottom: 5px;
            padding: auto;
            height: auto;
            border-color: rgb(221, 155, 183);
            }
            p {
            font-size: 5vh;
            font-family: Verdana;
            color: rgb(247, 179, 204);
            width: 30vw;
            }
            .vl {
            background-color: rgb(161, 212, 180);
            height: auto;
            width: 20px;
            border-radius: 10px 0px 0px 10px;
            }
            .flex-container {
            display: flex;
            /*flex-direction: row;
            margin-bottom: 12px;
            margin: auto;*/
            flex-wrap: wrap;
            }
            @media (max-width: 500px) {
            #topHead: {
            font-size: 1vw;
            }
            .flex-container div {
            width: 90vw;
            align: justify;
            }
            .flex-container {
            width: 20vw;
            }
            p {
            width: 80vw;
            }
            img {
            width: 80vw;
            }
            .flex-container .vl {
            width: 20px;
            }
            }
            @media (max-width: 800px) {
            .flex-container {
            flex-direction: column;
            margin-bottom: 12px
            }
            }
            @media (min-width: 800px) {
            .flex-container div {
            width: 40vw;
            align: justify;
            }
            .flex-container {
            width: 80vw;
            }
            .flex-container img {
            width: 80vw;
            }
            .flex-container .vl {
            width: 20px;
            }
            }
            .topPan {
            width: 100vw;
            position: sticky;
            background-color: white;
            top: 0px;
            height: 15px;
            dispaly: block
            }
            .topPan:hover {
            width: 100vw;
            position: sticky;
            background-color: white;
            top: 0px;
            height: auto;
            }
            .dropbtn {
            background-color: #04AA6D;
            color: white;
            padding: 16px;
            font-size: 16px;
            border: none;
            }
            .dropdown {
            position: relative;
            display: inline-block;
            }
            .dropdown-content {
            display: none;
            position: absolute;
            background-color: #f1f1f1;
            min-width: 300px;
            box-shadow: 0px 8px 16px 0px rgba(0, 0, 0, 0.2);
            z-index: 1;
            }
            .dropdown-content a {
            color: black;
            padding: 12px 16px;
            text-decoration: none;
            display: block;
            border: 2px solid rgb(187, 144, 252);
            }
            .dropdown-content a:hover {
            background-color: #ddd;
            }
            .dropdown:hover .dropdown-content {
            display: block;
            }
            .dropdown:hover .dropbtn {
            background-color: #3e8e41;
            }
            .child:hover {
            box-shadow: 2px 2px 2px 2px rgba(255, 255, 255, 0.7);
            }
            #topbtn {
            position: fixed;
            bottom: 20px;
            right: 30px;
            z-index: 1;
            border: none;
            outline: none;
            background-color: red;
            color: white;
            cursor: pointer;
            padding: 15px;
            border-radius: 10px;
            font-size: 18px;
            box-shadow: 0px 8px 16px 0px rgba(0, 0, 0, 0.7);
            }
        </style>
    </head>
    <body style="background-image:linear-gradient( to left,\
        rgb(111,111,111),rgb(0,0,0))">
        <div id='f' class="dropdown">
            <button class="dropbtn">Menu</button>
            <div class="dropdown-content">"""
                                                            
part1 = """                <a href="#{0}">{1}</a>
                <a href="#{2}">{3}</a>
                <a href="#{4}">{5}</a>
                <a href="#{6}">{7}</a>
            </div>
        </div>
        <div id="topHead">Dashboard</div>
        <hr style="height:0.5vh;border:none;background-color: \
            #333;margin:auto;">
                    <div class="parent">"""
                                                                               
part2 = """ <div class="child">
                <div style="display:flex;text-align:center">
                    <div class="vl" id="{}"></div>
                    <div style="padding:10px;width: 40vw;">
                        <p>{}</p>
                        <img src="{}">
                    </div>
                </div>
            </div>"""
                                                            
part3 = """</div>
        <a href="#f">
            <div id="topbtn">Go to Top</div>
        </a>
    </body>
</html>"""
import matplotlib.pyplot as pl
pl.ion()
                                                                                                                                                                                                                            
import os
                                                                                                          
try:
    os.mkdir("C:/Users/" + os.getlogin() + "/Desktop/bills/")
except:
    pass
import datetime


def tmpstmp():
    now = datetime.datetime.now()
    timestamp = str(now.strftime("%Y%m%d%H%M%S"))
    return timestamp

import mysql.connector as sqltor
done=False
while not done:
    usrpass = mp.advpass(mask="•",prompt="\033[1;44m Enter SQL passcode : \u001b[0m" )
    try:
        con = sqltor.connect(host="localhost", user="root", passwd=usrpass, database="mysql")
        usrpass="Umm...trying to get on to the pwd?Well I had thought of that before you."
        done=True
    except:
        print('\033[1;41m Incorrect passcode for SQL.Try again.  \u001b[0m')
        usrpass
cur = con.cursor()
lgin = False
user_true = False


def executesql(  query):
    cur.execute(query)
    try:
        c=cur.fetchall()
        return pd.DataFrame(c)
    except:
        pass
    



def selectall(table):
    cur.execute("select * from {};".format(table))
    out = cur.fetchall()
    return pd.DataFrame(out)


if con.is_connected():
    import sys
    import time
    from IPython.display import display,Image
    display(Image( os.getcwd()+'\\codehawk.jpg'))
    print("Loading: \n")
    pl.ioff()
    animation = [
        "\033[1;31m    [■□□□□□□□□□] 10%",
        "\033[1;31m    [■■□□□□□□□□] 20%",
        "\033[1;31m    [■■■□□□□□□□] 30%",
        "\033[6;34m    [■■■■□□□□□□] 40%",
        "\033[6;34m    [■■■■■□□□□□] 50%",
        "\033[6;34m    [■■■■■■□□□□] 60%",
        "\033[6;36m    [■■■■■■■□□□] 70%",
        "\033[6;36m    [■■■■■■■■□□] 80%",
        "\033[6;32m    [■■■■■■■■■□] 90%",
        "\033[6;32m    [■■■■■■■■■■] 100%",
    ]
    for i in range(len(animation)):
        time.sleep(0.25)
        sys.stdout.write("\r" + animation[i % len(animation)])
        sys.stdout.flush()

    print("\u001b[0m\n")
    con.autocommit = True
    executesql(  "create database if not exists restman;")

    executesql(  "use restman;")

    executesql(  
        "create table if not exists items\
  (ino int(10) primary key,\
  iname varchar(24) not null,\
  iprice int(64) not null,\
  icat varchar(64) not null);"
    )
        
    executesql(  "create table if not exists cats\
         (cats varchar(69));")
        
    executesql(  "create table if not exists cats\
     (cats varchar(69),unique(cats));")
    entrprc=""
    try:
        f = open("C:/Users/" + os.getlogin() + "/Desktop/bills/etrprc.txt", "r")
        x=f.read()
        entrprc=x
        f.close()
        executesql(  'insert into cats values("{} Special");'.format(entrprc))
    except:
        pass
        
    try:
        executesql(  'insert into cats values("BreakFast");')
        executesql(  'insert into cats values("Lunch");')
        executesql(  'insert into cats values("Dinner");')
        executesql(  'insert into cats values("FastFood");')
        executesql(  'insert into cats values("NorthIndian");')
        executesql(  'insert into cats values("SouthIndian");')
        executesql(  'insert into cats values("American");')
        executesql(  'insert into cats values("Mexican");')
        executesql(  'insert into cats values("Italian");')
        executesql(  'insert into cats values("Beverages");')
        executesql(  'insert into cats values("Snacks");')
        executesql(  'insert into cats values("IceCreams");')
        executesql(  'insert into cats values("Sandwiches");')
        executesql(  'insert into cats values("SweetToothSatisfiers");')
        executesql(  'insert into cats values("{}Special");'.format(entrprc))
    except:
        pass
        

    executesql(  
        'create table if not exists tbl_info\
  (tid varchar(10) primary key,\
  no_of_pax int(10) not null,\
  is_vacant varchar(2) default "Y");'
    )

    executesql(  
        'create table if not exists book_table\
  (c_id bigint primary key,\
  t_id varchar(10) not null,\
  c_name varchar(20) not null,\
  phone_no bigint(10) not null,\
  amount bigint not null, \
  review int(2) default 0,\
  billed varchar(4) default "N",\
  foreign key(t_id) references tbl_info(tid) on delete cascade);'
    )

    executesql(  
        "create table if not exists bill_transaction\
       (ord_id bigint,\
        c_id bigint ,\
        i_id int(20),\
        qty int(20),\
        iname varchar(50),\
        i_price int(20),\
        foreign key(i_id) references items(ino)  on delete cascade,\
        foreign key(c_id) references book_table(c_id) on delete cascade);"
    )

    executesql(  "use restman;")

    lgin = True
else:
    print("\033[1;41m credentials are wrong. try again! \u001b[0m")

try:

    passc=tti.decode("C:/Users/" + os.getlogin() + "/Desktop/bills/AppData.png")
    while lgin:
        userin = mp.advpass(mask="•",prompt="\033[1;44m Enter passcode : \u001b[0m" )
        if userin==passc:
            user_true = True
            lgin = False
            userin="Sorry. You can't see the pwd. Here."
        else:
            print("\033[1;41m The password you have entered is invalid \u001b[0m")
            print("\033[1;41m Please try again \u001b[0m")
            print()
            userin=""
    passc="Sorry. You can't see the pwd. Here."
except:
    try:
        executesql(  "drop database restman;")
        print("\u001b[0m\n")
        con.autocommit = True
        executesql(  "create database if not exists restman;")
        
        
            
        executesql(  "use restman;")
    
        executesql(  
            "create table if not exists items\
      (ino int(10) primary key,\
      iname varchar(24) not null,\
      iprice int(64) not null,\
      icat varchar(64) not null);"
        )
    
    
        
            
        executesql(  
            'create table if not exists tbl_info\
      (tid varchar(10) primary key,\
      no_of_pax int(10) not null,\
      is_vacant varchar(2) default "Y");'
        )
    
        executesql(  
            'create table if not exists book_table\
      (c_id bigint primary key,\
      t_id varchar(10) not null,\
      c_name varchar(20) not null,\
      phone_no bigint(10) not null,\
      amount bigint not null, \
      review int(2) default 0,\
      billed varchar(4) default "N",\
      foreign key(t_id) references tbl_info(tid));'
        )
    
        executesql(  
            "create table if not exists bill_transaction\
           (ord_id bigint,\
            c_id bigint ,\
            i_id int(20),\
            qty int(20),\
            iname varchar(50),\
            i_price int(20),\
            foreign key(i_id) references items(ino) on delete cascade,\
            foreign key(c_id) references book_table(c_id) on delete cascade);"
        )
        
            
        import shutil as sh
        sh.rmtree("C:/Users/" + os.getlogin() + "/Desktop/bills")
        os.mkdir("C:/Users/" + os.getlogin() + "/Desktop/bills/")
            
        executesql(  "use restman;")
        npass=mp.advpass(mask="•",prompt="Setup your pass code :")
        enc_save=tti.encode(npass,"C:/Users/" + os.getlogin() + "/Desktop/bills/AppData.png")
        npass="Sorry. You can't see the new pwd."
        user_true = True
        lgin = False
        
        
        
    except:
        npass=mp.advpass(mask="•",prompt="Setup your pass code :")
        enc_save=tti.encode(npass,"C:/Users/" + os.getlogin() + "/Desktop/bills/AppData.png")
        npass="Sorry. You can't see the new pwd."
        user_true=True
        lgin=False
try:
    f = open("C:/Users/" + os.getlogin() + "/Desktop/bills/etrprc.txt", "r")
    f.close()
except:
    f = open("C:/Users/" + os.getlogin() + "/Desktop/bills/etrprc.txt", "w")
    entrprc = input("What is your restaurant called? ")
    f.write(entrprc)
    f.close()
    executesql(  "create table if not exists cats\
     (cats varchar(69),unique(cats));")
     
    entrprc=""
    try:
        f = open("C:/Users/" + os.getlogin() + "/Desktop/bills/etrprc.txt", "r")
        x=f.read()
        entrprc=x
        f.close()
        executesql(  'insert into cats values("{} Special");'.format(entrprc))
    except:
        pass
    try:
        executesql(  'insert into cats values("BreakFast");')
        executesql(  'insert into cats values("Lunch");')
        executesql(  'insert into cats values("Dinner");')
        executesql(  'insert into cats values("FastFood");')
        executesql(  'insert into cats values("NorthIndian");')
        executesql(  'insert into cats values("SouthIndian");')
        executesql(  'insert into cats values("American");')
        executesql(  'insert into cats values("Mexican");')
        executesql(  'insert into cats values("Italian");')
        executesql(  'insert into cats values("Beverages");')
        executesql(  'insert into cats values("IceCreams");')
        executesql(  'insert into cats values("Snacks");')
        executesql(  'insert into cats values("IceCreams");')
        executesql(  'insert into cats values("Sandwiches");')
        executesql(  'insert into cats values("SweetToothSatisfiers");')
        executesql(  'insert into cats values("{}Special");'.format(entrprc))
    except:
        pass
    



tasks = """
\033[1;43m
-----------------------------
1)Item related               
-----------------------------
2)Tables related             
-----------------------------
3)Book table                 
-----------------------------
4)Generate bill              
-----------------------------
5)Generate report            
-----------------------------
6)Order items                
-----------------------------
7)Exit                       
-----------------------------
8)See customers at the moment
-----------------------------
9)Set a new passcode         
-----------------------------
10)See Menu                  
-----------------------------
\u001b[0m"""
       
tasks_1 = """\033[1;43m
---------------------------------------------
1)Add items                                  
---------------------------------------------
2)Update items                               
---------------------------------------------
3)Delete items(It will delete child records) 
---------------------------------------------
4)View items                                 
---------------------------------------------
5)Press any other key to go back to main menu
---------------------------------------------
\u001b[0m"""
tasks_2 = """\033[1;43m
---------------------------------------------
1)Add table                                  
---------------------------------------------
2)Update table                               
---------------------------------------------
3)Delete table(It will delete child records) 
---------------------------------------------
4)View table                                 
---------------------------------------------
5)Press any other key to go back to main menu
---------------------------------------------\u001b[0m"""

while user_true:
    print(tasks)
    todo = input("\033[1;44mEnter your choice \u001b[0m ")

    if todo == "1":
        print(tasks_1)
        done = False
        while not done:
            todo_1 = input("\033[1;44mEnter your choice \u001b[0m ")
            try:
                i = int(todo_1)
                done = True
            except:
                print("\033[1;41mEnter valid datatype \u001b[0m")

        if todo_1 == "1":
            tbl = selectall("items")
            try:
                print('\033[1;44m')
                tbl.columns = ["Ino.", "Item Name", "Price per plate", "category\u001b[0m"]
                tbl.index=[""]*len(tbl)
                print(tbl)
            except:
                print("\u001b[0m\033[1;41mNo items till now.\u001b[0m")
            
                     
                    
            done = False
            
            while not done:
                ex = False
                nxtl=False
                while not ex:
                        ino = input("\033[1;44mEnter the item number \u001b[0m ")
                        try:
                            i = int(ino)
                            nxtl=True
                        except:
                            print("\033[1;41mEnter integer only\u001b[0m")
                            nxtl=False
                            
                        if nxtl==True:
                            if int(ino) not in list(
                            np.array(executesql(  "select ino from items;")).reshape(
                                len(executesql(  "select ino from items;")),
                            )
                        ):
                                    ex = True
                            else:
                                    print("\033[1;41mitem no. already exists. Enter another number\u001b[0m")
                                    nxtl=False
                iname = input("\033[1;44mEnter the name of the item \u001b[0m ")
                
                done1=False
                while not done1:
                    try:
                        iprice = input("\033[1;44mEnter the price of the item \u001b[0m ")
                        i = int(iprice)
                        
                        done = True
                        cat=executesql(  "select distinct icat from items;")
                        cat.columns=[""]*len(cat.columns)
                        
                        print()
                        tbl = executesql(  "select distinct cats from cats;")
                        print('\033[1;44m')
                        tbl.columns = ["category\u001b[0m"]
                        k=[]
                        for x in range(0,len(tbl)):
                            k.append(x+1)
                        tbl.index=k
                        
                        print(tbl)
                        tbl=np.array(tbl)
                        tbl=list(tbl.reshape(len(tbl),))
                        done=False
                        done1=True
                    except:
                        done1=False
                done=False   
                while not done:
                    
                    try:
                        inp=input("enter the category from above options\u001b[0m ")
                        cat=tbl[int(inp)-1]
                        done=True
                    except:
                        print("\033[1;41m enter a valid choice \u001b[0m")
                icat = cat
                    
                executesql(  
                    'insert into items values({},"{}",{},"{}");'.format(
                        ino, iname, iprice, icat
                    )
                )
                print("\033[1;43mItem successfully entered!\u001b[0m")
                i = input("\033[1;32mWant to add more items? [Y,N] \u001b[0m ")
                if i.lower() == "n":
                    ex = True
                elif i.lower() == "y":
                    done = False
                else:
                    done = True
                # except:
                    # print("\033[1;41mIncorrect price format. Enter again.\u001b[0m")


        elif todo_1 == "2":
            now = datetime.datetime.now()
            timestamp = str(int(now.strftime("%Y%m%d")))
            if len(executesql(  
            'select * from book_table where c_id like \
                "{}______" and billed like "N";'.format(
                timestamp
                )
                        ))==0:
                if selectall("items").size!=0:
                    ex = False
                    while not ex:
                        tbl = selectall("items")
                        print('\033[1;44m')
                        tbl.columns = ["Ino.", "Item Name", "Price per plate", "category\u001b[0m"]
                        tbl.index=[""]*len(tbl)
                        print(tbl)
                        ex = False
                        while not ex:
                            done = False
                            while not done:
                                ino = input("\033[1;44mEnter the item number \u001b[0m ")
                                try:
                                    i = int(ino)
                                    done = True
                                    if int(ino) in list(
                                        np.array(executesql(  "select ino from items;")).reshape(
                                            len(executesql(  "select ino from items;")),
                                        )
                                    ):
                                        ex = True
                                    else:
                                        print("\033[1;41mNo such item!. Enter again.\u001b[0m ")
        
                                except:
                                    print("\033[1;41mEnter a valid no. i.e. integer \u001b[0m ")
        
                        out = executesql(  "select * from items where ino={};".format(ino))
                        print('\033[1;44m')
                        out.columns = ["Ino.", "Item Name", "Price per plate", "category\u001b[0m "]
                        out.index=[""]*len(out)
                        print(out)
                        iname = input("\033[1;44mEnter the name of the item \u001b[0m ")
                        done = False
                        while not done:
                            iprice = input("\033[1;44mEnter the price of the item \u001b[0m ")
                            try:
                                i = int(iprice)
                                done = True
                            except:
                                print("\033[1;41mIncorrect price format. Enter again.\u001b[0m ")
                        icat = input("\033[1;44mEnter the category of the item \u001b[0m ")
                        executesql(  
                            'update items set iname="{}",iprice={},icat="{}" where ino={};'.format(
                                iname, iprice, icat, ino
                            )
                        )
                        print("\033[1;32mItem updated successfully\u001b[0m")
                else:
                    print('\033[1;41mNo items exist\u001b[0m')

        elif todo_1 == "3":
            now = datetime.datetime.now()
            timestamp = str(int(now.strftime("%Y%m%d")))
            if len(executesql(  
            'select * from book_table where c_id like \
                "{}______" and billed like "N";'.format(
                timestamp
                )
                        ))==0:
                try:
                    tbl = selectall("items")
                    print('\033[1;44m')
                    tbl.columns = ["Ino.", "Item Name", "Price per plate", "category\u001b[0m"]
                    tbl.index=[""]*len(tbl)
                    print(tbl)
                    done = False
                    while not done:
                        ino = input("\033[1;44mEnter the item no. you want to delete \u001b[0m")
                        try:
                            i = int(ino)
                            if int(ino) in list(
                                np.array(executesql(  "select ino from items;")).reshape(
                                    len(executesql(  "select ino from items;")),
                                )
                            ):
                                executesql(  'delete from items where ino like "{}";'.format(ino))
                                done = True
                            else:
                                print("\033[1;41mNo such item exists!. Enter again.\u001b[0m")
                        except:
                            print("\033[1;41mEnter correct datatype \u001b[0m")
                    done = False
                except:
                    print("\033[1;41mNo items exist\u001b[0m")

        elif todo_1 == "4":
                tbl = selectall("items")
                if tbl.size!=0:
                    print('\033[1;44m')
                    tbl.columns = ["Ino.", "Item Name", "Price per plate", "category\u001b[0m"]
                    tbl.index=[""]*len(tbl)
                    print(tbl)
                else:
                    print('\033[1;41mNo items exist\u001b[0m')
        else:                                                                   
            done=True                                                               

    elif todo == "2":
        print(tasks_2)
        done = False
        while not done:
            todo_2 = input("\033[1;44mEnter your choice \u001b[0m")
            try:
                i = int(todo_2)
                done = True
            except:
                print("\033[1;41mEnter valid datatype \u001b[0m")

        if todo_2 == "1":

            
            try:
                tbl = selectall("tbl_info")
                print("\033[1;44m")
                tbl.columns = ["Table id", "Table Capacity", "Vacancy\u001b[0m"]
                tbl.index=['']*len(tbl)
                print(tbl)
            except:
                print("\033[1;41mNo tables are there.\u001b[0m")
            ex = False
            
            while not ex:
                done = False
                while not done:
                    
                    while not ex:
                        ex = False
                        tid = input("\033[1;44mEnter your table id \u001b[0m ")
                        try:

                            i = int(tid)

                            if tid not in list(
                                np.array(executesql(  "select tid from tbl_info;")).reshape(
                                    len(executesql(  "select tid from tbl_info;")),
                                )
                            ):
                                done = True
                                ex = True
                            else:
                                print("\033[1;41m Table no. already exists. Enter another number \u001b[0m")
                                
                        except:
                            print("\033[1;41mEnter integer only\u001b[0m")

                done = False
                while not done:
                    no_of_pax = input("\033[1;44mEnter no. of pax\u001b[0m ")
                    try:
                        i = int(no_of_pax)
                        done = True
                    except:
                        print("\033[1;41mIncorrect format. Enter again.\u001b[0m")

                executesql(  
                    'insert into tbl_info(tid,no_of_pax) values("{}","{}");'.format(
                        tid, no_of_pax
                    )
                )
                print("\033[1;32m Table entered succesfully \u001b[0m")
                i = input("\033[1;32m Want to add more items? [Y,N]\u001b[0m ")
                if i.lower() == "n":
                    ex = True
                elif i.lower() == "y":
                    ex = False
                else:
                    ex = True
        elif todo_2 == "2":
            now = datetime.datetime.now()
            timestamp = str(int(now.strftime("%Y%m%d")))
            if len(executesql(  
            'select * from book_table where c_id like \
                "{}______" and billed like "N";'.format(
                timestamp
                )
                        ))==0:
                if selectall("tbl_info").size!=0:
                    tbl = selectall("tbl_info")
                    print("\033[1;44m")
                    tbl.columns = ["Table id", "Table Capacity", "Vacancy\u001b[0m"]
                    tbl.index=['']*len(tbl)
                    print(tbl)
                    try:
                        tid = input("\033[1;44mEnter your table id\u001b[0m ")
                        no_of_pax = input("\033[1;44m Enter no. of pax\u001b[0m ")
                        executesql(  'update tbl_info set tid="{}",no_of_pax={}'.format(tid, no_of_pax))
                        print("\033[1;32mTable is Updated succesfully")
                    except:
                        print("\033[1;41mSomething was entered by you that can not be updated to DB\u001b[0m")
                else:
                    print('\033[1;41mNo tables exist\u001b[0m')
                
        elif todo_2 == "3":
            now = datetime.datetime.now()
            timestamp = str(int(now.strftime("%Y%m%d")))
            if len(executesql(  
            'select * from book_table where c_id like \
                "{}______" and billed like "N";'.format(
                timestamp
                )
                        ))==0:
                if selectall("tbl_info").size!=0:
                    tbl = selectall("tbl_info")
                    print("\033[1;44m")
                    tbl.columns = ["Table id", "Table Capacity", "Vacancy\u001b[0m"]
                    tbl.index=['']*len(tbl)
                    print(tbl)
                    inp=input('\033[1;44m Enter the table id to be deleted : \u001b[0m ')
                    executesql(  "delete from tbl_info where tid like '{}';".format(inp))
                else:
                    print('\033[1;41mNo tables exist\u001b[0m')

        elif todo_2 == "4":
            
            if selectall("tbl_info").size!=0:
                tbl1 = selectall("tbl_info")
                print("\033[1;44m")
                tbl1.columns = ["Table id", "Table Capacity", "Vacancy\u001b[0m"]
                tbl1.index=['']*len(tbl1)
                print(tbl1)
                
            else:
                print('\033[1;41mNo tables exist\u001b[0m')
                      
        else:
            done=True

    elif todo == "3":
        if selectall("tbl_info").size!=0:
            done = False
            while not done:
                npax = input("\033[1;44mEnter number of pax \u001b[0m ")
                try:
                    i = int(npax)
                    done = True
                except:
                    print("\033[1;41mInvalid input. Enter again.\u001b[0m ")
            out = executesql(  
                'select * from tbl_info where no_of_pax>= {} and is_vacant like "Y" ;'.format(
                    npax
                )
            )
            if out.size != 0:
                print("\033[1;45mThe table below shows available tables.\u001b[0m")
                print("\033[1;44m")
                out.columns = ["Table id", "Table Capacity", " Vacancy\u001b[0m"]
                out.index=['']*len(out)
                print(out)
    
                done = False
                while not done:
                    tbl2bbkd = input("\033[1;44mEnter table id to be booked \u001b[0m ")
                    if tbl2bbkd in list(
                        np.array(
                            executesql(  'select tid from tbl_info where is_vacant like"Y";')
                        ).reshape(
                            len(executesql(  "select tid from tbl_info where is_vacant like 'Y';")),
                        )
                    ):
                        done = True
                    else:
                        print("\033[1;41menter a valid table number\u001b[0m")
    
                if (
                    executesql(  
                        "select is_vacant from tbl_info where tid={};".format(tbl2bbkd)
                    ).iat[0, 0]
                    == "Y"
                ):
                    done = False
                    while not done:
                        phno = input("\033[1;44mEnter customer's phno. \u001b[0m ")
                        try:
                            i = int(phno)
                            if len(phno) == 10:
                                done = True
                            else:
                                print("\033[1;44mEnter 10 dig phone no.\u001b[0m")
                        except:
                            print("\033[1;41mPhno must be an integer.\u001b[0m")
    
                    cname = input("\033[1;44mEnter customer's name \u001b[0m ")
                    executesql(  
                        "update tbl_info set is_vacant='N' where tid='{}';".format(tbl2bbkd)
                    )
                    c_id = tmpstmp()
                    executesql(  
                        'insert into book_table(c_id,t_id,c_name,phone_no,amount) values({},"{}","{}",{},{});'.format(
                            c_id, tbl2bbkd, cname, phno, 0
                        )
                    )
                    print("\033[1;43mThis customers ID is " + str(c_id)+"\u001b[0m")
                    restore = clipb.paste()
                    clipb.copy(c_id)
                    print("\033[1;43mCurrent Customer id has been copied to your clip board.\u001b[0m")
                    print('The last Data on your clipboard was \033[1;44m "{}" \u001b[0m'.format(restore))
            else:
                print("\033[1;41mNo tables available for now!\u001b[0m")
        else:
                print('\033[1;41mNo tables exist\u001b[0m')

    elif todo == "6":
        
        if (
            len(
                list(
                    np.array(
                        executesql(  "select c_id from book_table where billed \
                                   like 'N';")
                    ).reshape(
                        len(executesql(  "select c_id from book_table where \
                                       billed='N';")),
                    )
                )
            )
            != 0
        ):
            out = executesql(  "select * from items;")
            print('\033[1;44m')
            out.columns=['Ino.','Iname','PricePerPlate','Category\u001b[0m']
            out.index=[""]*len(out)
            print(out)
            now = datetime.datetime.now()
            timestamp = str(int(now.strftime("%Y%m%d")))
            o = executesql(  
            'select * from book_table where c_id like "{}______" and billed\
                like "N";'.format(
                timestamp
            )
        ).iloc[:,[0,1,2,3,4]]
            print()
            print('\033[1;44m')
            o.columns = [ 'Cid',"T id ", "Name", "Phno", "Amount\u001b[0m"]
            print(o)
            cid = input("\033[1;44mEnter the customer's id \u001b[0m ")
            try:
                if int(cid) in list(
                    np.array(executesql(  "select c_id from book_table where\
                                        billed='N';")).reshape(
                        len(executesql(  "select c_id from book_table where\
                                       billed='N';")),
                    )
                ):
                    ord_id = tmpstmp()
                    try:
                        inp = input("\033[1;44mEnter the item no \u001b[0m ")
                        executesql(  
                            "insert into bill_transaction(ord_id,c_id,i_id) \
                                values({},{},{});".format(
                                ord_id, cid, inp
                            )
                        )
                        inp_qty = input("\033[1;44mEnter the qty of item \u001b[0m ")
                        i_name = executesql(  
                            "select iname from items where ino={};".format(inp)
                        ).iat[0, 0]
                        i_price = executesql(  
                            "select iprice from items where ino={};".format(inp)
                        ).iat[0, 0]
                        executesql(  
                            'update bill_transaction set qty= {},iname="{}",i_id= {}\
                                ,i_price= {} where ord_id= {} ;'.format(
                                inp_qty, i_name, inp, i_price, ord_id
                            )
                        )
                        iprice = executesql(  
                            "select iprice from items where ino={};".format(inp)
                        ).iat[0, 0]
                        executesql(  
                            "update book_table set amount=amount+{}*{} where \
                                c_id={};"\
                                .format(
                                iprice, inp_qty, cid
                            )
                        )
                        print("\033[1;45morder placed!\u001b[0m")
                    except:
                        print("\033[1;41mitem not found \u001b[0m")
                else:
                    print("\033[1;41m Cid is incorrect.\u001b[0m")
            except:
                print("\033[1;41m Cid dttype is incorrect.\u001b[0m")
        else:
            print("\033[1;41mNo customer present to place ordered.\u001b[0m")

    elif todo == "4":
        if len(list(
                np.array(executesql(  "select c_id from book_table where \
                                    billed='N';")).reshape(
                    len(executesql(  "select c_id from book_table where\
                                   billed='N';")),
                )
            ))==0:
            print('\033[1;41mNo customers present\u001b[0m')
        else:
            done = False
            while not done:
                now = datetime.datetime.now()
                timestamp = str(int(now.strftime("%Y%m%d")))
                o = executesql(  
                'select * from book_table where c_id like "{}______" and billed \
                    like "N";'.format(
                    timestamp
                )
            ).iloc[:,[0,1,2,3,4,5]]
                o.columns = ["\033[1;44mC id\u001b[0m", "\033[1;44mT id\u001b[0m",\
                             "\033[1;44mName\u001b[0m", "\033[1;44mPhno\u001b[0m", \
                                 "\033[1;44mAmount\u001b[0m", \
                                     "\033[1;44mRating\u001b[0m"]
                o.index=[""]*len(o)
                print(o)
                inp_cid = input("\033[1;44mEnter the customer id whose bill is to be \
                                created \u001b[0m ")
                if inp_cid in list(
                    np.array(executesql(  "select c_id from book_table where \
                                        billed='N';")).reshape(
                        len(executesql(  "select c_id from book_table where billed\
                                       ='N';")),
                    )
                ):
                    print("\033[1;41mBill has already been created for {} \u001b[0m".\
                          format(inp_cid))
                else:
                    done = True
                    done = False
                    try:
                        i = int(inp_cid)
                        done = False
                        if int(inp_cid) in list(
                            np.array(
                                executesql(  "select c_id from book_table where \
                                           billed='N';")
                            ).reshape(
                                len(executesql(  "select c_id from book_table where \
                                               billed='N';")),
                            )
                        ):
                            done = True
                    except:
                        done = False
    
            done = False
            while not done:
                try:
                    review = int(
                        input(
                            "\033[1;44mHow much does the customer rate the \
                                restaurant(no. of stars out of 5) \u001b[0m "
                        )
                    )
                    i = int(review)
                    if (review <= 5) and (review > 0):
                        done = True
                    else:
                        print("\033[1;41menter a value between 1 and 5\u001b[0m")
                except:
                    print("\033[1;41mEnter correct data type.\u001b[0m")
            done = False
    
            tid = executesql(  
                'select t_id from book_table where c_id like "{}";'.format(inp_cid)
            ).iat[0, 0]
            f = open("C:/Users/" + os.getlogin() + "/Desktop/bills/etrprc.txt", "r")
            shop = f.read()
            f.close()
            try:
    
                maindf = executesql(  
                    'select ord_id,i_id,iname,qty,i_price,i_price*qty as "Amount"\
                        from bill_transaction where c_id= {};'.format(
                        inp_cid
                    )
                )
                if maindf.size != 0:
                    print('\033[1;44m')
                    temp=maindf
                    maindf.columns = [
                        "orderid",
                        "itemid",
                        "itemname",
                        "qty",
                        "pricePerPlate",
                        "Amount \u001b[0m",
                    ]
                    temp.columns = [
                        "orderid",
                        "itemid",
                        "itemname",
                        "qty",
                        "pricePerPlate",
                        "Amount",
                    ]
                    maindf.index=[""]*len(maindf)
                    print(maindf)
                    print('Net Payable Amount : {}'.format(maindf.sum().Amount))
                else:
                    temp=maindf
                    maindf = "Nothing was bought."
                amount = executesql(  
                    'select amount from book_table where c_id like"{}"'.format(inp_cid)
                ).iloc[0, 0]
                bill = """Shubh			||Jai Ganeshaye Namah||			Labh
---------------------------------------------------------------------

    		Welcome to {}
---------------------------------------------------------------------
    Your bill is as follows
---------------------------------------------------------------------
""".format(
                    shop
                )
    
                bill+=str(maindf)
                bill += """
    
---------------------------------------------------------------------
    	Net Payable amount:Rs. {} """.format(
                    str(amount)
                )
                bill += """
    	Thank you for visiting us! Hope to see you soon here at
	the palace of spices and taste!
        """
                f = open(
                    "C:/Users/" + os.getlogin() + "/Desktop/bills/" + inp_cid + \
                        ".txt", "w"
                )
                f.write(bill)
                f.close()
                                                                                
                executesql(  
                    'update book_table set review={},billed="Y" where c_id like"{}"'\
                        .format(
                        str(review), str(inp_cid)
                    )
                )
                executesql(  "update tbl_info set is_vacant='Y' where tid={} ;"\
                           .format(tid))
                
                executesql(  "update tbl_info set is_vacant='Y' where tid={} ;".\
                           format(tid))
                
            except:
                print("\033[1;41mNo purchases found\u001b[0m")
                executesql(  "update tbl_info set is_vacant='Y' where tid={} ;".\
                           format(tid))

    elif todo == "5":
        
        try:
            
            import sys
            import time

            print("Loading: \n")
            animation = [
                "\033[1;31m    [■□□□□□□□□□] 10%",
                "\033[1;31m    [■■□□□□□□□□] 20%",
                "\033[1;31m    [■■■□□□□□□□] 30%",
                "\033[6;34m    [■■■■□□□□□□] 40%",
                "\033[6;34m    [■■■■■□□□□□] 50%",
                "\033[6;34m    [■■■■■■□□□□] 60%",
                "\033[6;36m    [■■■■■■■□□□] 70%",
                "\033[6;36m    [■■■■■■■■□□] 80%",
                "\033[6;32m    [■■■■■■■■■□] 90%",
                "\033[6;32m    [■■■■■■■■■■] 100%",
            ]
            for i in range(len(animation)):
                time.sleep(0.25)
                sys.stdout.write("\r" + animation[i % len(animation)])
                sys.stdout.flush()

            print("\u001b[0m\n")
            now = datetime.datetime.now()
            tym = str(now.strftime("%Y%m"))
            quan_items = executesql(  
                'select sum(qty),iname,ord_id from bill_transaction group \
                    by iname having ord_id like "{}________";'.format(
                    tym
                )
            ).loc[:, [0, 1]]
            pl.bar(quan_items.index, quan_items[0])
            pl.xticks(quan_items.index, quan_items[1])
            pl.ylabel("Plates sold this month.")
            try:
                os.mkdir("C:/Users/" + os.getlogin() +\
                         "/Desktop/bills/analysis")
                pl.savefig(
                    "C:/Users/" + os.getlogin() + \
                        "/Desktop/bills/analysis/qitems.png"
                )
                
            except:
                
                pl.savefig(
                    "C:/Users/" + os.getlogin() + \
                        "/Desktop/bills/analysis/qitems.png"
                )
            pl.close()
            tymp = str(now.strftime("%Y%m%d"))
            
            try:
                
                sale_o_day1 = executesql(  
                    'select sum(amount) from book_table where c_id like \
                        "{}______";'.format(
                        tymp
                    )
                ).iloc[0, 0]
                sale_o_day2 = executesql(  
                    'select sum(amount) from book_table where c_id like \
                        "{}______";'.format(
                        str(int(tymp-1))
                    )
                ).iloc[0, 0]
                pl.bar("Today", sale_o_day1)
                pl.bar("Yesterday", sale_o_day2)
                pl.savefig(
                    "C:/Users/"
                    + os.getlogin()
                    + "/Desktop/bills/analysis/saleprday.png"
                )
                pl.close()
                
            except:
                
                sale_o_day1 = executesql(  
                    'select sum(amount) from book_table where c_id like \
                        "{}______";'.format(
                        tymp
                    )
                ).iloc[0, 0]
                pl.close()
                pl.bar("Today", sale_o_day1)
                pl.savefig(
                    "C:/Users/"
                    + os.getlogin()
                    + "/Desktop/bills/analysis/saleprday.png"
                )
            rvws = executesql(  
                'select count(review),review from book_table where c_id \
                    like "{}________" group by review;'.format(
                    tym
                )
            )
            pl.bar(rvws.index, rvws[0])
            pl.xticks(rvws.index, rvws[1])
            pl.ylabel("No. of customers this month")
            pl.savefig(
                "C:/Users/" + os.getlogin() + \
                    "/Desktop/bills/analysis/reviews.png"
            )
            pl.close()
            quan_items.index = quan_items[1]
            del quan_items[1]
            item_prc = executesql(  "select iname,iprice from items;")
            item_prc.index = item_prc[0]
            del item_prc[0]
            df1 = item_prc.sort_index()
            df2 = quan_items.sort_index()
            king_item = pd.Series(df1[1]) * pd.Series(df2[0])
            pl.bar(king_item.index, king_item.values)
            pl.ylabel("Amount earned per item this month")
            pl.savefig(
                "C:/Users/" + os.getlogin() + \
                    "/Desktop/bills/analysis/earnpritem.png"
            )
            pl.close()
            month_code = str(now.strftime("%Y%m"))
            html = """""" + part11
            html += part1.format(
                "i1",
                "Plates sold for each item this month",
                "i2",
                "Income trends",
                "i3",
                "Customer Reviews",
                "i4",
                "Amount earned per item",
            )
            html += part2.format(
                "i1",
                "Plates sold for each item this month",
                "C:/Users/" + os.getlogin() + \
                    "/Desktop/bills/analysis/qitems.png",
            )
            html += part2.format(
                "i2",
                "Income trends",
                "C:/Users/" + os.getlogin() + \
                    "/Desktop/bills/analysis/saleprday.png",
            )
            html += part2.format(
                "i3",
                "Customer Reviews",
                "C:/Users/" + os.getlogin() + \
                    "/Desktop/bills/analysis/reviews.png",
            )
            html += part2.format(
                "i4",
                "Amount earned per item",
                "C:/Users/" + os.getlogin() + \
                    "/Desktop/bills/analysis/earnpritem.png",
            )
            html += part3
            f = open("C:/Users/" + os.getlogin() + \
                     "/Desktop/bills/Dashboard.html", "w")
            f.write(html)
            f.close()
            web.open_new("C:/Users/" + os.getlogin() + \
                         "/Desktop/bills/Dashboard.html")
        except:
            print("No data to make report.")
                                                                              
    elif todo == "7":
        print("\033[1;41mlogging you out\u001b[0m")
        user_true = False
        
        
    elif todo == "8":
        now = datetime.datetime.now()
        timestamp = str(int(now.strftime("%Y%m%d")))
                                                              
        try:
            
            
            o = executesql(  
            'select * from book_table where c_id like \
                "{}______" and billed like "N";'.format(
                timestamp
            )
        ).iloc[:,[0,1,2,3,4,5]]
            o.columns = ["\033[1;44mC id\u001b[0m", "\033[1;44mT \
                         id\u001b[0m", "\033[1;44mName\u001b[0m", "\033[1;44mPhno\u001b[0m", "\033[1;44mAmount\u001b[0m", "\033[1;44mRating\u001b[0m"]
            print(o)
                                                                    
        except:
            
            print("\033[1;41mno data\u001b[0m")
                                                                           
    elif todo == "9":
        done=False
        
        
        
        while not done:
            npass=mp.advpass(mask="•",prompt="\033[1;41m Enter new passcode \
                             :\u001b[0m")
            npass_=mp.advpass(mask="•",prompt="\033[1;41m Enter new passcode \
                              again for confirmation :\u001b[0m")
            
            if npass==npass_:
                enc_save=tti.encode(npass,"C:/Users/" + os.getlogin() +\
                                    "/Desktop/bills/AppData.png")
                print("\033[1;32m Passcode updated! \u001b[0m")
                done=True
                
            else:
                print("\033[1;41m Both passcodes don't match Enter again.\
                      \u001b[0m")
                
        npass="Sorry. You can't see the new pwd."
        npass_="Sorry. You can't see the pwd."
                                                                                                      
                                                                                                                                                                                
                                                    
                                                                                                        
    elif todo == '10':
            tbl = executesql(  "select distinct cats from cats;")
            tbl=np.array(tbl)
            tbl=list(tbl.reshape(len(tbl),))
            for x in tbl:
                try:
                    data=executesql(  'select ino,iname,iprice from items where\
                                    icat like "{}";'.format(x))
                    if data.size!=0:
                        print()
                        print("   \033[1;44m"+x+" \u001b[0m")
                        data.index=[""]*len(data)
                        print("\033[1;46m")
                        data.columns=['Ino.','Iname','IPrice\u001b[0m']
                        print(data)
                        print()
                except:
                    pass

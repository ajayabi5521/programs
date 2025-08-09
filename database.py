import pymysql
connection=pymysql.connect(
    host='localhost',
    user='root',
    password='livewire',
   
    
)


try:
    with connection.cursor() as cursor:
        
        cursor.execute("use company")
        create_table="""CREATE TABLE IF NOT EXISTS info_collection(s_no int(24) primary key auto_increment,
        name varchar(255),age int(30),
        location varchar(256))"""
        cursor.execute(create_table)
        connection.commit()

        '''insert="INSERT INTO info_collection (name,age,location) values(%s,%s,%s)"
        name=input("Enter your name:")
        age=input("Enter your age:")
        location=input("Enter your location:")
        cursor.execute(insert,(name,age,location))
        connection.commit()'''

        cursor.execute("select *from info_collection")
        result=cursor.fetchall()
        print("output")
        for row in result:
            for r in row:
                print(r,end=" ")
            print("\n")
            
     
        
finally:
    connection.close()
        


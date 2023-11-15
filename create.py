  # installed library mysql-connector-python
import mysql.connector

#creating connection 

class insert:
    def __init__(self):
        self.conn = mysql.connector.connect(
                host = "localhost",
                user = "root",
                password = "root",
                database = "bank"
                )
        
    def personal_details(self,cid,fname,lname,addr,pn,an,pan):
        cur = self.conn.cursor() # creating cursor
        cur.execute(f"insert into personal_details values({cid},'{fname}','{lname}','{addr}',{pn},'{an}','{pan}')")
        self.conn.commit()
        print("-----------personal information has been saved successfully--------:") 

    def bank_details(self,acn,cid,ifsc,actype) :
        cur=self.conn.cursor()
        cur.execute(f"insert into bank_details values({acn},{cid},'{ifsc}','{actype}')")
        self.conn.commit()
        print("---------bank details has been successfully saved------:")

    def transaction_details(self,tid,sac,rac,am,mtd):
        cur=self.conn.cursor()
        cur.execute(f"insert into transaction_details values({tid},{sac},{rac},{am},'{mtd}')")   
        self.conn.commit()
        print("-------transaction details has been successfully saved------:")

    def account_details(self,acn,tid,am,tp,cb):
        cur=self.conn.cursor()
        cur.execute(f"insert into account_details values({acn},{tid},{cb},{am}'{tp}')") 
        self.conn.commit() 
        print("----------account details has been successfully saved--------:")






   
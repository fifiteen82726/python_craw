# -*- coding: UTF-8 -*-     
#!/usr/bin/python

import MySQLdb
import json
import urllib

# Open database connection
db = MySQLdb.connect("140.138.77.104","BDSTeam08","BDSTeam08@2015","BDSTeam08_DB" )

# prepare a cursor object using cursor() method
cursor = db.cursor()


sql =  "INSERT INTO pet_1001514(pet_name, \
       pet_owner, pet_specise, pet_sex, pet_birth) \
       VALUES ('%s', '%s', '%s', '%s', '%s' )"  % \
        ( Mac ,  Mac1 ,  Mac2 ,  Mac3 ,  '0000-00-00' ) 
try : 
   #執行sql語句
   cursor . execute ( sql ) 
   #提交到數據庫執行
   db . commit () 
except : 
   #發生錯誤時回滾
   db . rollback ()

#關閉數據庫連接
db . close ()

# execute SQL query using execute() method.
# cursor.execute("SELECT VERSION()")

# # Fetch a single row using fetchone() method.
# data = cursor.fetchone()

# print "Database version : %s " % data

# # disconnect from serve

# sql = """INSERT INTO EMPLOYEE(FIRST_NAME,
#          LAST_NAME, AGE, SEX, INCOME)
#          VALUES ('Mac', 'Mohan', 20, 'M', 2000)"""


# sql =  "INSERT INTO EMPLOYEE(FIRST_NAME, \
#        LAST_NAME, AGE, SEX, INCOME) \
#        VALUES ('%s', '%s', '%d', '%c', '%d' )"  % \
#         ( 'Mac' ,  'Mohan' ,  20 ,  'M' ,  2000 ) 


# db.close()
# -*- coding: UTF-8 -*-     
#!/usr/bin/python

import MySQLdb
import json
import urllib

# Open database connection
db = MySQLdb.connect("140.138.77.104","BDSTeam08","BDSTeam08@2015","BDSTeam08_DB" )

# prepare a cursor object using cursor() method
cursor = db.cursor()


# sql =  "INSERT INTO pet_1001514(pet_name, \
#        pet_owner, pet_specise, pet_sex, pet_birth) \
#        VALUES ('%s', '%s', '%s', '%s', '%s' )"  % \
#         ( Mac ,  Mac1 ,  Mac2 ,  Mac3 ,  '0000-00-00' ) 
try : 
   #執行sql語句
   # cursor . execute ( sql ) 
   cursor.execute ("""
   UPDATE pet_1001514
   SET pet_name=%s, pet_owner=%s, pet_specise=%s, pet_sex=%s, pet_birth=%s
   WHERE pet_sex=%s
""", ("Year", "Month", "Day", "Hour", "0000-00-00", "Sk"))
   #提交到數據庫執行
   db . commit () 
except : 
   #發生錯誤時回滾
   db . rollback ()

#關閉數據庫連接
db . close ()





# -*- coding: UTF-8 -*-     
#!/usr/bin/python

import MySQLdb
import json
import urllib

# Open database connection
db = MySQLdb.connect("140.138.77.104","BDSTeam08","BDSTeam08@2015","BDSTeam08_DB" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

try : 
   #執行sql語句
   # cursor . execute ( sql ) 
   cursor.execute ("""
   UPDATE Railfall
   SET  Rainfall1hr=%s, PublishTime=%s
   WHERE SiteId=%s
""", ("Year", "Month","wr0101"))
   db . commit () 
except : 
   #提交到數據庫執行
   #發生錯誤時回滾
   db . rollback ()

#關閉數據庫連接
db . close ()





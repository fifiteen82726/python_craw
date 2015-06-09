# -*- coding: UTF-8 -*-     
#!/usr/bin/python

import MySQLdb
import json
import urllib

# Open database connection
db = MySQLdb.connect("140.138.77.104","BDSTeam08","BDSTeam08@2015","BDSTeam08_DB" )

cursor = db.cursor()


results = json.load(urllib.urlopen("http://opendata.epa.gov.tw/ws/Data/RainTenMin/?$orderby=PublishTime%20desc&$skip=0&$top=1000&format=json"))

try : 
   #執行sql語句
   # cursor . execute ( sql )
   for i in range(0, len(results) , 1): 
      cursor.execute ("""
      UPDATE Railfall
      SET  Rainfall1hr=%s, PublishTime=%s
      WHERE SiteId=%s
   """, (results[i]['Rainfall1hr'] , "123" , results[i]['SiteId'] ))
      db . commit () 
      #print i
except : 
   #提交到數據庫執行
   #發生錯誤時回滾
   print '7'
   db . rollback ()

#關閉數據庫連接
db . close ()





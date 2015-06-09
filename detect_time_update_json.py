# -*- coding: UTF-8 -*-     
#!/usr/bin/python

import MySQLdb
import json
import urllib

# Open database connection
db = MySQLdb.connect("140.138.77.104","BDSTeam08","BDSTeam08@2015","BDSTeam08_DB" )

cursor = db.cursor()

cursor.execute("SELECT PublishTime FROM Railfall WHERE SiteId = %s", ("A1AB80",))

# fetch all of the rows from the query
data = cursor.fetchall ()

for row in data :
   select_time = row[0]  #select_time 是從資料庫拉出來的時間

results = json.load(urllib.urlopen("http://opendata.epa.gov.tw/ws/Data/RainTenMin/?$orderby=PublishTime%20desc&$skip=0&$top=1000&format=json"))
results_time = results[0]['PublishTime']  #results_time 是json的更新 time
#print results[0]['SiteId']


#print results_time
#print select_time


if  (results_time != select_time):
   try : 
     # print "update"
   #執行sql語句
   # cursor . execute ( sql )
      for i in range(0, len(results) , 1): 
         #print i
         cursor.execute ("""
         UPDATE Railfall
         SET  Rainfall1hr=%s, PublishTime=%s
         WHERE SiteId=%s
      """, (results[i]['Rainfall1hr'] , results[i]['PublishTime'] , results[i]['SiteId'] ))
         db . commit () 
      #print i
   except : 
   #提交到數據庫執行
   #發生錯誤時回滾
     # print 'error'
      db . rollback ()


#關閉數據庫連接
db . close ()





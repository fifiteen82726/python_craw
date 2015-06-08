# -*- coding: UTF-8 -*-     
#!/usr/bin/python

import MySQLdb
import json
import urllib


# Open database connection
db = MySQLdb.connect("140.138.77.104","BDSTeam08","BDSTeam08@2015","BDSTeam08_DB" )

# prepare a cursor object using cursor() method
cursor = db.cursor()


results = json.load(urllib.urlopen("http://opendata.epa.gov.tw/ws/Data/RainTenMin/?$orderby=PublishTime%20desc&$skip=0&$top=1000&format=json"))

for i in range(0, len(results) , 1):
	sql =  "INSERT INTO Railfall(idRailfall, \
       SiteId,Rainfall1hr,PublishTime) \
       VALUES ('%d', '%s', '%s', '%s' )"  % \
       (0, results[i]['SiteId'] ,  results[i]['Rainfall1hr'] ,  results[i]['PublishTime']) 
	try : 
   #執行sql語句
   		cursor . execute ( sql ) 
   #提交到數據庫執行
   		db.commit () 
	except : 
   #發生錯誤時回滾
   		db . rollback ()

#關閉數據庫連接
db . close ()


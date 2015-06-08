#!/usr/bin/python
# view_rows.py - Fetch and display the rows from a MySQL database query
# import the MySQLdb and sys modules
import MySQLdb
import sys

import json
import urllib

# open a database connection
# be sure to change the host IP address, username, password and database name to match your own
connection = MySQLdb.connect (host = "140.138.77.104", user = "BDSTeam08", passwd = "BDSTeam08@2015", db = "BDSTeam08_DB")

# prepare a cursor object using cursor() method
cursor = connection.cursor ()


cursor.execute("SELECT PublishTime FROM Railfall WHERE SiteId = %s", ("A1AB80",))

# fetch all of the rows from the query
data = cursor.fetchall ()

for row in data :
	select_time = row[0]
# close the cursor object
cursor.close ()
# close the connection
connection.close ()


results = json.load(urllib.urlopen("http://opendata.epa.gov.tw/ws/Data/RainTenMin/?$orderby=PublishTime%20desc&$skip=0&$top=1000&format=json"))


results_time = results[0]['PublishTime'] 

print len(results_time)
print len(select_time)

if  (results_time == select_time):
	print "tttt"















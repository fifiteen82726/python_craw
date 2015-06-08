#!/usr/bin/python
# view_rows.py - Fetch and display the rows from a MySQL database query
# import the MySQLdb and sys modules
import MySQLdb
import sys
# open a database connection
# be sure to change the host IP address, username, password and database name to match your own
connection = MySQLdb.connect (host = "140.138.77.104", user = "BDSTeam08", passwd = "BDSTeam08@2015", db = "BDSTeam08_DB")

# prepare a cursor object using cursor() method
cursor = connection.cursor ()
# execute the SQL query using execute() method.
#cursor.execute ("select SiteId, PublishTime from Railfall WHERE SiteId=%s" % (A1AB80))
# cursor.execute("""SELECT SiteId, PublishTime 
#                   FROM Railfall 
#                   WHERE name=%s""",
#                (A1AB80))

cursor.execute("SELECT PublishTime FROM Railfall WHERE SiteId = %s", ("A1AB80",))


# fetch all of the rows from the query
data = cursor.fetchall ()
# print the rows
# print data [0][1]
for row in data :
	print row[0]
# close the cursor object
cursor.close ()
# close the connection
connection.close ()
# exit the program
sys.exit()

import sqlite3

conn = sqlite3.connect('ErnerNOC')
c = conn.cursor()
#c.execute("select * from HourlyStats where date(date)= date('2012-01-01') and file ='99.csv'")
c.execute("select * from HourlyStats where date(date)= date('2012-01-01')")
for row in c.fetchall():
    print (row)


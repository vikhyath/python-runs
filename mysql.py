#mysql example with python
import MySQLdb

db=mysql.connect(host='engsup-web-01.rtp.netapp.com', user='web', passwd='web', db='asup')
c = db.cursor()
c.execute("select * from delta_states where id = %d" %(1))
c.fetchone()
# c.fetchmany(n) or c.fetchall(). 

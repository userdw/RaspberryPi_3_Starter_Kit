import sqlite3
import time
import datetime
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style

conn = sqlite3.connect("library.db")
c = conn.cursor()

_students = "(student_id, student_name, student_addr)"
_members = "(member_id, student_id, date_list)"
_books = "(book_id, title, author, publisher)"
_guest = "(guest_id, member_id, date_list)"

def _createTable(_tableName, _atribut):
	commands = "CREATE table if not exists " + _tableName + " " + _atribut
	c.execute(commands)
	 
def _dataEntry(_tableName, _entitas, _data ):
	_data2 = "(" + str(_data)[1:-1] + ")"
	commands = "INSERT into " + _tableName + " " + _entitas + " VALUES " + _data2
	c.execute(commands)
	conn.commit()

#date = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
#_createTable("students", "(student_id REAL, student_name TEXT, student_addr TEXT)")
#_createTable("members", "(member_id REAL, student_id REAL, date_list TEXT)")
#_createTable("books", "(book_id REAL, title TEXT, author TEXT, publisher TEXT)")
#_createTable("guest", "(guest_id REAL, member_id REAL, date_list TEXT)")

#_dataEntry("students", _students, ['20170009', 'Harris', 'Surabaya'])
#_dataEntry("members", _members, ['P_0001', '20170001', date])
#_dataEntry("books", _books, ['B-5001', 'How to Be a Smart Person', 'William Shockley', 'Publishing.Inc'])


#for i in range (0,10):
	#date = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d')
	#_dataEntry("guest", _guest, [11, 'P_0002', '2017-11-24'])
	#time.sleep(2)

#c.close()
#conn.close()

df = pd.read_sql_query("SELECT * from students", conn)
df1 = pd.read_sql_query("SELECT * from members", conn)
df2 = pd.read_sql_query("SELECT * from books", conn)
df3 = pd.read_sql_query("SELECT * from guest", conn)
#print (df)
#print (df1)
#print (df2)
#print (df3)

import pymysql
from config import con,cur
con = pymysql.connect(user='root',host='localhost',database='demo')
cur = con.cursor()


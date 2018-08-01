import pymysql
from config import con,cur
con = pymysql.connect(user='be66e459d6f8f5',password='50eb0638',host='us-cdbr-iron-east-01.cleardb.net',database='heroku_9d30db5356467f4')
cur = con.cursor()


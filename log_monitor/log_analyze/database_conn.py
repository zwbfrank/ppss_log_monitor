import os
import sys
import django
import pymysql

config = {
	'db': 'log_DB',
	'user': 'root',
	'password': 'password',
	'host': '127.0.0.1',
	'port': 3306,
	'charset': 'utf8',
}

def pymysql_conn():
	conn = pymysql.connect(**config)
	# cursor = conn.cursor()
	return conn
	

def get_mysql_data():
	conn = pymysql_conn()
	cursor = conn.cursor()
	sql = 'select *from log_analyze_logmonitor'
	cursor.execute(sql)
	data = cursor.fetchall()
	log_path = data[0][2]
	cursor.close()
	conn.close()
	# conn.close()
	return log_path

if __name__ == '__main__':
	# config = {
	#     'db': 'log_DB',
	#     'user': 'root',
	#     'password': 'password',
	#     'host': '127.0.0.1',
	#     'port': 3306,
	#     'charset': 'utf8'
	# }
	# pymysql_conn()
	data = get_mysql_data()
	print(data)

# config = {
#     'db': 'log_DB',
#     'user': 'root',
#     'password': 'password',
#     'host': '127.0.0.1',
#     'port': 3306,
#     'charset': 'utf8'
# }

# conn = pymysql.connect(**config)
# cursor = conn.cursor()
# sql = 'select *from log_analyze_logmonitor'
# cursor.execute(sql)
# data = cursor.fetchall()
# log_path = data[0][2]
# print(log_path)


import sqlite3
from employee import Employee

global emp_1
global emp_2
emp_1 = Employee('John', 'Doe', 25, 80000)
emp_2 = Employee('Jane', 'Doe', 20, 90000)


def connect_database():
	connect = sqlite3.connect("employee.db")
	cursor = connect.cursor()

def create_database():
	connect = sqlite3.connect("employee.db")
	cursor = connect.cursor()
	cursor.execute("""Create table if not exists employees (
				first_name text,
				last_name text,
				age integer,
				pay integer
		)""")
	connect.commit()
	connect.close()

def insert_database():
	connect = sqlite3.connect("employee.db")
	cursor = connect.cursor()
	cursor.execute("INSERT INTO employees VALUES (?, ?, ?, ?)", (emp_1.first_name, emp_1.last_name, emp_1.age, emp_1.pay))
	connect.commit()
	connect.close()

def view_database():
	connect = sqlite3.connect("employee.db")
	cursor = connect.cursor()
	cursor.execute("""SELECT * FROM employees""")
	rows = cursor.fetchall()
	connect.commit()
	return rows
	connect.close()

connect_database()
create_database()
#insert_database()
print(view_database())
import sqlite3

class Employee:
	
	def __init__(self, first_name, last_name, age, pay):
		self.first_name = first_name
		self.last_name = last_name
		self.age = age
		self.pay = pay

	@property
	def email(self):
		return f'{self.first_name}.{self.last_name}@gmail.com'

	def fullName(self):
		return f'{self.first_name} {self.last_name}'

	def getName(self):
		return self.first_name

	def getLastName(self):
		return self.last_name

	def getAge(self):
		return age


	def connect_database(self):
		connect = sqlite3.connect("employee.db")
		cursor = connect.cursor()

	def create_database():
		connect = sqlite3.connect("employee.db")
		cursor = connect.cursor()
		cursor.execute("""CREATE TABLE IF NOT EXISTS employees (
					id INTEGER PRIMARY KEY,
					first_name text,
					last_name text,
					age integer,
					pay integer
			)""")
		connect.commit()
		connect.close()

	def insert_database(self):
		connect = sqlite3.connect("employee.db")
		cursor = connect.cursor()
		cursor.execute("INSERT INTO employees VALUES (NULL, ?, ?, ?, ?)", (self.first_name, self.last_name, self.age, self.pay
			))
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

	def delete_database(id):
		connect = sqlite3.connect("employee.db")
		cursor = connect.cursor()
		cursor.execute("""DELETE FROM employees WHERE id=?""", (id,))
		connect.commit()
		connect.close()

	def update_database(first_name, last_name, age, pay, id):
		connect = sqlite3.connect("employee.db")
		cursor = connect.cursor()
		cursor.execute("""UPDATE employees SET first_name=?, last_name=?, age=?, pay=? WHERE id=?""", (first_name, last_name, age, pay, id))
		connect.commit()
		connect.close()

	def search_database(first_name="", last_name="", age="", pay=""):
		connect = sqlite3.connect("employee.db")
		cursor = connect.cursor()
		cursor.execute("""SELECT * FROM employees WHERE first_name=? OR last_name=? OR age=? OR pay=?""", (first_name, last_name, age, pay))
		rows = cursor.fetchall()
		connect.commit()
		connect.close()
		return rows

	def __repr__(self):
		return f'Employee {self.first_name}, {self.last_name} pay {self.pay}'

emp1 = Employee('Tanjil', 'Khan', 14, 90000)
emp2 = Employee('Jack', 'Bill', 35, 150000)
Employee.create_database()
#Employee.insert_database(emp1)
#Employee.insert_database(emp2)
print(Employee.view_database())
print(len(Employee.view_database()))
#Employee.delete_database(2)
#print(Employee.view_database())
#print(len(Employee.view_database()))
Employee.update_database('John', 'Doe', 20, 20000, 1)
print(Employee.search_database('Jack'))
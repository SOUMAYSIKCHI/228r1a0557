import  sqlite3

def create_table():
    conn = sqlite3.connect('Employees.db')
    cur = conn.cursor()

    cur.execute('''
    CREATE TABLE IF NOT EXISTS EMPLOYEES (id TEXT PRIMARY KEY,
    name Text,
    role Text,
    gender Text,
    status Text)''')
    conn.commit()
    conn.close()

def fetch_employees():
    conn = sqlite3.connect('Employees.db')
    cur = conn.cursor()
    cur.execute('SELECT * FROM Employees')
    employees = cur.fetchall()
    conn.close()
    return employees

def insert_employee(id,name,role,gender,status):
    conn = sqlite3.connect('Employees.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO Employees(id,name,role,gender,status) VALUES(?,?,?,?,?)',(id,name,role,gender,status))
    conn.commit()
    conn.close()

def delete_employee(id):
    conn = sqlite3.connect('Employees.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM Employees WHERE id = ?',(id,))
    conn.commit()
    conn.close()

def update_employee(new_name,new_role,new_gender,new_status,id):
    conn = sqlite3.connect('Employees.db')
    cursor = conn.cursor()
    cursor.execute("Update Employees SET name = ? ,role = ?,gender = ?,status = ? where id = ?",(new_name,new_role,new_gender,new_status,id))
    conn.commit()
    conn.close()

def id_exists(id):
    conn = sqlite3.connect('Employees.db')
    cursor = conn.cursor()
    cursor.execute('SELECT COUNT(*) FROM employees Where id = ?',(id,))
    result = cursor.fetchone()
    conn.cursor()
    return result[0]>0

create_table()

import pyodbc 

conn = pyodbc.connect('DRIVER={SQL Server}; SERVER=YAMI-CHANOWO\\SQLEXPRESS; DATABASE=QLSinhVien; Trusted_Connection=yes')
cursor = conn.cursor()
cursor.execute("SELECT @@version")

db_version = cursor.fetchone()
conn.close()
print (db_version)
import sqlite3

connection = sqlite3.connect('student.db')

curesor = connection.cursor()

table_info  = """
CREATE TABLE IF NOT EXISTS student (NAME VARCHAR(50) NOT NULL,
SECTION VARCHAR(50) NOT NULL,
MARK INTEGER NOT NULL);

"""

curesor.execute(table_info)

curesor.execute("INSERT INTO student (NAME, SECTION, MARK) VALUES ('John Doe', 'A', 85)")
curesor.execute("INSERT INTO student (NAME, SECTION, MARK) VALUES ('Jane Smith', 'B', 90)")
curesor.execute("INSERT INTO student (NAME, SECTION, MARK) VALUES ('Alice Johnson', 'A', 78)")
curesor.execute("INSERT INTO student (NAME, SECTION, MARK) VALUES ('Bob Brown', 'C', 88)")
curesor.execute("INSERT INTO student (NAME, SECTION, MARK) VALUES ('Charlie Black', 'B', 92)")
curesor.execute("INSERT INTO student (NAME, SECTION, MARK) VALUES ('David White', 'A', 75)")
curesor.execute("INSERT INTO student (NAME, SECTION, MARK) VALUES ('Eva Green', 'C', 95)")
curesor.execute("INSERT INTO student (NAME, SECTION, MARK) VALUES ('Frank Blue', 'B', 80)")
curesor.execute("INSERT INTO student (NAME, SECTION, MARK) VALUES ('Grace Yellow', 'A', 88)")
curesor.execute("INSERT INTO student (NAME, SECTION, MARK) VALUES ('Henry Orange', 'C', 82)")
curesor.execute("INSERT INTO student (NAME, SECTION, MARK) VALUES ('Ivy Purple', 'B', 91)")
curesor.execute("INSERT INTO student (NAME, SECTION, MARK) VALUES ('Jack Red', 'A', 87)")

print("The inserted records are:")

data = curesor.execute("SELECT * FROM student").fetchall()

for row in data:
    print(row)

connection.commit()
connection.close()
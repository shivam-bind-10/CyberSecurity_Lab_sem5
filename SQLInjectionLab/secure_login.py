import sqlite3

# Take username and password from user
username = input("Enter username: ")
password = input("Enter password: ")

# Connect to the database
conn = sqlite3.connect("university.db")

cursor = conn.cursor()

# Secure parameterized query
query = """
SELECT * FROM students
WHERE username = ?
AND password = ?
"""

# Execute query safely
cursor.execute(query, (username, password))

# Get login result
result = cursor.fetchone()

# Check whether login is successful
if result:
    print("Login Successful")
else:
    print("Login Failed")

# Close database connection
conn.close()
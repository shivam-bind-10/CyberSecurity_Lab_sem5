import sqlite3

# Connect to database
conn = sqlite3.connect("university.db")

# Create cursor
cursor = conn.cursor()

# Create students table
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    username TEXT,
    password TEXT
)
""")

# Insert student data
cursor.execute(
    "INSERT INTO students VALUES (?, ?)",
    ("rahul", "pass123")
)

# Save changes
conn.commit()

# Close database
conn.close()

print("Database created successfully!")
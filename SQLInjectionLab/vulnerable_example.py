username = input("Enter username: ")
password = input("Enter password: ")

query = (
    "SELECT * FROM students "
    "WHERE username = '" + username +
    "' AND password = '" + password + "'"
)

print("\nGenerated SQL Query:")
print(query)
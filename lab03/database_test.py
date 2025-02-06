import sqlite3

conn = sqlite3.connect('users.db')  # Connect to database
cursor = conn.cursor()

# Create a table (if not exists)
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY,
        name TEXT,
        age INTEGER
    )
''')

# Insert a user
cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("Alice", 25))
conn.commit()

# Fetch and print users
cursor.execute("SELECT * FROM users")
users = cursor.fetchall()

for user in users:
    print(user)

conn.close()

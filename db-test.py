import sqlite3

# Connect to a new database
conn = sqlite3.connect("people.db")

# Create a cursor
cur = conn.cursor()

# test data
names_list = [
    ("John", "Doe"),
    ("Jane", "Doe"),
    ("John", "Smith")
]

# Create a table
cur.executemany(
    """
    INSERT INTO people (first_name, last_name)
    VALUES (?, ?)
    """, names_list
)
conn.commit()


# Close connection
conn.close()
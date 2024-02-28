import sqlite3
import cleaned_data

# Connect to SQLite database (creates a new database if it doesn't exist)
conn = sqlite3.connect('podcast_data.db')

# Create a cursor object to execute SQL commands
cursor = conn.cursor()


# Should be able to functionize most of these

# # Create a table to store podcast episode data
# cursor.execute('''CREATE TABLE episodes
#                 (id INTEGER PRIMARY KEY,
#                 title TEXT,
#                 summary TEXT,
#                 guest TEXT,
#                 duration INTEGER,
#                 release_date TEXT,
#                 transcript TEXT)''')

# # Add a new column to the existing table
# cursor.execute('''ALTER TABLE episodes
#                 ADD COLUMN audio_url TEXT''')
# Func to add column to table
def add_column(column_name: str, col_type='TEXT'):
    cursor.execute(f'''ALTER TABLE episodes
                    ADD COLUMN {column_name} {col_type}''')


# # # Populate the id column with numerical IDs from 1 to 51 (there are 51 podcasts currently)
# # # The '?' relates to the item(s) in the parens
# for episode_id in range(1, 52):
#     cursor.execute('''INSERT INTO episodes
#                     (id)
#                     VALUES (?)''', (episode_id,))

# # Populate the title column with the titles
# titles = cleaned_data.titles
# # `start=1` because otherwise it would start at 0, and in our table the rows start at 1
# for i, title in enumerate(titles, start=1):
#     cursor.execute('''UPDATE episodes
#                     SET title = ?
#                     WHERE id = ?''', (title, i))

# Func to add guest names to table from .txt file
def add_guests(file_name):
    guests = cleaned_data.guest_list(file_name)
    for i, guest in enumerate(guests, start=1):
        cursor.execute('''UPDATE episodes
                        SET guest = ?
                        WHERE id = ?''', (guest, i))


# Func to add podcast durations to table from list
def add_durations():
    durations = cleaned_data.duration_list()
    for i, duration in enumerate(durations, start=1):
        cursor.execute('''UPDATE episodes
                        SET duration = ?
                        WHERE id = ?''', (duration, i))


# Func to add publish date to table from list
def add_publish_date():
    publish_dates = cleaned_data.date_list()
    for i, date in enumerate(publish_dates, start=1):
        cursor.execute('''UPDATE episodes
                        SET release_date = ?
                        WHERE id = ?''', (date, i))


# Func to add audio url to table from list
def add_audio_url():
    urls = cleaned_data.url_list()
    for i, url in enumerate(urls, start=1):
        cursor.execute('''UPDATE episodes
                        SET audio_url = ?
                        WHERE id = ?''', (url, i))


# # Execute a query to select and display all rows from the episodes table
# data = cursor.execute('''SELECT * FROM episodes''')
# for row in data:
#     print(row)

# Commit changes and close the connection
conn.commit()
conn.close()

import pandas as pd
import sqlite3

# Step 1: Upload CSV to Pandas
csv_file_path = r"C:\Users\Hp\Desktop\genai_sql\bollywood_movie.csv"  # Using raw string for file path
df = pd.read_csv(csv_file_path)
print("DataFrame loaded from CSV:")
print(df.head())  # Show the first 5 rows of the DataFrame

# Step 2: Move the CSV to SQLite Database
conn = sqlite3.connect('bollywood_movie.db')  # Connect to the SQLite database
cursor = conn.cursor()

# Create a new table in SQLite to hold the movie data (if it doesn't exist)
cursor.execute('''
CREATE TABLE IF NOT EXISTS Movies (
    Title TEXT,
    Type TEXT,
    Release_Year INTEGER,
    Genre TEXT,
    Director TEXT,
    Production_House TEXT,
    Lead_Actors TEXT,
    Language TEXT,
    Budget_Millions REAL,
    Box_Office_Millions REAL,
    OTT_Platform TEXT,
    Runtime_Minutes INTEGER,
    No_of_Episodes INTEGER,
    IMDb_Rating REAL,
    Audience_Score INTEGER,
    Critics_Score INTEGER,
    Awards_Nominations INTEGER,
    Awards_Won INTEGER,
    Social_Media_Mentions INTEGER,
    User_Reviews_Count INTEGER,
    Viewership_Hours_Million REAL
)
''')

# Insert data from DataFrame into the SQLite table
# Note: Using if_exists='replace' to ensure table is overwritten if it already exists
df.to_sql('Movies', conn, if_exists='replace', index=False)

# Commit changes
conn.commit()

# Sample Query: Retrieve top 5 movies from the Movies table
query = '''SELECT * FROM Movies LIMIT 5'''
result = cursor.execute(query)

# Print the result of the query
print("\nTop 5 Movies:")
for row in result:
    print(row)

# Close the database connection
conn.close()

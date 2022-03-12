# Importing all libraries
import pandas as pd
import numpy as np
import sqlite3
from pathlib import Path

#Fetching first 10 records of the Data
users = pd.read_csv('DATA.csv')
users.head(10)

#Check for the null value in the csv file
users = users.isnull().sum()
users

#Create a SQLite database
Path('SFL.db').touch()

#Create the SQLite table
conn = sqlite3.connect('SFL')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS users (
  id int,
  first_name text,
  last_name text,
  email varchar,
  gender text,
  ip_address varchar
)''')

#Load csv file into SQLite table
users = pd.read_csv('Data.csv')
users.to_sql('users', conn, if_exists='append', index = False)

#Executing the SQL query to fetch the records in array format
c.execute('''SELECT * FROM users limit 10''').fetchall()

#Executing the query using pandas library
df = pd.read_sql('''SELECT * FROM users''', conn)
df.head(10)
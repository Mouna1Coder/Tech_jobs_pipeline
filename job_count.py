import pandas as pd
import mysql.connector
from db_connection import connect_to_db
import matplotlib.pyplot as plt

# Fetch into pandas
conn = connect_to_db()
df = pd.read_sql("SELECT location FROM jobs", conn)
conn.close()

# Prepare counts
counts = df['location'].value_counts()

# Plot
counts.plot(kind='bar')
plt.title('Jobs by Location')
plt.xlabel('Location')
plt.ylabel('Number of Jobs')
plt.show()

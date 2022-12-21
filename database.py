import sqlite3
from pprint import pprint

# Query the database and return records
def show_all():

    # connect to the database
    conn = sqlite3.connect('players.db')
# Create a cursor
    cursor = conn.cursor()

    cursor.execute("SELECT rowid, * FROM players")
    items = cursor.fetchall()

    for item in items:
        pprint(items)

    conn.commit()

    conn.close()

def add_one(first,last,player_rating):
    conn = sqlite3.connect("players.db")
    c = conn.cursor
    c.execute("INSERT INTO players VALUES(?,?,?)",(first,last,player_rating))
    
    conn.commit()

    conn.close()
import sqlite3 
with sqlite3.connect("AudioTour2.db") as db: # connect to the database
            cursor = db.cursor() # create cursor
            cursor.execute("SELECT *FROM Main_tbl")
            products = cursor.fetchall()
            print (products)
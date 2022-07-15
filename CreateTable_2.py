import sqlite3 as sql

def main():
    try: 
        db = sql.connect('BukuTelefonIndah.db')
        cur = db.cursor()
        tablequery = "CREATE TABLE Users (id INT, namadepan TEXT, namabelakang TEXT, kota TEXT, notelefon TEXT, email TEXT)"

        cur.execute(tablequery)
        print("Table Created Succesfully")

    except sql.Error as e:
        print("There is a table or an error has occurred")

    finally:
        db.close()
        
if __name__ == "__main__":
    main()
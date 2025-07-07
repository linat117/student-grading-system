import mysql.connector

def db_connection():
    try:
        db =  mysql.connector.connect(
            host = "localhost",
            user="root",
            password = "",
            database = "student-grading-system"
        )
        return db
    except mysql.connector.Error as err:
          print("❌ Database connection error:", err)
          return None

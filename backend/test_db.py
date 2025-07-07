from db_config import db_connection 

db = db_connection()

if db:
    print("Connectd")
else:
    print("not connected.")
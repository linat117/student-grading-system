from db_config import db_connection 

def add_student():
    db = None
    cursor = None
    try:
        db = db_connection()
        cursor = db.cursor()

        student_id = int(input("Enter studentID: "))
        name = input("Enter student name: ")
        age = int(input("Enter age: "))
        major = input("Enter major: ")

        cursor.execute("""
            INSERT INTO students (id, name, age, major)
            VALUES (%s, %s, %s, %s)
        """, (student_id, name, age, major))

        db.commit()
        print("✅ Student added successfully.")

    except Exception as e:
        print("❌ Error adding student:", e)
    finally:
        if cursor:
            
            cursor.close()
        if db:

            db.close()
def list_students():
     try:
        db = db_connection()
        cursor = db.cursor()

        cursor.execute("SELECT * FROM students")
        students = cursor.fetchall()
        for student in students:
            print(f"ID: {student[0]} | Name: {student[1]} | Age: {student[2]} | Major: {student[3]}")

     except Exception as e:
        print("❌ Error fetching students:", e)
     finally:
        cursor.close()
        db.close()

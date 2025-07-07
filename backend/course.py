from db_config import db_connection 


def add_course():
    try:
        db = db_connection()
        cursor = db.cursor()

        course_id = int(input("Enter the course ID : "))
        course_name = input("Enter the course name : ")
        instructor = input("Enter the instructor name : ")

        cursor.execute("""
            INSERT INTO courses (id,name,instructor)
                        VALUES (%s, %s, %s)""",
                        (course_id, course_name, instructor))
        
        db.commit()
        print("✔️Course added successfully!")
    
    except Exception as e:
        print("Error adding course:", e)
    finally:
        cursor.close()
        db.close()

def list_courses():
    try:
        db = db_connection()
        cursor = db.cursor()

        cursor.execute("SELECT * FROM courses")
        courses  = cursor.fetchall()
        for course in courses:
            print(f" ID : {course[0]} | Name : {course[1]} | Instructor = {course[2]}")

    except Exception as e:
        print("Error fetching course.")
    finally:
        cursor.close()
        db.close()
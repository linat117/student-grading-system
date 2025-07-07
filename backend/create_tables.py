from db_config import db_connection 
try: 
    db = db_connection()
    cursor = db.cursor()

    cursor.execute("""
    CREATE TABLE students(
         id INT PRIMARY KEY,
         name VARCHAR(100),
         age INT,
         major VARCHAR(100)          
               )
               """)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS courses (
        id INT PRIMARY KEY,
        name VARCHAR(100),
        instructor VARCHAR(100)
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS grades (
        id INT AUTO_INCREMENT PRIMARY KEY,
        student_id INT,
        course_id INT,
        score FLOAT,
        grade_letter VARCHAR(2),
        semester VARCHAR(20),
        FOREIGN KEY (student_id) REFERENCES students(id),
        FOREIGN KEY (course_id) REFERENCES courses(id)
    )
    """)

    print("✔️ All tables created successfully!")

except Exception as e:
    print("❌ Error:", e)

finally:
    cursor.close()
    db.close()
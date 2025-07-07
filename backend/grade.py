from db_config import db_connection

def assign_grade():
    try:
        db = db_connection()
        cursor = db.cursor()

        student_id = int(input("Enter student ID: "))
        course_id = int(input("Enter course ID: "))
        score = float(input("Enter score (0-100): "))
        semester = input("Enter semester (e.g., Fall 2025): ")

        # Grade calculation
        if score >= 90:
            grade_letter = "A"
        elif score >= 80:
            grade_letter = "B"
        elif score >= 70:
            grade_letter = "C"
        else:
            grade_letter = "F"

        cursor.execute("""
            INSERT INTO grades (student_id, course_id, score, grade_letter, semester)
            VALUES (%s, %s, %s, %s, %s)
        """, (student_id, course_id, score, grade_letter, semester))

        db.commit()
        print("✅ Grade assigned successfully.")

    except Exception as e:
        print("❌ Error assigning grade:", e)
    finally:
        cursor.close()
        db.close()


def view_transcript(student_id):
    try:
        db = db_connection()
        cursor = db.cursor()

        cursor.execute("""
            SELECT c.name, g.score, g.grade_letter, g.semester
            FROM grades g
            JOIN courses c ON g.course_id = c.id
            WHERE g.student_id = %s
        """, (student_id,))

        transcript = cursor.fetchall()

        print(f"\n📄 Transcript for Student ID {student_id}")
        print("-" * 50)
        for row in transcript:
            course, score, letter, semester = row
            print(f"{course} | Score: {score} | Grade: {letter} | Semester: {semester}")
        print("-" * 50)

    except Exception as e:
        print("❌ Error viewing transcript:", e)
    finally:
        cursor.close()
        db.close()

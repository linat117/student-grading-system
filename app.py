from flask import Flask, render_template, request, redirect, url_for, flash
from db_config import db_connection

app = Flask(__name__)
app.secret_key = 'your-secret-key'  # Needed for flashing messages

@app.route('/')
def index():
    return render_template('base.html')

# Add Student
@app.route('/add_student', methods=['GET', 'POST'])
def add_student():
    if request.method == 'POST':
        try:
            student_id = int(request.form['id'])
            name = request.form['name']
            age = int(request.form['age'])
            major = request.form['major']

            db = db_connection()
            cursor = db.cursor()
            cursor.execute(
                "INSERT INTO students (id, name, age, major) VALUES (%s, %s, %s, %s)",
                (student_id, name, age, major)
            )
            db.commit()
            cursor.close()
            db.close()

            flash('Student added successfully!', 'success')
            return redirect(url_for('add_student'))
        except Exception as e:
            flash(f'Error: {e}', 'danger')

    return render_template('add_student.html')


# Add Course
@app.route('/add_course', methods=['GET', 'POST'])
def add_course():
    if request.method == 'POST':
        try:
            course_id = int(request.form['id'])
            name = request.form['name']
            instructor = request.form['instructor']

            db = db_connection()
            cursor = db.cursor()
            cursor.execute(
                "INSERT INTO courses (id, name, instructor) VALUES (%s, %s, %s)",
                (course_id, name, instructor)
            )
            db.commit()
            cursor.close()
            db.close()

            flash('Course added successfully!', 'success')
            return redirect(url_for('add_course'))
        except Exception as e:
            flash(f'Error: {e}', 'danger')

    return render_template('add_course.html')


# Assign Grade
@app.route('/assign_grade', methods=['GET', 'POST'])
def assign_grade():
    if request.method == 'POST':
        try:
            student_id = int(request.form['student_id'])
            course_id = int(request.form['course_id'])
            score = float(request.form['score'])
            semester = request.form['semester']

            def grade_letter(score):
                if score >= 90: return 'A'
                elif score >= 80: return 'B'
                elif score >= 70: return 'C'
                elif score >= 60: return 'D'
                else: return 'F'

            letter = grade_letter(score)

            db = db_connection()
            cursor = db.cursor()
            cursor.execute(
                "INSERT INTO grades (student_id, course_id, score, grade_letter, semester) VALUES (%s, %s, %s, %s, %s)",
                (student_id, course_id, score, letter, semester)
            )
            db.commit()
            cursor.close()
            db.close()

            flash('Grade assigned successfully!', 'success')
            return redirect(url_for('assign_grade'))
        except Exception as e:
            flash(f'Error: {e}', 'danger')

    return render_template('assign_grade.html')


# View Transcript
@app.route('/view_transcript', methods=['GET', 'POST'])
def view_transcript():
    if request.method == 'POST':
        try:
            student_id = int(request.form['student_id'])

            db = db_connection()
            cursor = db.cursor()
            cursor.execute("""
                SELECT c.name, g.score, g.grade_letter, g.semester
                FROM grades g
                JOIN courses c ON g.course_id = c.id
                WHERE g.student_id = %s
            """, (student_id,))
            grades = cursor.fetchall()
            cursor.close()
            db.close()

            return render_template('transcript.html', grades=grades, student_id=student_id)
        except Exception as e:
            flash(f'Error: {e}', 'danger')

    return render_template('view_transcript.html')


if __name__ == '__main__':
    app.run(debug=True)

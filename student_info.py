from flask import Flask, request, jsonify

app = Flask(__name__)

# Mock student database
students = {
    "12345": {"name": "John Doe", "course": "Data Science", "year": "3", "gpa": 3.7},
    "67890": {"name": "Jane Smith", "course": "Information Systems", "year": "2", "gpa": 9.9}
}

# Fetch student info by ID
@app.route('/api/student')
def get_student():
    student_id = request.args.get('id')
    student = students.get(student_id)

    if not student:
        return jsonify({"error": "Student not found"}), 404

    return jsonify(student)

# Get total number of students
@app.route('/api/students/count')
def student_count():
    return jsonify({"total_students": len(students)})

if __name__ == "__main__":
    app.run(debug=True)

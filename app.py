from flask import Flask, render_template, request
from attendance.attendance import mark_attendance
from recognition.recognition import recognize_face

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/mark_attendance', methods=['POST'])
def mark_attendance_route():
    employee_id = recognize_face()  # This should return the recognized employee ID
    if employee_id:
        mark_attendance(employee_id)
        return f"Attendance marked for employee ID: {employee_id}"
    return "No face recognized."

if __name__ == '__main__':
    app.run(debug=True)

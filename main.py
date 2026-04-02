from flask import Flask, render_template

app = Flask(__name__)

students = ['Ali', 'Vali', 'Guli', 'Zafar', 'Nilufar', 'Sardor', 'Malika']
@app.route('/')
def home():
    student_count = len(students)
    return render_template(
        'students.html', 
        student_count = student_count,
        students = students
    )


if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask

from student import Student

students = []

app = Flask(__name__)


@app.route("/", methods={"GET", "POST"})
def student_page():
    if request.method == "POST":
        new_student_id =  request.form.get("student-id", "")
        new_student_name = request.form.get("name", "")
        new_student_last_name = request.form.get("last-name", "")

        new_student = Student(name=new_student_name,student_id=new_student_id)
        students.append(new_student)

        return redirect(url_for("student_page"))

    return render_template("index.html", students=students)


if __name__ == "__main__":
    app.run(debug=True)


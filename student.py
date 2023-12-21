from flask import Flask
import json
from flask import jsonify, request


app = Flask("__name__")


@app.route("/list", methods=["POST", "GET"])
def list_data():
    with open('studentdata.json', 'r') as file:
        student_data = json.load(file)

    student_data = student_data["students"]

    std = request.args.get("std", default=None)

    if std is None:
        return jsonify(student_data)
    else:
        res_list = []
        for student_data in student_data:
            if student_data["std"] == int(std):
                res_list.append(student_data)
        return jsonify(res_list)


@app.route("/student-data", methods=["get"])
def student_data():

    with open('studentdata.json', 'r') as file:
        studentdata = json.load(file)

    studentdata = studentdata["students"]

    name = request.args.get("name", default=None)
    res_list = []
    for studentdata in studentdata:
        if studentdata["name"] == name:
            res_list = studentdata

    if name is None:
        return f"please enter student name"
    elif len(res_list) == 0:
        return f"No student found with the name {name}"
    else:
        return jsonify(res_list)


@app.route("/add-data", methods=["post"])
def add_data():

    with open("studentdata.json", "r") as file:
        student_data= json.load(file)

    data = request.get_json()

    student_data["students"].append(data)

    with open("studentdata.json", "w") as file:
        json.dump(student_data, file)
    return jsonify({"message": "Data added successfully"}), 200


@app.route("/update-data/<string:name>", methods=["put"])
def update_data(name):

    with open("studentdata.json", "r") as file:
        student_data = json.load(file)

    students = student_data["students"]

    for student in students:
        if student["name"] == name:
            student.update(request.get_json())  # Update the student's data
            with open("studentdata.json", "w") as file:
                json.dump(student_data, file)
            return jsonify({"message": "Student data updated successfully"}), 200

    return jsonify({"error": "Student not found"}), 404

@app.route("/delete-data", methods=["delete"])

def delete_data():

    with open("studentdata.json", "r") as file:
        student_data = json.load(file)

    students = student_data["students"]
    name = request.args.get("name", default=None)

    student_to_remove = None

    for student in students:
        if student["name"] == name:
            student_to_remove = student
            break

    if student_to_remove:
        students.remove(student_to_remove)  # Remove the student from the list
        with open("studentdata.json", "w") as file:
            json.dump(student_data, file)  # Save the updated data to the JSON file
        return jsonify({"message": f"Student {name} deleted successfully"}), 200
    else:
        return jsonify({"error": f"Student {name} not found"}), 404


if __name__ == "__main__":
    app.run(debug=True)

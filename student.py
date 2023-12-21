from flask import Flask
import json
from flask import jsonify, request


app = Flask("__name__")


@app.route("/list", methods=["POST"])
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


if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, request, jsonify
import helper

app = Flask(__name__)

"""CONSTANTS"""
FILENAME = "data.json"


@app.route("/")
def home():
    return jsonify("Welcome to Raghav's API Challenge!")


@app.route("/todo", methods=["GET", "POST"])
def todos():
    if request.method == "GET":
        return helper.get_todos(FILENAME)

    elif request.method == "POST":
        add_data = request.get_json()
        return helper.add_todo(add_data)


@app.route("/todo/<modified_id>", methods=["GET", "PUT", "DELETE"])
def delete_id(modified_id):
    if request.method == "GET":
        return helper.get_specific_id(modified_id, FILENAME)

    elif request.method == "DELETE":
        return helper.delete_json_item(modified_id, FILENAME)

    elif request.method == "PUT":
        edit_data = request.get_json()
        return helper.edit_todo_item(edit_data, modified_id, FILENAME)

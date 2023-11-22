from flask import Flask, request, jsonify
import json
import helper

app = Flask(__name__)

"""CONSTANTS"""
FILENAME = "data.json"


@app.route("/")
def home():
    return jsonify("Welcome to Raghav's API Challenge!")


@app.route("/todo", methods=["GET", "POST", "PUT", "DELETE", "PATCH"])
def todos():
    if request.method == "GET":
        return helper.get_todos(FILENAME), {'content-type': 'application/json'}

    elif request.method == "POST":
        add_data = request.get_json()
        return helper.add_todo(add_data), {'content-type': 'application/json'}

    elif request.method == "PUT" or request.method == "DELETE" or request.method == "PATCH":
        error = {"error": "Method Not Allowed"}
        return json.dumps(error), 405, {'content-type': 'application/json'}


@app.route("/todo/<modified_id>", methods=["GET", "PUT", "DELETE", "POST"])
def delete_id(modified_id):
    if request.method == "GET":
        return helper.get_specific_id(modified_id, FILENAME), {'content-type': 'application/json'}

    elif request.method == "DELETE":
        return helper.delete_json_item(modified_id, FILENAME), {'content-type': 'application/json'}

    elif request.method == "PUT":
        edit_data = request.get_json()
        return helper.edit_todo_item(edit_data, modified_id, FILENAME), {'content-type': 'application/json'}

    elif request.method == "POST":
        error = {"error": "Method Not Allowed"}
        return json.dumps(error), 405, {'content-type': 'application/json'}

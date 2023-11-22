import json
import uuid
from schema import Schema, And, Use, SchemaError
from flask import jsonify
import logging

"""CONSTANTS"""
FILE_NOT_FOUND = "File not found\n"
LOGFILE = "log.txt"
FILENAME = "data.json"
JSON_FORMAT = Schema({
    "Title": And(Use(str)),
    "Description": And(Use(str)),
    "DoneStatus": And(Use(bool))
})


def load_json(filename):
    """
    This function loads the json file to and returns a list
    :param filename: A valid json file
    :return: A list of dictionaries
    """
    try:
        with open(filename, "r") as file:
            json_data = json.load(file)
        return json_data
    except FileNotFoundError:
        with open(LOGFILE, "a") as logfile:
            logfile.write(FILE_NOT_FOUND)
        return json.dumps({"Error": "JSON not in the expected format"}), 404
    except json.decoder.JSONDecodeError:
        with open(LOGFILE, "a") as logfile:
            logfile.write("JSON File not found\n")
        return json.dumps({"Error": "JSON not in the format"}), 404


def get_todos(filename):
    """
    This function returns a json object with the data in the file
    :param filename: A valid json path
    :return: A json object
    """
    all_todos = load_json(filename)
    lines = []
    for line in all_todos:
        lines.append(line)
    json_data = json.dumps(lines)
    return json_data


def update_json(data, filename="data.json"):
    """
    This function writes the data to the json file
    :param data: A dictionary of data
    :param filename: A valid json file path
    :return: A str with the status
    """
    try:
        with open(filename, "w") as file:
            json.dump(data, file)
        return "Updated"
    except Exception as err:
        with open(LOGFILE, "a") as logfile:
            logfile.write(f"Error Occurred: {err}\n")
        return json.dumps({"Error": "JSON not in the expected format"}), 404


def add_todo(json_file):
    """
    This function adds a to-do to the json file
    :param json_file: A list with dictionaries of todos
    :return: A str with the status
    """
    if check_json_structure(json_file):
        todo = json_file['Title']
        done = json_file['DoneStatus']
        description = json_file['Description']
        new_id = create_id()
        data = {"Title": todo, "doneStatus": done, "description": description, "id": new_id}
        json_data = load_json(FILENAME)
        json_data.append(data)
        with open("data.json", "w") as f:
            json.dump(json_data, f)
        with open(LOGFILE, "a") as logfile:
            logfile.write(f"ADDED todo: {data}")
        added_id = json.dumps({'id': data['id']})
        return added_id
    else:
        with open(LOGFILE, "a") as logfile:
            logfile.write(f"JSON not in the expected format: {json_file}\n")
        return json.dumps({"Error": "JSON not in the expected format"}), 404


def delete_json_item(del_id, filename):
    """
    This function deletes a json item if it is in the json file using the 'id'
    :param del_id: id of the to-do
    :param filename: The data.json file
    :return: the todos after deleting
    """
    todos = load_json(filename)
    for item in todos:
        if del_id in item['id']:
            item_data = item
            todos.remove(item_data)
    update_json(todos)
    return json.dumps(f"Deleted todo: {del_id}")


def edit_todo_item(edit_data, updates_edit_id, filename):
    """
    This function edits an existing to-do
    :param edit_data: A dictionary with keys "Title", "Description", "doneStatus"
    :param updates_edit_id: The to-do id that has to be edited
    :param filename: A valid json file with the particular to-do
    :return: updated to-do list
    """
    if check_json_structure(edit_data):
        todos = load_json(filename)
        for item in todos:
            if updates_edit_id in item['id']:
                item['Title'] = edit_data['Title']
                item['description'] = edit_data['Description']
                item['doneStatus'] = edit_data['DoneStatus']
        update_json(todos)
        get_updated_todos = load_json(filename)
        for edited_item in get_updated_todos:
            if updates_edit_id in edited_item['id']:
                edited_todo_item = json.dumps({
                    "Title": edited_item['Title'],
                    "description": edited_item['description'],
                    "doneStatus": edited_item['doneStatus'],
                    "id": edited_item['id']
                })
                return edited_todo_item
    else:
        with open(LOGFILE, "a") as logfile:
            logfile.write("JSON not in the expected format\n")
        return json.dumps({"Error": "JSON not in the expected format"}), 404


def get_specific_id(modified_id, filename):
    """
    :param modified_id: The id of the to-do to be modified
    :param filename: A valid json file with the particular to-do
    :return: A json with the specific to-do
    """
    get_todo = load_json(filename)
    for item in get_todo:
        if modified_id == item['id']:
            return json.dumps(item)


def check_json_structure(json_file):
    """
    This function uses validates if the format of the passed json is correct
    :param json_file: A dictionary
    :return: A boolean
    """
    try:
        JSON_FORMAT.validate(json_file)
        return True
    except SchemaError:
        return False


def create_id():
    """
    This function creates a unique hex id
    :return: A hex id
    """
    created_id = uuid.uuid4().hex
    return created_id

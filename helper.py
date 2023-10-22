import json
import uuid
from schema import Schema, And, Use, SchemaError
from flask import jsonify

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
    except json.decoder.JSONDecodeError:
        with open(LOGFILE, "a") as logfile:
            logfile.write("JSON File not found\n")


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
    return jsonify(lines)


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
        with open(LOGFILE, "a") as logfile:
            logfile.write("DELETED\n")
        return "Updated"
    except Exception as err:
        with open(LOGFILE, "a") as logfile:
            logfile.write(f"Error Occurred: {err}\n")


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
        return load_json(FILENAME)
    else:
        with open(LOGFILE) as logfile:
            logfile.write("JSON not in the expected format\n")
        return "JSON not in the expected format"


def delete_json_item(del_id, filename):
    """
    This function deletes a json item if it is in the json file using the id
    :param del_id: id of the to-do
    :param filename: The data.json file
    :return: the todos after deleting
    """
    get_todos = load_json(filename)
    for item in get_todos:
        if del_id in item['id']:
            item_data = item
            get_todos.remove(item_data)
    update_json(get_todos)
    return get_todos


def edit_todo_item(edit_data, updates_edit_id, filename):
    """
    This function edits an existing to-do
    :param edit_data: A dictionary with keys "Title", "Description", "doneStatus"
    :param updates_edit_id: The to-do id that has to be edited
    :param filename: A valid json file with the particular to-do
    :return:
    """
    if check_json_structure(edit_data):
        get_todos = load_json(filename)
        for item in get_todos:
            if updates_edit_id in item['id']:
                item['Title'] = edit_data['Title']
                item['description'] = edit_data['Description']
                item['doneStatus'] = edit_data['DoneStatus']
        update_json(get_todos)
        get_updated_todos = load_json(filename)
        return get_updated_todos
    else:
        return "JSON not in the expected format"


def get_specific_id(modified_id, filename):
    get_todo = load_json(filename)
    for item in get_todo:
        if modified_id == item['id']:
            return jsonify(item)



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

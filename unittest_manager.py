from flask import Flask
import unittest
import helper
import json
from schema import Schema, And, Use, SchemaError
from app import app

"""CONSTANTS"""
ADDING_TODO = {"Title": "Sample To-do Item", "Description": "Hello Validating", "DoneStatus": True}
ADD_TODO_SCHEMA = Schema({
    "id": And(Use(str))
})
JSON_DATA = json.dumps(ADDING_TODO)
ADD_TODO = json.loads('{"Title": "Sample To-do Item","Description": "Hello Validating","DoneStatus": true}')
EDIT_TODO = json.loads('{"Title": "Sample To-do Item","Description": "Hello Validating","DoneStatus": false}')
todo_id = ""


class MyTest(unittest.TestCase):
    def test_load_json(self):
        pass


if __name__ == '__main__':
    unittest.main()

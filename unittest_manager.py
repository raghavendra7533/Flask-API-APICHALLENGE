import unittest
import json
import os
from helper import load_json, get_todos, update_json


class TestJson(unittest.TestCase):

    def setUp(self):
        with open("data_unittest.json", "w+") as json_file:
            self.json_dict = [{
                "Title": "Sample To-do Item",
                "doneStatus": True,
                "description": "Hello Validating",
                "id": "8955a41cb7104d71a26e4e59b81925ca"
            }]
            json.dump(self.json_dict, json_file)
        with open("error_data_unittest.txt", "w+") as error_json:
            self.json_error = "Hello World"
            error_json.write(self.json_error)
        with open("data_unittest.json", "r") as comparison_file:
            self.comparison_data = json.load(comparison_file)

    def tearDown(self):
        if os.path.exists("data_unittest.json"):
            os.remove("data_unittest.json")
        if os.path.exists("error_data_unittest.txt"):
            os.remove("error_data_unittest.txt")

    def test_load_json(self):
        response = load_json("data_unittest.json")
        self.assertEqual(response, self.comparison_data)

    def test_err_load_json(self):
        error_response = load_json("error_data_unittest.txt")
        self.assertRaises(json.decoder.JSONDecodeError)

    def test_invalid_file_path_load_json(self):
        load_json("hello.json")
        self.assertRaises(FileNotFoundError)


class TestReadTodos(unittest.TestCase):

    def setUp(self):
        with open("data_unittest.json", "w+") as json_file:
            self.json_dict = [{
                "Title": "Sample To-do Item",
                "doneStatus": True,
                "description": "Hello Validating",
                "id": "8955a41cb7104d71a26e4e59b81925ca"
            }]
            json.dump(self.json_dict, json_file)
        with open("error_data_unittest.txt", "w+") as error_json:
            self.json_error = "Hello World"
            error_json.write(self.json_error)
        with open("data_unittest.json", "r") as comparison_file:
            self.comparison_data = json.load(comparison_file)

    def tearDown(self):
        if os.path.exists("data_unittest.json"):
            os.remove("data_unittest.json")
        if os.path.exists("error_data_unittest.txt"):
            os.remove("error_data_unittest.txt")

    def test_get_todos(self):
        response = get_todos("data_unittest.json")
        self.assertIsInstance(json.loads(response), list)

    def test_invalid_file_path_get_todos(self):
        response = get_todos("test.txt")
        self.assertRaises(FileNotFoundError)


class TestUpdateTodos(unittest.TestCase):

    def setUp(self):
        with open("data_unittest.json", "w+") as json_file:
            self.json_dict = [{
                "Title": "Sample To-do Item",
                "doneStatus": True,
                "description": "Hello Validating",
                "id": "8955a41cb7104d71a26e4e59b81925ca"
            }]
            json.dump(self.json_dict, json_file)
        with open("error_data_unittest.txt", "w+") as error_json:
            self.json_error = "Hello World"
            error_json.write(self.json_error)
        with open("data_unittest.json", "r") as comparison_file:
            self.comparison_data = json.load(comparison_file)

    def tearDown(self):
        if os.path.exists("data_unittest.json"):
            os.remove("data_unittest.json")
        if os.path.exists("error_data_unittest.txt"):
            os.remove("error_data_unittest.txt")

    def test_update_json(self):
        json_element = [
            {
                "Title": "Sample To-do Item",
                "doneStatus": True,
                "description": "Hello Validating",
                "id": "8955a41cb7104d71a26e4e59b81925ca"
            },
            {
                "Title": "POSTMAN API TEST",
                "doneStatus": True,
                "description": "Hello Validating",
                "id": "6f5762b7e50e4bd0bae5d4945cf00d3c"
            }]
        update_json(json_element, "data_unittest.json")
        with open("data_unittest.json", "r") as comparison_file:
            new_comparison_data = json.load(comparison_file)
        self.assertTrue(new_comparison_data != self.comparison_data)

    def test_err_update_json(self):
        error_data = {"Hello World"}
        response = update_json(error_data, "data_unittest.json")
        self.assertRaises(json.decoder.JSONDecodeError)


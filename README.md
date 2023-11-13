# A CRUD Operation Microservice using Flask

- This project is built on Flask
- This project can be used to learn how an API works

## Tech Stack
- Python 3.8
  - Flask

## Main file
### Import the relevant libraries
1. Flask
2. [[#Helper.py]]
### Define the constants
1. Filename
### App Routes
1. **Root**
	- Define a function `home` which returns a json string with the content `Welcome to Raghav's API Challenge`
2. `/todo`
	- If the request method is `GET`, get all the todos
	- If the request method is `POST`, add a todo after accepting a json object
	- If the request method is anything else, return a json string with an error `405`, `Method Not Allowed`
3. `/todo/<id>`
	- If the request method is `GET`, get that specific todo which matches that particular id
	- If the request method is `DELETE`, delete that specific todo which matches that particular id
	- If the request method is `PUT`, accept a json object and edit that particular todo which matches that particular id
	- If the request method is anything else return a json object with an error `405`

## Helper.py
### Import the relevant libraries
1. json
2. uuid
3. schema
4. flask
### Define the constants
1. FILE_NOT_FOUND
2. LOGFILE
3. FILENAME
4. JSON_FORMAT (for schema validation)
### Functions
1. `load_json`:
	This function loads the json file to return a list of the content in the file
	:param filename: A valid json file
	:return: A list of dictionaries
2. `get_todos`
	This function returns a json object with the data in the file  
	:param filename: A valid json path:return: A json object
3. `update_json`
	This function writes the data to the json file  
	:param data: A dictionary of data
	:param filename: A valid json file path:return: A str with the status
4. `add_todo`
	This function adds a to-do to the json file  
	:param json_file: A list with dictionaries of todos
	:return: A str with the status
5. `delete_json_item`
	This function deletes a json item if it is in the json file using the id  
	:param del_id: id of the to-do
	:param filename: The data.json file
	:return: the todos after deleting
6. `edit_todo_item`
	This function edits an existing to-do  
	:param edit_data: A dictionary with keys "Title", "Description", "doneStatus"  
	:param updates_edit_id: The to-do id that has to be edited  
	:param filename: A valid json file with the particular to-do  
	:return: updated to-do list
7. `get_specific_id`
	This function gets the todo with a specific id
	:param modified_id: The id of the todo to be modified
	:param filename: A valid json file with the particular todo
	:return: A json with the specific todo
8. `check_json_structure`
	This function uses validates if the format of the passed json is correct  
	:param json_file: A dictionary
	:return: A boolean
9. `create_id`
	This function creates a unique hex id  
	:return: A hex id
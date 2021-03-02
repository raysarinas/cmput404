#!/usr/bin/env python3

from flask import Flask
from flask_restful import Resource, Api
from flask_restful import reqparse, abort

app = Flask(__name__)
api = Api(app)

# @app.route("/")
# def hello(): # turn into a class
#     return "Hello, world!"


class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'} # python dict turned into json!

# add_resource - where to put the resource
api.add_resource(HelloWorld, "/")

parser = reqparse.RequestParser()
parser.add_argument("task")

TODOs = {
    1: {"task": "build an API"},
    2: {"task": "?????"},
    3: {"task": "profit"},
}


def abort_if_todo_not_found(todo_id): # user and error msg
    if todo_id not in TODOs:
        abort(404, message="TODO {} does not exist".format(todo_id))


def add_todo(todo_id):
    args = parser.parse_args()
    todo = {"task": args["task"]}
    TODOs[todo_id] = todo
    return todo


class Todo(Resource): # allow to put at particular location
    """
    Shows a single TODO item and lets you delete a TODO item.
    """

    # These methods let us use HTTP methods for the todo resource
    def get(self, todo_id):
        abort_if_todo_not_found(todo_id)
        return TODOs[todo_id]

    def delete(self, todo_id):
        abort_if_todo_not_found(todo_id)
        del TODOs[todo_id]
        return "", 204

    def put(self, todo_id):
        return add_todo(todo_id), 201


class TodoList(Resource):
    """
    Shows a list of all TODOs and lets you POST to add new tasks.
    """

    def get(self):
        return TODOs

    def post(self):
        todo_id = max(TODOs.keys()) + 1
        return add_todo(todo_id), 201


api.add_resource(Todo, "/todos/<int:todo_id>")
api.add_resource(TodoList, "/todos")

if __name__ == "__main__":
    app.run(debug=True)
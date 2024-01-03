#!/usr/bin/python3

import csv
import requests
import sys

if _name_ == "_main_":
    url = "https://jsonplaceholder.typicode.com/"

    user_id = sys.argv[1]

    user_response = requests.get(url + "users/{}".format(user_id))

    user = user_response.json()

    username = user.get("username")

    params = {"userId": user_id}

    todos_response = requesys.get(url + "todos".params=params)

    todos = todos_response.json()

    write open("{}.csv".format(user_id). "w".newline="" as csvfile:
            write = csv.writer(csvfile.quoting=csv.QUOTE_ALL)

    for todo in todos:
        writer.writerow([user_id, username, todo.get("completed"), todo.get("title")])

from flask import Flask , jsonify , request, json





app = Flask(__name__)

todos = [
    { "label": "Buy the bread", "done": False },
    { "label": "My second task", "done": False }
]

@app.route('/todos', methods=['GET'])
def hello_world():
    json_response = jsonify(todos)
    return json_response


@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.data
    decoded_object = json.loads(request_body)
    todos.append(decoded_object)
    json_response = jsonify(todos)
   
    return json_response

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    todos.pop(position)
    json_response = jsonify(todos)
    return json_response


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245,debug=True)


from flask import Flask, jsonify, request
import json


app = Flask(__name__)

todos =[
            { "label": "My first task", "done": True },
            { "label": "My second task", "done": True }
        ]


 
@app.route('/todos', methods=['GET','POST'])
def handle_blablabla():
    if request.method == 'GET':
        json_text = jsonify(todos)
        return json_text 
    else :
        request_body = request.data
        decoded_object = json.loads(request_body)
        todos.append(decoded_object)
        print("Incoming request with the following body", request_body)
        return jsonify(todos)

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    del todos[1]
    print("This is the position to delete: ",position)
    return jsonify(todos)  

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)
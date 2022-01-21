from flask import Flask, jsonify

# Init app
app = Flask(__name__)

# Defining main route
@app.route('/', methods=['GET'])
def get():
    return jsonify({"msg": "Hello!"})

# RunServer
if __name__ == '__main__':
    app.run(debug=True)
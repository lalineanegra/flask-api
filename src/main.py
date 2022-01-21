from flask import Flask, jsonify

# Init app
app = Flask(__name__)

# RunServer
if __name__ == '__main__':
    app.run(debug=True)
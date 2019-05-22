from flask import Flask
import os
app = Flask(__name__)
port = int(os.environ.get("PORT", 5000))

@app.route('/')
def hello_world():
    return 'Flask Dockerized and deployed to Heroku'

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=port)
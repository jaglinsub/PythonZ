import flask
from GetToken import *

app = flask.Flask(__name__)


@app.route('/')
def hello():
    return "Welcome to Zuora Prototype!"

@app.route('/token')
def token():
    return getToken123()

def handler(event, context):
    app.run()
    return 'Hello from AWS Lambda using Python' + sys.version + '!!'

if __name__ == '__main__':
    app.run()
    # app.run(host='0.0.0.0')
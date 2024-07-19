from flask import Flask
from flask import json
import logging
import sys

app = Flask(__name__)

handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

error_handler = logging.StreamHandler(sys.stderr)
error_handler.setLevel(logging.ERROR)
error_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
error_handler.setFormatter(error_formatter)

app.logger.addHandler(handler)
app.logger.addHandler(error_handler)
app.logger.setLevel(logging.DEBUG)

@app.route('/status')
def healthcheck():
    response = app.response_class(
            response=json.dumps({"result":"OK - healthy"}),
            status=200,
            mimetype='application/json'
    )
    app.logger.info('Status request successful')
    app.logger.debug('DEBUG message')
    return response

@app.route('/metrics')
def metrics():
    response = app.response_class(
            response=json.dumps({"status":"success","code":0,"data":{"UserCount":140,"UserCountActive":23}}),
            status=200,
            mimetype='application/json'
    )
    app.logger.info('Metrics request successful')
    return response

@app.route("/")
def hello():
    app.logger.info('Main request successful')
    return "Hello World!"

if __name__ == "__main__":
    # Run the Flask application
    app.run(host='0.0.0.0')

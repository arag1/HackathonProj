#Resources: https://auth0.com/blog/developing-restful-apis-with-python-and-flask/
#https://humeai.github.io/hume-python-sdk/0.3.3/stream/hume-stream-client/
#https://github.com/msindev/Chat-App-Flask-SocketIO
#http://curric.rithmschool.com/springboard/lectures/flask-ext-apis/

# MUST RUN http://127.0.0.1:5000/test to retrieve job id for other api endpoints (test2 and test3 to work)

import flask
import requests
import json

app = flask.Flask(__name__,template_folder='templates')

urls = ["https://iep.utm.edu/wp-content/media/hume-bust.jpg"]
models = {
"face": {}
}
@app.route("/")
def hello_world():
    # Creating homepage for a test with Hello World using index.html

    return flask.render_template("index.html")
@app.route("/test1")

def start_job():
    # Must include all headers and body data for url to work

    data = {
        "urls": [
            "https://iep.utm.edu/wp-content/media/hume-bust.jpg"
        ],
        "models": {
            "face": {}
        }
    }
    headers = {"X-Hume-Api-Key": "uRFAGAFDQfxnZGiv1MRsnHXwKcAfMb5GvCeAXADJJcrr8yHA", 'content-type': "application/json; charset=utf-8'"
               , "accept": "application/json; charset=utf-8'"}

    resp = requests.post("https://api.hume.ai/v0/batch/jobs", headers= headers,
                         data = json.dumps(data))

    test = resp.json()

    return flask.jsonify(test=test)

@app.route("/test2")
def check_job_status():
    # Must include all headers and params for url to work


    headers = {"X-Hume-Api-Key": "uRFAGAFDQfxnZGiv1MRsnHXwKcAfMb5GvCeAXADJJcrr8yHA", 'content-type': "application/json; charset=utf-8'"
               , "accept": "application/json; charset=utf-8'"}


    # Include Job ID
    resp = requests.get("https://api.hume.ai/v0/batch/jobs", headers= headers, params={"job_id": "3f027d6a-ba1d-45f4-a36b-b8e8c04f4237"})

    test = resp.json()

    return flask.jsonify(test=test)

@app.route("/test3")
def predictions():
    # Must include all headers url to work

    headers = {"X-Hume-Api-Key": "uRFAGAFDQfxnZGiv1MRsnHXwKcAfMb5GvCeAXADJJcrr8yHA", 'content-type': "application/json; charset=utf-8'"
               , "accept": "application/json; charset=utf-8'"}

    #make sure to include job id before the /predictions portion
    resp = requests.get("https://api.hume.ai/v0/batch/jobs/3f027d6a-ba1d-45f4-a36b-b8e8c04f4237/predictions", headers= headers)

    test = resp.json()

    return flask.jsonify(test=test)


app.run(debug=True)
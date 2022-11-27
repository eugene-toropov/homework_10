from flask import Flask
import utils


app = Flask(__name__)


@app.route("/")
def index():
    candidates = utils.get_all()
    result = '<br>'
    for candidate in candidates:
        result += candidate["name"] + '<br>'
        result += candidate["position"] + '<br>'
        result += candidate["skills"] + '<br>'
        result += '<br>'
    return f"<pre> {result} </pre>"


@app.route("/candidate/<int:pk>")
def get_candidate_by_pk(pk):
    candidate = utils.get_by_pk(pk)
    if not candidate:
        return "Кандидат не найден"

    url = candidate["picture"]
    result = f"<img src='{url}'>"
    result += '<br>'
    result += candidate["name"] + '<br>'
    result += candidate["position"] + '<br>'
    result += candidate["skills"] + '<br>'
    result += '<br>'
    return f"<pre> {result} </pre>"


@app.route("/skills/<skill>")
def get_candidate_by_skill(skill):
    candidates = utils.get_by_skill(skill)
    result = '<br>'
    for candidate in candidates:
        result += candidate["name"] + '<br>'
        result += candidate["position"] + '<br>'
        result += candidate["skills"] + '<br>'
        result += '<br>'
    return f"<pre> {result} </pre>"


app.run()






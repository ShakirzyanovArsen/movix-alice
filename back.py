from flask import Flask
from flask import request
from flask import make_response
from action_conf import action_config
from actions import greetings
from actions import cant_do_that

app = Flask(__name__)


def check_new_session(sess_info):
    return sess_info.get('new')


def check_no_command(payload):
    return not bool(payload.get('command'))


@app.route('/api/alice/ping/')
def ping():
    return make_response({'ping': 'pong'})


@app.route('/api/alice/', methods=['POST'])
def endpoint():
    req = request.get_json()
    metadata = req.get('meta')
    payload = req.get('request')
    session = req.get('session')
    if check_new_session(session) and check_no_command(payload):
        resp = make_response(greetings())
    else:
        resp = make_response(process_dialog(payload))
    return resp


def process_dialog(payload):
    tokens = payload.get('nlu').get('tokens')
    for item in action_config:
        if item.issubset(tokens):
            return action_config[item](payload)
    return cant_do_that()


if __name__ == '__main__':
    app.run(debug=True, port=1337)

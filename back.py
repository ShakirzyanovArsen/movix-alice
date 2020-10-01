from flask import Flask
from flask import request
from flask import make_response

app = Flask(__name__)


@app.route('/alice/', methods=['POST'])
def endpoint():
    req = request.get_json()
    metadata = req.get('meta')
    payload = req.get('request')
    session = req.get('session')
    if check_new_session(session) and not payload.get('command'):
        resp = make_response(greetings())
    else:
        resp = make_response(process_dialog(payload))
    return resp


def do_a_barrel_roll():
    return {'response': {
        'text': 'Вжух!',
        'tts': 'Вж+ух!',
        'end_session': False
    }, 'version': '1.0'}


def check_new_session(sess_info):
    return sess_info.get('new')


def greetings():
    return {'response':{
        'text': 'Привет! Пока что я ничего не умею, но могу сделать бочку!',
        'tts': 'Прив+ет! sil <[300]> Пок+а што я ничев+о не ум+ею sil <[100]> но мог+у сд+елать б+очку!',
        'end_session': False
    }, 'version':'1.0'}


def process_dialog(payload):
    if {'сделай', 'бочку'}.issubset(payload.get('nlu').get('tokens')):
        return do_a_barrel_roll()
    else:
        return cant_do_that()

def cant_do_that():
    return {'response':{
        'text': 'Извините, но я такого не умею...',
        'tts': 'Извин+ити но я так+ово не ум+ею',
        'end_session': False
    }, 'version':'1.0'}


if __name__ == '__main__':
    app.run(debug=True, port=1337)

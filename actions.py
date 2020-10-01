def text_body(func):
    def wrapper():
        text, tts = func()
        return {'response': {
            'text': text,
            'tts': tts,
            'end_session': False
        }, 'version': '1.0'}
    return wrapper


@text_body
def do_a_barrel_roll():
    text = 'Вжух!'
    tts = 'Вж+ух!'
    return text, tts


@text_body
def do_a_spin():
    text = 'Фьють!'
    tts = 'Фь+ють!'
    return text, tts

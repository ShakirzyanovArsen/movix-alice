import movix_buttons as mb


def text_body(parametrized: bool = False):
    def decorator(func):
        def wrapper(payload=None):
            if parametrized:
                text, tts = func(payload)
            else:
                text, tts = func()
            return {'response': {
                'text': text,
                'tts': tts,
                'end_session': False
            }, 'version': '1.0'}

        return wrapper

    return decorator


@text_body()
def greetings():
    text = 'Привет! Пока что я ничего не умею, но могу сделать бочку! Или штопор!'
    tts = 'Прив+ет! sil <[300]> Пок+а што я ничев+о не ум+ею sil <[100]> но мог+у сд+елать б+очку! sil <[300]> Или шт+опор!'
    return text, tts


@text_body()
def cant_do_that():
    text = 'Извините, но я такого не умею...'
    tts = 'Извин+ити но я так+ово не ум+ею'
    return text, tts


@text_body()
def do_a_barrel_roll():
    text = 'Вжух!'
    tts = 'Вж+ух!'
    return text, tts


@text_body()
def do_a_spin():
    text = 'Фьють!'
    tts = 'Фь+ють!'
    return text, tts


@text_body(True)
def volume_inc(payload):
    vol_delta = get_volume_delta(payload)
    for _ in range(vol_delta):
        mb.send_request(4)
    text = f'Увеличила громкость на {vol_delta}'
    tts = f'Увил+ичила гр+омкость на {vol_delta}'
    return text, tts


@text_body(True)
def volume_dec(payload):
    vol_delta = get_volume_delta(payload)
    for _ in range(vol_delta):
        mb.send_request(5)
    text = f'Уменьшила громкость на {vol_delta}'
    tts = f'Ум+еньшила гр+омкость на {vol_delta}'
    return text, tts


def extract_numbers(payload):
    numbers = []
    for item in payload.get('nlu').get('entities'):
        if item['type'] == 'YANDEX.NUMBER':
            numbers.append(item['value'])
    return numbers


def get_volume_delta(payload):
    num_tokens = extract_numbers(payload)
    if len(num_tokens) == 1:
        value = num_tokens[0]
    else:
        value = 1
    return value


@text_body()
def open_menu():
    mb.menu()
    text = 'Открыла меню'
    tts = 'Откр+ыла мен+ю'
    return text, tts

import movix_buttons as mb


def simple_text_body(func):
    def wrapper(payload):
        text, tts = func()
        return {'response': {
            'text': text,
            'tts': tts,
            'end_session': False
        }, 'version': '1.0'}

    return wrapper


def parametrized_text_body(func):
    def wrapper(payload):
        text, tts = func(payload)
        return {'response': {
            'text': text,
            'tts': tts,
            'end_session': False
        }, 'version': '1.0'}

    return wrapper


@simple_text_body
def do_a_barrel_roll():
    text = 'Вжух!'
    tts = 'Вж+ух!'
    return text, tts


@simple_text_body
def do_a_spin():
    text = 'Фьють!'
    tts = 'Фь+ють!'
    return text, tts


@parametrized_text_body
def volume_inc(payload):
    vol_delta = get_volume_delta(payload)
    for _ in range(vol_delta):
        mb.press_volume_plus()
    text = f'Увеличила громкость на {vol_delta}'
    tts = f'Увил+ичила гр+омкость на {vol_delta}'
    return text, tts


@parametrized_text_body
def volume_dec(payload):
    vol_delta = get_volume_delta(payload)
    for _ in range(vol_delta):
        mb.press_volume_minus()
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


@simple_text_body
def open_menu():
    mb.press_menu()
    text = 'Открыла меню'
    tts = 'Откр+ыла мен+ю'
    return text, tts

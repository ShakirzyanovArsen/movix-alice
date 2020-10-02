import logging
import toml
import requests


# TODO когда бекенд будет :^)

def volume_plus():
    pass


def volume_minus():
    pass


def menu():
    pass


log = logging.getLogger('movix_api')
log.setLevel(10)  # (format='[%(levelname)s] - %(message)s', level=10)
fh = logging.FileHandler('access.log')
log.addHandler(fh)


def send_request(button_id: int):
    # response = requests.get(url=)
    log.debug(f'Got new request; Button id: {button_id}')

import logging
import toml
import requests


log = logging.getLogger('movix_api')
log.setLevel(10)
fh = logging.FileHandler('access.log')
log.addHandler(fh)
base_url = toml.load('config.toml')['Movix']['url']


def send_request(button_id: int):
    response = requests.get(url=base_url, params={'id': button_id})
    code = response.status_code
    if code == 200:
        log.debug(f'Success! Button id: {button_id}')
    else:
        log.error(f'ERROR: {code}')
    return code

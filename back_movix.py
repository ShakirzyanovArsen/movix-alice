from flask import Flask
from flask import request
from flask import make_response
from movix_buttons import send_request

app = Flask(__name__)


@app.route('/api/movix/button', methods=['GET'])
def push_button():
    button_id = request.args.to_dict().get('id')
    send_request(button_id)
    return make_response({'status': 'ok'})


if __name__ == '__main__':
    app.run(port=1338, debug=True)

from flask import Flask

from ch.maxant.itproject.data.user import User
from ch.maxant.itproject.util import json

app = Flask(__name__,
            static_url_path='',
            static_folder='../web')

app.config.from_object(__name__)


# TODO access DB and return data
@app.route('/users/<id>', methods=['GET'])
def send_json(id):
    u = User(id, "Ant")
    return json(u)


@app.route('/')
def root():
    return app.send_static_file('index.html')
    # or could do this, if we didnt have the static folder at the start: return send_from_directory('.', path)


app.run(host='0.0.0.0', port=8080, debug=True)




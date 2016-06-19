from functools import update_wrapper
from datetime import timedelta
from flask import Flask
from flask import render_template
from flask import jsonify
from flask.ext.cors import CORS, cross_origin
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


def crossdomain(origin=None, methods=None, headers=None,
                max_age=21600, attach_to_all=True,
                automatic_options=True):
    if methods is not None:
        methods = ', '.join(sorted(x.upper() for x in methods))
    if headers is not None and not isinstance(headers, basestring):
        headers = ', '.join(x.upper() for x in headers)
    if not isinstance(origin, basestring):
        origin = ', '.join(origin)
    if isinstance(max_age, timedelta):
        max_age = max_age.total_seconds()

    def get_methods():
        if methods is not None:
            return methods

        options_resp = current_app.make_default_options_response()
        return options_resp.headers['allow']

    def decorator(f):
        def wrapped_function(*args, **kwargs):
            if automatic_options and request.method == 'OPTIONS':
                resp = current_app.make_default_options_response()
            else:
                resp = make_response(f(*args, **kwargs))
            if not attach_to_all and request.method != 'OPTIONS':
                return resp

            h = resp.headers
            h['Access-Control-Allow-Origin'] = origin
            h['Access-Control-Allow-Methods'] = get_methods()
            h['Access-Control-Max-Age'] = str(max_age)
            h['Access-Control-Allow-Credentials'] = 'true'
            h['Access-Control-Allow-Headers'] = \
                "Origin, X-Requested-With, Content-Type, Accept, Authorization"
            if headers is not None:
                h['Access-Control-Allow-Headers'] = headers
            return resp

        f.provide_automatic_options = False
        return update_wrapper(wrapped_function, f)
    return decorator

@app.route('/', methods=['POST', 'OPTIONS'])
@crossdomain(origin='*')
def index():
    # return url_for('static', filename='style.css')
    # return render_template('index.html')
    return render_template('index.html')

@app.route('/submit', methods=['GET', 'OPTIONS'])
@crossdomain(origin='*')
def distance():

  logging.getLogger('flask_cors').level = logging.DEBUG
  # response.headers.add('Access-Control-Allow-Origin', '*')
  # response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
  # response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')


  return jsonify(distance=123)

  str1 =  request.form['username'];
  str2 = request.form['password'];
  distance = get_distance(str1, str2)
  
  return json.dumps({'status':'OK','distance':distance});


# @app.after_request
# def after_request(response):
#   response.headers.add('Access-Control-Allow-Origin', '*')
#   response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
#   response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
#   return response



if __name__ == '__main__':
    app.run()




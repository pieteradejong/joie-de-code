from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/')
def index():
    # return url_for('static', filename='style.css')
    # return render_template('index.html')
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def distance():
  return 123

  str1 =  request.form['username'];
  str2 = request.form['password'];
  distance = get_distance(str1, str2)
  
  return json.dumps({'status':'OK','distance':distance});

if __name__ == '__main__':
    app.run()



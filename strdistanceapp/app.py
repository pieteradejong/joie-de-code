from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return url_for('static', filename='style.css')

@app.route('/submit', methods=['POST'])
def distance():
  return 123

if __name__ == '__main__':
    app.run()



from flask import Flask
from flask import render_template
app = Flask(__name__, static_url_path='/static')

import similarity
sim = similarity.Similarity()

@app.route('/')
def index():
    return render_template('index.html', name='pieter')

@app.route('/submit', methods=['POST'])
def distance():
  return 123

  str1 =  request.form['username']
  str2 = request.form['password']
  distance = get_distance(str1, str2)
  
  return json.dumps({'status':'OK','distance':distance})

def get_distance(str1, str2):
  # todo: convert str1,2 to binarized vectors so we can calcualte distance
  return sim.euclidian()


if __name__ == '__main__':
    app.run()




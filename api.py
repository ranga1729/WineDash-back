from flask import Flask

app = Flask(__name__)

@app.route('/time')
def test():
  return {'text':"Hello world!"}
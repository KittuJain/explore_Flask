from flask import Flask

app = Flask(__name__)

@app.route('/')
def heartbeat():
	return 'App is up and running.'

@app.route('/hello')
def hello_world():
	return 'Hello World!'



if __name__ == '__main__':
	app.run(debug=True)


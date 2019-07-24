from flask import Flask
app = Flask(__name__)

@app.route('/hello/<name>&<otro>')
def hello(name,otro):
	print name
	print otro
	return "Hello %s %s" %name

if __name__ == '__main__':
	app.run(debug=True)
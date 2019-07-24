from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
	return "Hello world in flask"

@app.route('/dos')
def dos():
	return "nuevo ingreso a dos"

@app.route('/tres')
def tres():
	val1 = 10
	val2 = 11
	
	return "nuevo ingreso a tres: " + str(val1+val2)

if __name__ == '__main__':
	app.run()
from flask import Flask
app = Flask(__name__)

@app.route('/entero/<int:valor>')
def valor(valor):
	print str(valor)
	return "Hello %d " %valor

@app.route('/flotante/<float:valor>')
def flotante(valor):
	print str(valor)
	return "Hello %f " %valor

if __name__ == '__main__':
	app.run(debug=True)
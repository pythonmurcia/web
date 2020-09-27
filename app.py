# This is the main file of the Pythun Murcia organization, it has been built 
# using the Flask python module.

# imports
from flask import Flask, render_template, url_for

# create the app object
app = Flask(__name__)

@app.route('/')
def home():
	"""
	This is the function that manages the main page of
	the web, it uses the return_template() flask function
	and the index.html template located in ./templates/
	to return the main page to the browser.
	"""
	# create the cards diccionary and pass it to the index.html template
	cards = [
		{
			'image_alt':'...',
			'title':'Python España',
			'text':'Python Murcia nace del movimiento de comunidades español Python España. Creada por unos estudiantes que buscan reunir a la mayor comunidad de programadores posible.'
		},
		{
			'image_alt':'...',
			'title':'Open Source',
			'text':'Al igual que Python en sí, esta comunidad apuesta por el código abierto, disfruta de la creación de otros programadores y haz que otros disfruten de la tuya.'
		},
		{
			'image_alt':'...',
			'title':'Branding',
			'text':'Como cualquier otra empresa o organización, nosotros también tenemos marca. Puedes ver la marca de la organización en la sección branding de nuestra página.'
		}

	]
	return render_template('index.html', cards=cards)

@app.errorhandler(404)
@app.route('/error/404')
def error404(err=None):
	e404 = {
		'number':'404',
		'title':'Página no encontrada',
		'description':'Comprueba que la dirección del enlace esté bien escrita.'
	}
	return render_template('error.html', title='404', error=e404), 404

@app.errorhandler(403)
@app.route('/error/403')
def error403(err=None):
	e403 = {
		'number':'403',
		'title':'Acceso denegado',
		'description':'No tienes permisos para acceder a está página.'
	}
	return render_template('error.html', title='403', error=e403), 403

@app.errorhandler(410)
@app.route('/error/410')
def error410(err=None):
	e410 = {
		'number':'410',
		'title':'Página no disponible',
		'description':'Está página ya no está disponible, puede que no este disponible temporalmente.'
	}
	return render_template('error.html', title='410', error=e410), 410 

@app.errorhandler(500)
@app.route('/error/500')
def error500(err=None):
	e500 = {
		'number':'500',
		'title':'Error interno',
		'description':'No te preocupes, no es culpa tuya. Estamos intentando arreglar esto.'
	}
	return render_template('error.html', title='500', error=e500), 500

if __name__ == '__main__':
	app.run(debug=True)
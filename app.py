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
	# create the cards diccionary
	cards = [
		{
			'image_route':'...',
			'image_alt':'image 1',
			'title':'card 1',
			'text':'text of card 1'
		},
		{
			'image_route':'...',
			'image_alt':'image 2',
			'title':'card 2',
			'text':'text of card 2'
		},
		{
			'image_route':'...',
			'image_alt':'image 3',
			'title':'card 3',
			'text':'text of card 3'
		}

	]
	return render_template('index.html')
if __name__ == '__main__':
	app.run(debug=True)
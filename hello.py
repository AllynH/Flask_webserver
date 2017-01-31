from flask import Flask, render_template
from flask_script import Manager
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'

manager = Manager(app)
bootstrap = Bootstrap(app)

@app.route('/')
def index():
	message = "Hello, World!"
	return render_template('index.html', message=message)

if __name__ == '__main__':
	manager.run()
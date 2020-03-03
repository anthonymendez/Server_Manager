from flask import Flask
from flask import render_template

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

# Main Page
@app.route('/')
def home_page():
    return render_template('index.html')

app.run(debug=True)
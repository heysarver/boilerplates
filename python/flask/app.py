from flask import Flask, render_template, jsonify
from api import api_blueprint
from pages import pages_blueprint

app = Flask(__name__)

app.register_blueprint(api_blueprint, url_prefix='/api')
app.register_blueprint(pages_blueprint)

if __name__ == "__main__":
    app.run(debug=True)

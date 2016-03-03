from flask import Flask, render_template
from .views.home import home

app = Flask(__name__)
app.config.from_object('config')

# Server errors

@app.errorhandler(404)
def not_found(error):
    return (render_template('404.html'), 404)

@app.errorhandler(500)
def internal_server(error):
    return (render_template('500.html'), 500)

app.register_blueprint(home)

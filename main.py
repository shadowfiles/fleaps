"""`main` is the top level module for your Flask application."""
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), 'lib'))

from app import app

# Note: We don't need to call run() since our application is embedded within
# the App Engine WSGI application server.
# app.run(host='0.0.0.0', port=8080, debug=True)

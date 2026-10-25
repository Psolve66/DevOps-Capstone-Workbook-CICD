import sys
from flask import Flask
from flask_talisman import Talisman
from flask_cors import CORS
from service.common import log_handlers

app = Flask(__name__)
app.config.from_object("config")

# Initialize Cross-Origin Resource Sharing (CORS)
CORS(app, resources={r"/accounts/*": {"origins": "*"}})

# Initialize Flask-Talisman for strict HTTP security headers
talisman = Talisman(
    app,
    content_security_policy={
        'default-src': '\'self\'',
        'object-src': '\'none\''
    },
    force_https=False
)

from service import routes, models
from service.common import error_handlers

log_handlers.init_logging(app, "gunicorn.error")
app.logger.info("Service initialized with CORS and Talisman Security Headers")

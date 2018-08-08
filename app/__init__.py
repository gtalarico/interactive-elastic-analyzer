"""
Interactive Elasticsearch Analyzer
https://github.com/gtalarico/interactive-elastic-analyzer


"""

from flask import Flask
import os
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)


# Set Env `FLASK_ENV=development` to enable Development mode.
app.config['FLASK_ENV'] = os.getenv('FLASK_ENV', 'production')

from .views import index, robots, elastic  # noqa

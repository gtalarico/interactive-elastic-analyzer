import os

from urllib.parse import urlparse, urljoin
from flask import jsonify, send_file, request
import requests

from . import app


@app.route("/")
def index():
    return send_file("templates/index.html")


@app.route("/robots.txt")
def robots():
    return send_file("robots.txt")


@app.route("/elastic", methods=["POST"])
def elastic():
    """ Elastic Search Analyze Endpoint """
    data = request.json
    text = data.get("text", "")
    tokenizer = data.get("tokenizer", "standard")
    filters = data.get("filters", [])
    tokenizer_config = data.get("tokenConfig", {})
    body = {
        "text": text,
        "tokenizer": dict(type=tokenizer, **tokenizer_config),
        "filter": filters,
        # "char_filter": ["html_strip"], TODO
    }
    resp = session.post(ANALYZER_URL, json=body)
    return jsonify(resp.json())


# Configure Session
# You can set `SEARCHBOX_URL` to your own elastic instance or use the free tier
DEFAULT_SEARCHBOX_URL = \
  'http://paas:fa037e1c0782e410fa17ca277ec47225@thorin-us-east-1.searchly.com'
URL = os.getenv('SEARCHBOX_URL', DEFAULT_SEARCHBOX_URL)
INDEX_NAME = "interactive-index"
INDEX_URL = f"{URL}/{INDEX_NAME}"
ANALYZER_URL = f"{INDEX_URL}/_analyze"
session = requests.Session()
session.headers = {"Content-Type": "application/json"}

# Ensure Index Exists
payload = {
    "settings": {"index": {"number_of_shards": 1, "number_of_replicas": 1}}
}
session.put(INDEX_URL, json=dict(body=payload))

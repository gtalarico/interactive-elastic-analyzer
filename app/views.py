import os

from flask import jsonify, send_file, request
from elasticsearch import Elasticsearch

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
    resp = es.indices.analyze(index=INDEX_NAME, body=body)
    return jsonify(resp)


# Configure Session
# You can set `SEARCHBOX_URL` to your own elastic instance or use the free tier
DEFAULT_SEARCHBOX_URL = \
  'http://paas:fa037e1c0782e410fa17ca277ec47225@thorin-us-east-1.searchly.com:80'
URL = os.getenv('SEARCHBOX_URL', DEFAULT_SEARCHBOX_URL)
INDEX_NAME = "interactive-index"
es = Elasticsearch(URL)

# Ensure Index Exists
payload = {
    "settings": {"index": {"number_of_shards": 1, "number_of_replicas": 1}}
}
# create the index, ignore 400 if index already exists
es.indices.create(index=INDEX_NAME, body=payload, ignore=400)

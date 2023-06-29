import json
from flask import Flask, request, jsonify
from elastic_client import index_name,elastic

app = Flask(__name__)


# API for searching in elastic content
@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query')
    body = {
        "query": {
            "match": {
                "text": query
            }
        }
    }
    response = elastic.search(index=index_name, body=body)
    return jsonify(response.body)


# API for tagging Elasticsearch documents
@app.route("/tag", methods=["POST"])
def tag():
    doc_id = request.json.get("doc_id")
    tags = request.json.get("tags")

    # Fetch the document from Elasticsearch
    doc = elastic.get(index=index_name, id=doc_id)

    # Update the tags field
    doc["_source"]["tags"] = tags
    
    # Update the document in Elasticsearch
    elastic.index(index=index_name, id=doc_id, body=doc["_source"])
    return "Tags added successfully."


if __name__ == "__main__":
    app.run(debug=True)
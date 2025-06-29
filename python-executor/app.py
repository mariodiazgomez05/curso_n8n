from flask import Flask, request, jsonify
import chromadb

app = Flask(__name__)

client = chromadb.HttpClient(host="chroma-server", port=8000)

@app.route("/run", methods=["POST"])
def run():
    data = request.json
    op = data.get("operation")

    if op == "add_document":
        collection_name = data["collection_name"]
        docs = data["documents"]
        ids = data["ids"]

        collection = client.get_or_create_collection(name=collection_name)
        collection.add(documents=docs, ids=ids)

        return jsonify({"status": "added", "collection": collection_name})

    return jsonify({"error": "Invalid operation"}), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)


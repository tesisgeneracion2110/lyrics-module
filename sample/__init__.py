import os
from sample.lstm.main_generator import init_generator
from flask import Flask, jsonify, send_from_directory

UPLOAD_DIRECTORY = "lstm/result/"
if not os.path.exists(UPLOAD_DIRECTORY):
    os.makedirs(UPLOAD_DIRECTORY)
api = Flask(__name__)


@api.route("/lyric")
def generate_lyric():
    filename = init_generator()
    response = [filename, "test"]
    return jsonify(response)


@api.route("/lyric/file/<path:path>")
def get_file(path):
    """Download a file."""
    return send_from_directory(UPLOAD_DIRECTORY, path, as_attachment=True)


@api.route("/lyric/file/all")
def list_files():
    """Endpoint to list files on the server."""
    files = []
    for filename in os.listdir(UPLOAD_DIRECTORY):
        path = os.path.join(UPLOAD_DIRECTORY, filename)
        if os.path.isfile(path):
            files.append(filename)
    return jsonify(files)


if __name__ == "__main__":
    api.run(debug=True)



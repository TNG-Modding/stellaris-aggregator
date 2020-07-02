from __future__ import print_function
import time
from flask import Flask, request, jsonify
from flask_cors import CORS
from lib import *
from pprint import pprint

app = Flask(__name__)
CORS(app)

@app.route("/parse", methods=['POST'])
def parse():
    """Parse a file"""
    pprint(request.json["directorypath"])
    directorypath = request.json["directorypath"]
    parsedFile = LoadStellarisFile(directorypath)
    return jsonify(parsedFile)

@app.route("/files", methods=['POST'])
def files():
    """Print the event filenames."""
    pprint(request.json["directorypath"])
    directorypath = request.json["directorypath"]
    filepaths = GetFilenamesInFolder(directorypath)
    return jsonify({"filepaths":filepaths})

@app.route("/conversations/<path:directorypath>", methods=['POST'])
def conversations(directorypath):
    conversations = ReadConversationsInFolder(directorypath)
    print(conversations)
    return conversations

@app.route("/localization/<path:localizationpath>", methods=['POST'])
def localization(localizationpath):
    """Load the localization contents."""
    localizations = GetLocalizationContentsInFolder(localizationpath)
    print(localizations)
    return localizations

if __name__ == "__main__":
    print('Server starting 127.0.0.1:5000')
    app.run(host='127.0.0.1', port=5000, debug=True)
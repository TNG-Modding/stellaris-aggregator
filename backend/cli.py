import click
import time
from flask import Flask
from flask_cors import CORS
from .lib import *
from pprint import pprint

@click.group()
def cli():
    """stellarisfiles CLI"""
    pass

@cli.command()
def server():
    app = Flask(__name__)
    CORS(app)
    print('Server starting 127.0.0.1:5000')
    app.run(host='127.0.0.1', port=5000)

@app.route("/parse/<eventFilepath>")
def hello(eventFilepath):
    print(eventFilepath)
    return "Hello"

@cli.command()
def events():
    """Print the event filenames."""
    print(fileloader.GetFilenamesInFolder("/Volumes/Storage/stellaris-defines/events/"))

@cli.command()
def conversations():
    pprint(fileloader.ReadConversationsInFolder("../galactic-conversation/conversations/"))

@cli.command()
def localization():
    """Load the localization contents."""
    fileloader.GetLocalizationContentsInFolder("/Volumes/Storage/stellaris-defines/localisation/english/")

@cli.command()
@click.option('--input', prompt='Input file', default="/Volumes/Storage/stellaris-defines/events/simplerTest.txt", help='The path of where the templated service will go.')
def parse(input):
    pprint(fileloader.LoadStellarisFile(input))

if __name__ == '__main__':
    cli()
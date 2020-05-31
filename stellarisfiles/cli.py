import click
from .lib import kinter as kinter
from .lib import fileloader as fileloader
from pprint import pprint

@click.group()
def cli():
    """stellarisfiles CLI"""
    pass

@cli.command()
def load():
    """Load UI."""
    files = fileloader.GetFilenamesInFolder("./events/")
    localisations = fileloader.GetLocalizationContentsInFolder("./localisation/english/")
    kinter.createWindow(files, localisations)

@cli.command()
def events():
    """Print the event filenames."""
    print(fileloader.GetFilenamesInFolder("./events/"))

@cli.command()
def localisation():
    """Load the localisation contents."""
    fileloader.GetLocalizationContentsInFolder("./localisation/english/")

@cli.command()
@click.option('--input', prompt='Input file', default="./events/advisor_events.txt", help='The path of where the templated service will go.')
def parse(input):
    fileloader.LoadStellarisFile(input)

if __name__ == '__main__':
    cli()
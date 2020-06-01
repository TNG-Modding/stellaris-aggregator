import click
from .lib import kinter as kinter
from .lib import fileloader as fileloader
from pprint import pprint

@click.group()
def cli():
    """stellarisfiles CLI"""
    pass

@cli.command()
@click.option('--localisation/--no-localisation', default=True, prompt='Include localisation', help='Whether to load localisation files.')
def load(localisation):
    """Load UI."""
    files = fileloader.GetFilenamesInFolder("./events/")
    localisations = fileloader.GetLocalizationContentsInFolder("./localisation/english/") if localisation else {}
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
@click.option('--input', prompt='Input file', default="./events/simplerTest.txt", help='The path of where the templated service will go.')
def parse(input):
    pprint(fileloader.LoadStellarisFile(input))

if __name__ == '__main__':
    cli()
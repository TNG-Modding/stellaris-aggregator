import click
from .lib import kinter as kinter
from .lib import fileloader as fileloader

@click.group()
def cli():
    """stellarisfiles CLI"""
    pass

@cli.command()
def load():
    """Load UI."""
    files = fileloader.GetFilenamesInFolder("./events/")
    kinter.createWindow(files)

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
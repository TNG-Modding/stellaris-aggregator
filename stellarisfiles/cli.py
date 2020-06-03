import click
from .lib import kinter as kinter
from .lib import fileloader as fileloader
from pprint import pprint

@click.group()
def cli():
    """stellarisfiles CLI"""
    pass

@cli.command()
@click.option('--localization/--no-localization', default=True, prompt='Include localization', help='Whether to load localization files.')
def load(localization):
    """Load UI."""
    files = fileloader.GetFilenamesInFolder("./events/")
    localizations = fileloader.GetLocalizationContentsInFolder("./localisation/english/") if localization else {}
    kinter.createWindow(files, localizations)

@cli.command()
def events():
    """Print the event filenames."""
    print(fileloader.GetFilenamesInFolder("./events/"))

@cli.command()
def localization():
    """Load the localization contents."""
    fileloader.GetLocalizationContentsInFolder("./localisation/english/")

@cli.command()
@click.option('--input', prompt='Input file', default="./events/simplerTest.txt", help='The path of where the templated service will go.')
def parse(input):
    pprint(fileloader.LoadStellarisFile(input))

if __name__ == '__main__':
    cli()
import click
from .lib import kinter as kinter
from .lib import fileloader as fileloader

@click.group()
def cli():
    """stellarisfiles CLI"""
    pass

@cli.command()
def load():
    """Load the files here."""
    files = fileloader.GetFilesInCurrentFolder()
    kinter.createWindow(files)

@cli.command()
def files():
    """Load the files here."""
    print(fileloader.GetFilesInCurrentFolder())

if __name__ == '__main__':
    cli()
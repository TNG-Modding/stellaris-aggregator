import click
from .lib import kinter as operations

@click.group()
def cli():
    """stellarisfiles CLI"""
    pass

@cli.command()
def load():
    """Load the files here."""
    print("Loading files...\n")
    operations.createWindow()

if __name__ == '__main__':
    cli()
# fitness_tracker/tracker.py

import click

@click.command()
def main():
    click.echo("Welcome to Fitness Tracker CLI!")

if __name__ == "__main__":
    main()

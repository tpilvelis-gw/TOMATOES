import click
import jira

ME_AS_JIRA_TICKET = "PERSON-13"

@click.group()
def cli():
    pass

@click.command()
@click.argument('name')
def task(name):
    click.echo('creating jira issue...')
    click.echo(f"Title: {name}")


@click.command()
def dropdb():
    click.echo('Dropped the database')

cli.add_command(task)
cli.add_command(dropdb)

if __name__ == '__main__':
    cli()

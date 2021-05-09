from saygeek import SayGeek
import typer

app = typer.Typer(add_completion=False)

@app.callback()
def callback():
    """
    Classic ALMA saygeek application, ported to Python.
    It returns random funny geek or historical ALMA quotes.

    Usage:

    saygeek phrase AOG

    saygeek phrase ALMA

    saygeek phrase GOLDEN-JIRA

    saygeek keys
    """

@app.command()
def phrase(key: str = typer.Argument(None)):
    sg = SayGeek()
    data = sg.random_phrase(key)
    header = '[{}]:\n'.format(data['prefix']) if data['prefix'] else ''
    print('{}{}'.format(header, data['phrase']))

@app.command()
def keys():
    sg = SayGeek()
    print('\n'.join(sorted(sg.keys)))

def main():
    app()
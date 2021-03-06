'''
This class is a Python port of classic ALMA saygeek application, originally written in bash.
Original version was written by several ALMA geeks.
Python version by JLO.

During porting, chance was taken to remove hard-coded "phrases", saving them in the database
instead. Other very minor creative liberties were also taken, like aligning language in prefix
and phrases, where applicable.

Requirements for command-line usage:
pip install typer

'''

import re
import os
import random

PATH_DB = os.path.join(os.path.dirname(__file__), 'resources', 'saygeek.db')

class SayGeek(object):
    """Port of ADC's saygeek, originally a bash script"""

    PREFIXES = {
        'ALMA': 'Se dijo en ALMA alguna vez',
        'AOG': 'Se dijo en el Control Room alguna vez',
        'GOLDEN-SVN': 'Funny SVN logs',
        'BAD-TRANSLATION': 'Anglicismos directos',
        'BAD-SPANISH': 'Español mal usado',
        'GOLDEN-JIRA': 'Notable tickets'
    }

    def __init__(self, path_to_db=PATH_DB):
        super(SayGeek, self).__init__()

        with open(path_to_db, encoding='utf-8') as f:
            lines = f.readlines()

        self.phrases = {}
        self.keys = []
        for line in lines:
            # Skip comments
            if line.startswith('#'):
                continue

            # Match pattern _KEY_. E.g., _ALMA_, _AOG_, _HUMOUR_, etc
            _key = re.findall(r'_([^_]*)_', line)
            if not _key:
                continue
            key = _key[0]
            # If key is new, create a new key-phrases list
            if key not in self.keys:
                self.keys.append(key)
                self.phrases[key] = []

            # Append phrase to corresponding list
            self.phrases[key].append(line.strip(f'_{key}_').strip())

    def random_phrase(self, key=None):
        '''Return random phrase from key list'''

        random.seed(os.urandom(10))

        # If no key is given, choose randomly from all found in database
        if key is None:
            _key = random.choice(self.keys)
        else:
            _key = key

        if _key not in self.keys:
            return {
                'key': _key,
                'phrase': 'Error: key {} not found in database'.format(_key),
                'prefix': None
            }

        return {
            'key': _key,
            'phrase': random.choice(self.phrases[_key]),
            'prefix': self.PREFIXES.get(_key)
        }

if __name__ == "__main__":
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

    app()
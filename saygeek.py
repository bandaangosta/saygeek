'''

Requirements for stand-alone usage:
pip install typer

'''
from pprint import pprint
import re
import random

class SayGeek(object):
    """Port of ADC's SayGeek, originally a bash script"""
    def __init__(self):
        super(SayGeek, self).__init__()

        with open('saygeek.db') as f:
            lines = f.readlines()

        self.phrases = {}
        self.keys = []
        for line in lines:
            # Skip comments
            if line.startswith('#'):
                continue

            # Match pattern _KEY_
            _key = re.findall(r'_([^_]*)_', line)
            if not _key:
                continue
            key = _key[0]
            if key not in self.keys:
                self.keys.append(key)
                self.phrases[key] = []

            self.phrases[key].append(line.strip(f'_{key}_').strip())

    def random_phrase(self, key=None):
        if key is None:
            _key = random.choice(self.keys)
        else:
            _key = key

        return {'key': _key, 'phrase': random.choice(self.phrases[_key])}

def main(name: str):
    typer.echo(f"Hello {name}")

if __name__ == "__main__":
    # import typer
    # typer.run(main)

    sg = SayGeek()
    # print(sg.keys)
    print(sg.random_phrase('ALMA'))
    print(sg.random_phrase('AOG'))
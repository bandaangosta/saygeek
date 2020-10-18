# saygeek

This repository implements a Python port of classic ALMA saygeek application, originally written in bash.   
It also provides a very simple command-line application to run it.

Original version was written by several ALMA geeks.
Python version by JLO.

During porting, chance was taken to remove hard-coded "phrases", saving them in the database
instead. Other very minor creative liberties were also taken, like aligning language in prefix
and phrases, where applicable.

Requirements for command-line usage:   
    
    pip install typer

# saygeek

This repository implements a Python port of classic ALMA saygeek application, originally written in bash.
It provides a very simple command-line application to run it.

Original version was written by several ALMA geeks.
Python version by JLO.

During porting, chance was taken to remove hard-coded "phrases", saving them in the database
instead. Other very minor creative liberties were also taken, like aligning language in prefix
and phrases, where applicable.

### Installation:

    pip install saygeek

### Usage:

    $ saygeek phrase AOG
    [Se dijo en el Control Room alguna vez]:
    Déjate de pegarme en las patas Emiliano

    $ saygeek phrase ALMA
    [Se dijo en ALMA alguna vez]:
    Mi problema son las tentaciones como Avarias y Guagüito...

    $ saygeek phrase GOLDEN-JIRA
    [Notable tickets]:
    ICT-5433 "... like the TPP is hemorrhaging memory ..."

    $ saygeek keys
    ALMA
    AOG
    BAD-CONCEPTS
    BAD-SPANISH
    BAD-TRANSLATION
    BYE
    CONFIRM
    GOLDEN-JIRA
    GOLDEN-SVN
    HELLO
    HUMOUR
    MOVIE
    QUOTE

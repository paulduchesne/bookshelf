import isbn_hyphenate
import pandas
import pathlib
import pydash
import requests
import time

with open(pathlib.Path.cwd() / 'bookshelf.md') as data:

    data = data.read().split('\n')
    data = [x for x in data if x != '']

for x in data:
    isbn = isbn_hyphenate.hyphenate(x)
    print(isbn)

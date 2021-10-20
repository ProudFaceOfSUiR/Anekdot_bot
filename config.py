import json
import random
from balaboba import balaboba

token = '1772160965:AAGtuQID5PCAEIwoSG5ZueR3Hna_KjA11i8'

class Joke(object):
    '''Класс - родитель для всех шуток'''
    def __init__(self, category):
        self.category = category

    def generate(self):
        pass


class Badjoke(Joke):

    def __init__(self):
        Joke.__init__(self, 1)

    def __repr__(self):
        return repr(self.text)

    def generate(self):
        links = open('bad_jokes.json', 'r', encoding='utf-8')
        parsed_links = json.load(links)
        self.text = random.choice(parsed_links["items"])['joke']

class Peacefuljoke(Joke):

    def __init__(self):
        Joke.__init__(self, 0)

    def __repr__(self):
        return repr(self.text)

    def generate(self):
        links = open('peaceful_jokes.json', 'r', encoding='utf-8')
        parsed_links = json.load(links)
        self.text = random.choice(parsed_links["items"])['joke']


class Neuronjoke(Joke):

    def __init__(self):
        Joke.__init__(self, 0)

    def __repr__(self):
        return repr(self.text)

    def generate(self, text):
        self.text = balaboba(text).replace("\n"," ")

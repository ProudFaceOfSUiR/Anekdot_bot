import json
import random
from balaboba import balaboba

token = '1772160965:AAGtuQID5PCAEIwoSG5ZueR3Hna_KjA11i8'

class Joke(object):
    '''Класс - родитель для всех шуток'''
    def __init__(self, category):
        '''Конструктор, принимает на вход только тип шутки'''
        self.category = category

    def generate(self):
        pass


class Badjoke(Joke):
    '''Класс для чернушных шуток'''
    def __init__(self):
        Joke.__init__(self, 1)

    def __repr__(self):
        return repr(self.text)

    def generate(self):
        '''Метод, возвращающий случайную шутку из json файла'''
        links = open('bad_jokes.json', 'r', encoding='utf-8')
        parsed_links = json.load(links)
        self.text = random.choice(parsed_links["items"])['joke']

class Peacefuljoke(Joke):
    '''Класс для добрых анекдотов'''
    def __init__(self):
        Joke.__init__(self, 0)

    def __repr__(self):
        return repr(self.text)

    def generate(self):
        '''Метод, возвращающий случайную шутку из json файла'''
        links = open('peaceful_jokes.json', 'r', encoding='utf-8')
        parsed_links = json.load(links)
        self.text = random.choice(parsed_links["items"])['joke']


class Neuronjoke(Joke):
    '''Класс для продолжений от балабобы'''
    def __init__(self):
        Joke.__init__(self, 0)

    def __repr__(self):
        return repr(self.text)

    def generate(self, text):
        '''Метод, генерирующий ответ от балаболы
        @:param text пользователь вводит то, что должна продолжить нейросеть'''
        self.text = balaboba(text).replace("\n"," ")

import re
from unidecode import unidecode

# BASED ON *
# https://pt.stackoverflow.com/questions/217042/como-remover-palavras-indesejadas-de-um-texto


class Cleaner():
    blacklist = ['Mr.', 'Mrs.', 'Ms.', 'Miss', 'Dr.', 'Jr.', 'Sr.', 'I', 'II', 'III', 'IV', 'V', 'MD', 'DDS', 'PhD', 'DVM', 'DM']

    @classmethod
    def __blacklist_cleaning(cls, string):
        word_list = string.split(' ')
        result = [word for word in word_list if word not in cls.blacklist]
        new_string = ' '.join(result)
        return new_string

    @staticmethod
    def __strip_cleaning(value):
        return value.strip()

    @staticmethod
    def __characters_cleaning(cpf):
        return re.sub('[^0-9]', '', cpf)

    @staticmethod
    def __case_cleaning(string):
        return string.upper()

    @staticmethod
    def __accents_cleaning(string):
        return unidecode(string)

    @classmethod
    def name_cleaning(cls, string):
        blacklisted = cls.__blacklist_cleaning(string)
        striped = cls.__strip_cleaning(blacklisted)
        unaccented = cls.__accents_cleaning(striped)
        lowered = cls.__case_cleaning(unaccented)
        return lowered

    @classmethod
    def score_cleaning(cls, number):
        striped = cls.__strip_cleaning(number)
        floated = float(striped)
        return floated

    @classmethod
    def cpf_cleaning(cls, cpf):
        uncharactered = cls.__characters_cleaning(cpf)
        striped = cls.__strip_cleaning(uncharactered)
        return striped

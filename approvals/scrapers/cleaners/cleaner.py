import re
from unidecode import unidecode


class Cleaner():
    blacklist = ['Mr.', 'Mrs.', 'Ms.', 'Miss', 'Dr.', 'Jr.', 'Sr.', 'I', 'II', 'III', 'IV', 'V', 'MD', 'DDS', 'PhD', 'DVM', 'DM']

    @classmethod
    def __blacklist_cleaning(self, string):
        word_list = string.split(' ')
        result = [word for word in word_list if word not in self.blacklist]
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
    def name_cleaning(self, string):
        blacklisted = self.__blacklist_cleaning(string)
        striped = self.__strip_cleaning(blacklisted)
        unaccented = self.__accents_cleaning(striped)
        lowered = self.__case_cleaning(unaccented)
        return lowered

    @classmethod
    def score_cleaning(self, number):
        striped = self.__strip_cleaning(number)
        floated = float(striped)
        return floated

    @classmethod
    def cpf_cleaning(self, cpf):
        uncharactered = self.__characters_cleaning(cpf)
        striped = self.__strip_cleaning(uncharactered)
        return striped

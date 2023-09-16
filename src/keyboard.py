from src.item import Item


class MixinLog:

    def __init__(self, language):
        self.__language = 'EN'

    @property
    def language(self):
        return self.__language

    def change_lang(self):
        if self.__language == 'EN':
            self.__language = 'RU'
            return self.__language
        else:
            self.__language = 'EN'
            return self.__language


class Keyboard(MixinLog, Item):
    def __init__(self, name, price, quantity, language='EN'):
        MixinLog.__init__(self, language)
        Item.__init__(self, name, price, quantity)

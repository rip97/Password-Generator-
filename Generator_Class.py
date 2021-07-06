# Description: Class file that contains the working functions of
# the password generator. Imports random class and imports the
# search_algorithms.py file
'''Please Enter values into the lists in the dictionary before running code'''

import random
import Search_Algorithms


class PasswordGenerator(object):
    # Global class vars
    __CATEGORIES = {
        'colors': [],
        'shapes': [],
        'animals': [],
        'food': [],
        'places': []
    }
    __KEYS = list(__CATEGORIES.keys())

    def __init__(self, category1='', category2='', category3=''):
        self.__category1 = category1
        self.__category2 = category2
        self.__category3 = category3

    def SetCategories(self, categories):
        self.__category1 = categories[0]
        self.__category2 = categories[1]
        self.__category3 = categories[2]

    def GetCategories(self):
        return self.__category1, self.__category2, self.__category3
    categories = property(GetCategories, SetCategories)

    def GetKeys(self):
        return self.__KEYS

    # make changes to validate repeated words

    def validateInput(self):
        # this function will validate the users input to make sure it matches
        # with the dictionary keys, will return a bool

        usersPicks = [self.__category1, self.__category2, self.__category3]
        boolList = []  # all 3 user picks need to be true in order to move on
        for pick in usersPicks:
            valid_key = Search_Algorithms.linearSearch(self.__KEYS, pick)
            boolList.append(valid_key)

        decision = 'True'
        for bools in boolList:
            if bools != True:
                decision = 'False'

        if usersPicks[0] == usersPicks[1] or usersPicks[1] == usersPicks[2] or usersPicks[0] == usersPicks[2]:
            decision = 'False'

        if decision == 'True':
            return True
        else:
            return False

    def generatePasswd(self):
        usersChoice = (self.__category1, self.__category2, self.__category3)
        passWd = ''
        randWords = []
        for index in usersChoice:
            randWords.append(self.__CATEGORIES[index][random.randint(0, (len(self.__CATEGORIES[index]) - 1))])

        for i in range(0, 3):
            randWords.append(str(random.randint(0, 9)))

        passWd = passWd.join(randWords).capitalize()
        return passWd

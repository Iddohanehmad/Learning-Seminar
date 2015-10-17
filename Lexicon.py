from Word import *
from Character import Character
import random

class Lexicon:
    def __init__(self, inv, exc):
        assert (isinstance(inv, str) or all(isinstance(member, UR) for member in inv))
        assert (isinstance(exc, str) or all(isinstance(member, UR) for member in exc))
        if isinstance(inv, str):
            self.inventory = Inventory(inv)
        else:
            self.inventory = inv
        if isinstance(inv, str):
            self.exceptions = Exceptions(exc)
        else:
            self.exceptions = exc

    def __repr__(self):
        return self.inventory.__repr__() + Character(Character.COMP_SEP).__repr__() + self.exceptions.__repr__()

    def __str__(self):
        return str(self.inventory) + str(self.exceptions) + str(Character(Character.COMP_SEP))

    def replace(self):  # moves a member from the inventory to the exception list or vice versa
        if random.random() < 0.5:
            if self.inventory.lex:
                self.exceptions.append(self.invetory.pop())
        else:
            if self.exceptions.lex:
                self.inventory.append(self.lex.pop())

class WordList(object):
    def __init__(self, lex):
        assert (isinstance(lex, str) or all(isinstance(member, Word) for member in lex))
        if isinstance(lex, str):
            self.lst = [Word(w) for w in lex.split("#")]
        else:
            self.lst = lex

    def __repr__(self):
        return Character(Character.WORD_SEP).__repr__().join(w.__repr__() for w in self.lst)

    def __str__(self):
        return str(Character.WORD_SEP).join(str(w) for w in self.lst)

    def __len__(self):
        return sum(len(w) + 1 for w in self.lst) - 1

    def append(self, w):
        assert (isinstance(w, Word))
        self.lst.append(w)

    def pop(self):  # pops a random word
        if len(self.lst) < 1:
            return
        i = random.randint(0, len(self.lst) - 1)
        tmp = self.lst[i]
        del (self.lst[i])
        return tmp

class Inventory(WordList):
    def __init__(self, exc):
        super(Inventory, self).__init__(exc)

class Exceptions(WordList):
    def __init__(self, exc):
        super(Exceptions, self).__init__(exc)




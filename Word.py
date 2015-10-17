from Character import Character
from Foot import Foot


class Word:
    def __init__(self, w):
        assert (isinstance(w, str) or all(isinstance(member, Character) for member in w))
        if isinstance(w, str):
            self.w = [Character(c) for c in w]
        else:
            self.w = w

    def __repr__(self):
        return "".join(c.__repr__() for c in self.w)

    def __str__(self):
        return "".join(str(c) for c in self.w)

    def __len__(self):
        return sum(len(c) for c in self.w)

    def __eq__(self, other):
        if isinstance(other, Word):
            return self.w == other.w
        if isinstance(other, str):
            return self.w == [c for c in other]
        return False


class SR(Word):  # surface representation

    def __init__(self, w, feet=None):
        assert (feet is None or all(isinstance(f, Foot) for f in feet))
        super(SR, self).__init__(w)
        self.feet = feet

    def __repr__(self):
        res = [c.__repr__() for c in self.w]
        for i in range(len(self.feet) - 1, -1, -1):
            f = self.feet[i]
            right_side=' '+f.strength.lower()
            if f.indices[1]!=f.indices[0]:
                right_side+=f.type.lower()
            right_side+=']'
            res.insert(f.indices[1] + 1,right_side)
            res.insert(f.indices[0], '[')
        return "".join(res)

    def __str__(self):
        return "".join(str(c) for c in self.w)

    def __eq__(self, other):
        if isinstance(other, SR):
            return self.w == other.w and self.feet == other.feet
        elif isinstance(other, str):
            return self.__repr__() == str
        return False

class PR(Word):  # phonetic representation
    def __init__(self, w):
        super(SR, self).__init__(w)


class UR(Word):  # underlying representation
    def __init__(self, w):
        super(SR, self).__init__(w)

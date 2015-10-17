class Constraint:
    AFL = "0000"  # The left edge of a foot is aligned with the left edge of a word.
    AFR = "0001"  # the right edge of a foot is aligned with the right edge of a word.
    FTBIN = "0010"  # FootBINARITY  Feet are binary on the mora or syllable level.
    FTNONFIN = "0011"  # FootNonFinal- The head syllable of a foot is not final in the foot.
    IAMBIC = "0100"  # The rightmost syllable in a foot is the head syllable.
    MAINL = "0101"  # MAIN-LEFT- The leftmost foot in a word is the head-foot.
    MAINR = "0110"  # MAIN-RIGHT- The rightmost foot in a word is the head foot.
    NONFIN = "0111"  # NonFinality- The final syllable is not included in a foot.
    PARSE = "1000"  # Every syllable is included in a foot.
    WFL = "1001"  # WORD-FOOT-LEFT The left word edge is aligned with a foot.
    WFR = "1010"  # WORD-FOOT-RIGHT The right word edge is aligned with a foot.
    WSP = "1011"  # WEIGHT-TO-STRESS PRINCIPLE- heavy syllables are stresses
    FAITH = "1100"  # the input is preserved

    def __init__(self, con_type):
        assert (isinstance(con_type, str) and len(con_type) == 4)
        self.type = con_type

    def __repr__(self):
        if self.type == self.AFL:
            return "AFL"
        if self.type == self.AFR:
            return "AFR"
        if self.type == self.FTBIN:
            return "FTBIN"
        if self.type == self.FTNONFIN:
            return "FTNONFIN"
        if self.type == self.IAMBIC:
            return "IAMBIC"
        if self.type == self.MAINL:
            return "MAINL"
        if self.type == self.MAINR:
            return "MAINR"
        if self.type == self.NONFIN:
            return "NONFIN"
        if self.type == self.PARSE:
            return "PARSE"
        if self.type == self.WFL:
            return "WFL"
        if self.type == self.WFR:
            return "WFR"
        if self.type == self.WSP:
            return "WSP"
        if self.type == self.FAITH:
            return "FAITH"

    def __str__(self):
        return self.con_type

    def __len__(self):
        return len(self.con_type)


class Con:
    def __init__(self, constraints=[Constraint(Constraint.FAITH)]):
        assert (all(isinstance(member, Constraint) for member in constraints))
        self.con = constraints

    def __repr__(self):
        return "->".__repr__().join(c.__repr__() for c in self.con)

    def __str__(self):
        return "".join(str(c) for c in self.con)

    def __len__(self):
        sum(len(c for c in self.con))

    def remove(self):
        pass

    def add(self):
        pass

    def demote(self):
        pass

    def promote(self):
        pass

    def switch(self, i, j):  # switch position of i and j
        pass




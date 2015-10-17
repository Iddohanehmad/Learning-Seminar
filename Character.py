class Character:
    HEAVY = "000"
    LIGHT = "001"
    PRIMARY = "010"
    SECONDARY = "011"
    WORD_SEP = "100"
    COMP_SEP = "101"

    def __init__(self, char_type):
        assert (isinstance(char_type, str))
        if len(char_type) == 1:
            self.char_type = self.str_to_char(char_type)
        else:
            self.char_type = char_type

    def str_to_char(self, char_type):
        if char_type == "H":
            return self.HEAVY
        if char_type == "L":
            return self.LIGHT
        if char_type == "P":
            return self.PRIMARY
        if char_type == "S":
            return self.SECONDARY
        if char_type == "#":
            return self.WORD_SEP
        if char_type == "*":
            return self.COMP_SEP

    def __repr__(self):
        if self.char_type == self.HEAVY:
            return "H"
        if self.char_type == self.LIGHT:
            return "L"
        if self.char_type == self.PRIMARY:
            return "P"
        if self.char_type == self.SECONDARY:
            return "S"
        if self.char_type == self.WORD_SEP:
            return "#"
        if self.char_type == self.COMP_SEP:
            return "*"

    def __str__(self):
        return self.char_type

    def __len__(self):
        return len(self.char_type)

    def __eq__(self, other):
        if isinstance(other, Character):
            return self.char_type == other.char_type
        if isinstance(other, str):
            return self.char_type == other
        return False

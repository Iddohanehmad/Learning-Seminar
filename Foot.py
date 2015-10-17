from Character import Character

class Foot:
    IAMBIC="I"
    TROCHEE="T"
    STRONG="S"
    WEAK="W"

    def __init__(self,indices,iambic,strength):
        self.type=iambic
        self.strength=strength
        self.indices=indices




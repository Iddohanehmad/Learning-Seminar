from Grammar import Grammar
from Data import Data
from Description import Description
from Lexicon import *
from Cons import *

class System:
    def __init__(self, grammar, data):
        assert (isinstance(grammar, Grammar))
        assert (isinstance(data, Data))
        self.G = grammar
        self.D = data
        self.DG = self.get_dg()

    def get_dg(self):
        return Description(self.G, self.D)

    def eval(self):
        return len(self.G) + len(Character(Character.COMP_SEP)) + len(self.DG)

    def __repr__(self):
        self.G.__repr__() + Character(Character.COMP_SEP).__repr__() + self.DG.__repr__()

    def __str__(self):
        str(self.G) + str(Character(Character.COMP_SEP)) + str(self.DG)

    def __len__(self):
        len(self.G) + len(Character(Character.COMP_SEP)) + len(self.DG)

L=Lexicon("HLL#LLH","HPL")
C=Con([Constraint(Constraint.AFL),Constraint(Constraint.AFR),Constraint(Constraint.FAITH),Constraint(Constraint.MAINR)])
sr=SR("HLL",[Foot((0,1),Foot.IAMBIC,Foot.STRONG)])
print(sr.__repr__())
G=Grammar(L,C)
D=Data("HPLL#LLPH#HPL")
S=System(G,D)
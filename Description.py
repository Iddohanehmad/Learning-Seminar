from Grammar import Grammar
from Data import Data

class Description:
    def __init__(self, grammar, data):
        assert (isinstance(grammar, Grammar))
        assert (isinstance(data, Data))
        self.input_outputs_dic=self.get_outputs(grammar)
        self.description = self.describe(data)

    def get_outputs(self,grammar):
        return ""

    def describe(self,data):
        return ""


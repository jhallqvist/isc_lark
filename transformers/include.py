from lark import Transformer

class IncludeTransformer(Transformer):

    def start(self, items):
        return {items[0] :"include"}

    def file(self, items):
        return items[0].value
from lark import Transformer

class KeyTransformer(Transformer):

    def start(self, items):
        values = {k: v for d in items for k, v in d.items()}
        return {"keys": [values]}

    # def key(self, items):
    #     return {k: v for d in items for k, v in d.items()}

    def name(self, items):
        return {"name": items[0].value}

    def algorithm(self, items):
        return {"algorithm": items[0].value}

    def secret(self, items):
        return {"secret": items[0].value}
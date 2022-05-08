from lark import Transformer

class AmlTransformer(Transformer):

    def start(self, items):
        return items

    def ip_prefix(self, items):
        if None in items:
            items.remove(None)
        return ("".join(items))

    def ip_addr(self, items):
        if None in items:
            items.remove(None)
        return ("".join(items))

    def key(self, items):
        if None in items:
            items.remove(None)
        return ("".join(items))

    def acl(self, items):
        if None in items:
            items.remove(None)
        return ("".join(items))

    def predefined(self, items):
        if None in items:
            items.remove(None)
        return ("".join(items))

    def list(self, items):
        result = {"negated": False, "entries": []}
        negated, items = items
        if negated is not None:
            result["negated"] = True
        for item in items:
            result["entries"].append(item)
        return result

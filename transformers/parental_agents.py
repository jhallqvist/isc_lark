from lark import Transformer

class ParentalAgentsTransformer(Transformer):

    def start(self, items):
        return {"parental-agents": items}

    def clause(self, items):
        return {k: v for d in items for k, v in d.items()}

    def name(self, items):
        return {"name": items[0].value}

    def port(self, items):
        if items[0] is not None:
            return {"port": int(items[0].value)}
        return {"port": items[0]}

    def dscp(self, items):
        if items[0] is not None:
            return {"dscp": int(items[0].value)}
        return {"dscp": items[0]}

    def rsl(self, items):
        return {"entries": items}

    def element(self, items):
        return {k: v for d in items for k, v in d.items()}

    def ip_addr(self, items):
        return {"ip-address": items[0].value}

    def key_id(self, items):
        return {"key-id": items[0].value}

    def tls_id(self, items):
        return {"tls-id": items[0].value}
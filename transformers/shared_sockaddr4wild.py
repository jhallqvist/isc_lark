from lark import Transformer

class SocketAddr4WildTransformer(Transformer):

    def start(self, items):
        key, *values = items
        values_dict = {k: v for d in values for k, v in d.items()}
        return {str(key): values_dict}

    def clause_type(self, items):
        return items[0].value

    def ip_addr(self, items):
        return {"ip-address": items[0].value}

    def port(self, items):
        if items[0] is not None:
            if items[0] == '*':
                return {"port": items[0].value}
            else:
                return {"port": int(items[0].value)}
        return {"port": items[0]}

    def dscp(self, items):
        if items[0] is not None:
            return {"dscp": int(items[0].value)}
        return {"dscp": items[0]}

from lark.visitors import Transformer, merge_transformers
from .aml import AmlTransformer

class ControlsBaseTransformer(Transformer):
    
    def start(self, items):
        return {"controls": items}

    def inet(self, items):
        return {k: v for d in items for k, v in d.items()}

    def channel(self, items):
        return {"channel": items[0].value}

    def ip_addr(self, items):
        return {"ip-address": items[0].value}

    def port(self, items):
        if items[0] is not None:
            return {"port": int(items[0].value)}
        return {"port": items[0]}

    def allow(self, items):
        return {"allow": items[0]}

    def unix(self, items):
        return {k: v for d in items for k, v in d.items()}

    def path(self, items):
        return {"path": items[0].value}

    def perm(self, items):
        return {"perm": items[0].value}

    def owner(self, items):
        return {"owner": items[0].value}

    def group(self, items):
        return {"group": items[0].value}

    def keys(self, items):
        if items[0] is not None:
            return {"keys": items[0]}
        return {"keys": []}

    def read_only(self, items):
        if items[0] in ('true', '1', 'yes'):
            value = True
        elif items[0] in ('false', '0', 'no'):
            value = False
        else:
            value = None
        return {"read-only": value}


ControlsTransformer = merge_transformers(
                            ControlsBaseTransformer,
                            aml=AmlTransformer())
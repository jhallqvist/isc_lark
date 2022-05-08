from lark.visitors import Transformer, merge_transformers
from .shared_aml import AmlTransformer

class AclBaseTransformer(Transformer):

    def start(self, items):
        return {"acls": items}

    def acl(self, items):
        name, values = items
        return {"name": name, "entries": values}

    def name(self, items):
        return str(items[0])

AclTransformer = merge_transformers(
                            AclBaseTransformer,
                            shared_aml=AmlTransformer())

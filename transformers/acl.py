from lark.visitors import Transformer, merge_transformers
from .aml import AmlTransformer

class AclBaseTransformer(Transformer):

    def start(self, items):
        return {"acls": items}

    def acl(self, items):
        return {"name": items[0], "entries": items[1]}

    def name(self, items):
        return str(items[0])

# class AclComposer(Transformer):

#     def start(self, items):
#         return {"acls": items}

AclTransformer = merge_transformers(
                            AclBaseTransformer,
                            aml=AmlTransformer())

# middle_transformer = merge_transformers(
#                             AclBaseTransformer,
#                             aml=AmlTransformer())

# AclTransformer = merge_transformers(
#                             AclComposer,
#                             acl=middle_transformer())

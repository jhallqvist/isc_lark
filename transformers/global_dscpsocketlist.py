from lark.visitors import Transformer, merge_transformers
from .shared_dscpsocketlist import DscpSocketTransformer

class GlobalDscpSocketBaseTransformer(Transformer):

    def start(self, items):
        clause, *values = items
        name, *values = values
        values_dict = {k: v for d in values[0] for k, v in d.items()}
        name.update(values_dict)
        return {clause: [name]}

    def clause_type(self, items):
        return items[0].value

    def name(self, items):
        return {"name": items[0].value}

GlobalDscpSocketTransformer = merge_transformers(
                            GlobalDscpSocketBaseTransformer,
                            shared_dscpsocketlist=DscpSocketTransformer())
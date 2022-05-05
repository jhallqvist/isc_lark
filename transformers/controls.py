from lark.visitors import Transformer, merge_transformers
from .aml import AmlTransformer

class InetTransformer(Transformer):
    pass


class ControlsTransformer(Transformer):
    
    def start(self, items):
        return {"controls": items}
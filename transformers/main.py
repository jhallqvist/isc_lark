from lark.visitors import Transformer, merge_transformers
from .acl import AclTransformer
from .controls import ControlsTransformer
from .include import IncludeTransformer
from .key import KeyTransformer
from .logging import LoggingTransformer
from .options import OptionsTransformer
from .global_dscpsocketlist import GlobalDscpSocketTransformer


class Storage(Transformer):
    def start(self, children):
    #     result = {}
    #     for child in children:
    #         key, value = list(child.items())[0]
    #         if key in result.keys():
    #             result[key].extend(value)
    #         else:
    #             result[key] = value
    #     return result
        return children

main_transformer = merge_transformers(
                            Storage(),
                            acl=AclTransformer(),
                            controls=ControlsTransformer(),
                            include=IncludeTransformer(),
                            key=KeyTransformer(),
                            logging=LoggingTransformer(),
                            options=OptionsTransformer(),
                            global_dscpsocketlist=GlobalDscpSocketTransformer()
                            )
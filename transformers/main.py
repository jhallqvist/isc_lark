from lark.visitors import Transformer, merge_transformers
from transformers.acl import AclTransformer
from transformers.controls import ControlsTransformer
from transformers.include import IncludeTransformer
from transformers.key import KeyTransformer
from transformers.logging import LoggingTransformer
from transformers.dscpsocketlist import DscpSocketTransformer

class Storage(Transformer):
    def start(self, children):
        # result = {}
        # for child in children:
        #     key, value = list(child.items())[0]
        #     if key in result.keys():
        #         result[key].extend(value)
        #     else:
        #         result[key] = value
        # return result
        return children

main_transformer = merge_transformers(
                            Storage(),
                            acl=AclTransformer(),
                            controls=ControlsTransformer(),
                            include=IncludeTransformer(),
                            key=KeyTransformer(),
                            logging=LoggingTransformer(),
                            dscpsocketlist=DscpSocketTransformer()
                            )
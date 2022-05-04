from pathlib import Path
from lark import Lark
from lark.visitors import Transformer, merge_transformers
from transformers.acl import AclTransformer
from pprinter import Formatter

__dir__ = Path(__file__).parent
pprint = Formatter()

class Storage(Transformer):
    def start(self, children):
        return children

main_transformer = merge_transformers(
                            Storage(),
                            acl=AclTransformer())


text = '''
acl "test" {
    !1.1.1.0/24;
    2.2.2.2;
    none;
    {
        !2001:af:3546::1/64;
        "Test String";
    }; 
    !{
        key MyKey;
        4.4.4.4; 
    };
};
acl "test2" { 4.4.4.4; };
'''


parser = Lark.open(__dir__ / 'grammars/main.lark')

tree = parser.parse(text)

print(tree.pretty())

transformed_tree = main_transformer.transform(tree)
# transformed_tree = AclTransformer().transform(tree)

print(pprint(transformed_tree))
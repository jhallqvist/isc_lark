from pathlib import Path
from lark import Lark
from transformers.main import main_transformer
from pprinter import Formatter

__dir__ = Path(__file__).parent
pprint = Formatter()


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
controls {
    inet 1.1.1.1 port 56 allow { 1.1.1.1; } keys {"myKey";} read-only true;
    inet * allow {};
    unix "/etc/socket" 0773 10 20keys {"myKey";} read-only no;
};
acl "test3" { 4.4.4.4; };
acl "test4" { 4.4.4.4; };
include "/home/includes/file.txt";
key "secret" {
    algorithm hmac-md5;
    secret "SUperSecerte";
};
key "secret2" {
    algorithm hmac-md5;
    secret "SUperSecerte";
};
logging {
    category myCat {
        abc;
    };
    channel myChan {
        buffered true;
        file "myFile" suffix timestamp;
        null;
        print-category true;
        print-severity false;
        print-time iso8601;
        severity debug 3;
        stderr;
        syslog kern;
    };
};
parental-agents "Test" port 49153 dscp 33 {
    "MyMaster-list";
    1.1.1.1 port 798;
    2001::1 key myKey tls myTls;
};
parental-agents "Test2" port 49153 dscp 33 {
    "MyMaster-list";
    1.1.1.1 port 798;
    2001::1 key myKey tls myTls;
};
options {
    allow-new-zones 1;
    allow-notify { 1.1.1.1; };
};
'''

text = '''
options {
    allow-new-zones 1;
    allow-notify { 1.1.1.1; };
    allow-recursion { "mytestList"; };
    also-notify "Test2" port 49153 dscp 33 {
        "MyMaster-list";
        1.1.1.1 port 798;
        2001::1 key myKey tls myTls;
    };
};
'''

parser = Lark.open(__dir__ / 'grammars/main.lark')

tree = parser.parse(text)

print(tree.pretty())

transformed_tree = main_transformer.transform(tree)

print(pprint(transformed_tree))
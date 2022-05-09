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
        file "myFile" versions unlimited  size 3M suffix timestamp;
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
    alt-transfer-source * port 33 dscp 62;
    allow-transfer port 49152 transport tls { 1.1.1.1; };
    also-notify port 798 dscp 33 {
        "MyMaster-list";
        1.1.1.1 port 798;
        2001::1 key myKey tls myTls;
    };
    alt-transfer-source 1.1.1.1 port * dscp 32;
    alt-transfer-source-v6 2001::1 port 666 dscp 43;
    answer-cookie no;
    attach-cache A;
    auth-nxdomain true;
    auto-dnssec allow;
    automatic-interface-scan 0;
    avoid-v4-udp-ports { 5000; range 1024 2048; };
    avoid-v6-udp-ports { 40000; range 50000 60000; };
    bindkeys-file "myTestFile";
    blackhole { 8.8.8.8; 8.8.4.4; };
    catalog-zones { 
        zone test
        default-masters port 798 dscp 33 {
            "MyMaster-list";
            1.1.1.1 port 798;
            2001::1 key myKey tls myTls;
        }
        zone-directory "myZone"
        in-memory false
        min-update-interval 1234
        ;
    };
    cache-file "/etc/bind/secretfile.file";
    check-dup-records fail;
    check-integrity no;
    check-mx warn;
    check-mx-cname ignore;
    check-names slave;
    check-sibling true;
    check-spf ignore;
    check-srv-cname warn;
    check-wildcard false;
    clients-per-query 66;
    cookie-algorithm aes;
    cookie-secret 0123456789aBcDeF0123;
    coresize 3G;
    datasize unlimited;
    deny-answer-addresses { 8.8.8.8; } except-from { "example.net"; };
    deny-answer-aliases { "example.net"; } except-from { "example.net"; };
};
'''

parser = Lark.open(__dir__ / 'grammars/main.lark')

tree = parser.parse(text)

print(tree.pretty())

transformed_tree = main_transformer.transform(tree)

print(pprint(transformed_tree))
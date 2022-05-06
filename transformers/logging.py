from lark.visitors import Transformer, merge_transformers

class LoggingTransformer(Transformer):
    
    def start(self, items):
        return {"logging": items}

    def category(self, items):
        # return {k: v for d in items for k, v in d.items()}
        name, entries = items
        return {"category": {"name": name, "entries": entries}}

    def category_name(self, items):
        return str(items[0])

    def category_list(self, items):
        return items

    def element(self, items):
        return str(items[0])

    def channel(self, items):
        return {"channel": {k: v for d in items for k, v in d.items()}}

    def channel_name(self, items):
        return {"name": str(items[0])}

    def buffered(self, items):
        return {"buffered": str(items[0])}

    def file(self, items):
        return {"file": {k: v for d in items for k, v in d.items()}}

    def file_name(self, items):
        return {"name": str(items[0])}

    def file_versions(self, items):
        return {"versions": str(items[0])}

    def file_size(self, items):
        return {"size": str(items[0])}

    def file_suffix(self, items):
        return {"suffix": str(items[0])}

    def null(self, items):
        return {"null": True}

    def print_category(self, items):
        return {"print-category": str(items[0])}

    def print_severity(self, items):
        return {"print-severity": str(items[0])}

    def print_time(self, items):
        return {"print-time": str(items[0])}

    def severity(self, items):
        return {"severity": str(items[0])}

    def stderr(self, items):
        return {"stderr": True}

    def syslog(self, items):
        return {"syslog": str(items[0])}
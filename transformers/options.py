from lark.visitors import Transformer, merge_transformers
from .shared_aml import AmlTransformer
from .shared_sockaddr4wild import SocketAddr4WildTransformer
from .shared_sockaddr6wild import SocketAddr6WildTransformer
from .shared_dscpsocketlist import DscpSocketTransformer

class OptionsBaseTransformer(Transformer):

    def start(self, items):
        return {"options": items}

    def key_bool(self, items):
        key, value = items
        if value in ('yes', '1', 'true'):
            value = True
        elif value in ('no', '0', 'false'):
            value = False
        else:
            value = None
        return {str(key): bool(value)}

    def key_str(self, items):
        key, value = items
        return {str(key): str(value)}

    def key_quoted_str(self, items):
        key, value = items
        return {str(key): str(value)}

    def auto_dnssec (self, items):
        return {"auto-dnssec": str(items[0])}

    def key_aml(self, items):
        key, values = items
        return {str(key): values}

    def allow_transfer(self, items):
        attrs = {k: v for d in items if isinstance(d, dict) for k, v in d.items()}
        entries = items[-1]
        attrs.update({"entries": entries})
        return {"allow-transfer": attrs}

    def port(self, items):
        if items[0] is not None:
            return {"start": int(items[0].value), "end": int(items[0].value)}
        return {"port": items[0]}

    def port_tuple(self, items):
        if items[0] is not None:
            return {"port": int(items[0].value)}
        return {"port": items[0]}

    def transport(self, items):
        return {"transport": items[0].value}

    def also_notify(self, items):
        values_dict = {k: v for d in items[0] for k, v in d.items()}
        return {"also-notifty": values_dict}

    def socketaddr4wild(self, items):
        return items[0]

    def socketaddr6wild(self, items):
        return items[0]

    def port_stmts(self, items):
        name, *values = items
        return {str(name): values}

    def portrange(self, items):
        start, end = items
        return {"start": int(start), "end": int(end)}

    def catalog_zones(self, items):
        return {"catalog-zones": items}

    def catalog_zone(self, items):
        values_dict = {k: v for d in items for k, v in d.items()}
        return values_dict

    def zone(self, items):
        return {"zone": str(items[0])}

    def default_rsl(self, items):
        name, *values = items
        values_dict = {k: v for d in values[0] for k, v in d.items()}
        return {str(name): values_dict}

    def zone_directory(self, items):
        return {"zone-directory": str(items[0])}

    def in_memory(self, items):
        return {"in-memory": str(items[0])}

    def min_update_interval(self, items):
        return {"min-update-interval": str(items[0])}


OptionsTransformer = merge_transformers(
                            OptionsBaseTransformer,
                            shared_aml=AmlTransformer(),
                            shared_sockaddr4wild=SocketAddr4WildTransformer(),
                            shared_sockaddr6wild=SocketAddr6WildTransformer(),
                            shared_dscpsocketlist=DscpSocketTransformer())
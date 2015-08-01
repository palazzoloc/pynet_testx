import json
import yaml
from ciscoconfparse import CiscoConfParse

parse_file = CiscoConfParse("kirks_config.conf")
interface_objs = parse_file.find_objects("^crypto map CRYPTO")
for obj in interface_objs:
    print obj.parent
    print obj.children

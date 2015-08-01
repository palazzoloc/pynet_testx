import yaml
import json
from pprint import pprint as pp
my_list = []
my_list.append('=====================================')
my_list.append('This is a file for storing IP address')
my_list.append('=====================================')
my_list.append({})
my_list[-1]['IP ADDRESS A'] = '10.0.0.0'
my_list[-1]['IP ADDRESS B'] = '172.16.0.0'
my_list[-1]['IP ADDRESS C'] = '192.168.0.0'
my_list[-1]['SUBNET MASK A'] = '255.0.0.0'
my_list[-1]['SUBNET MASK B'] = '255.255.0.0'
my_list[-1]['SUBNET MASK C'] = '255.255.255.0'
my_list.append('=====================================')
#print my_list
print yaml.dump(my_list, default_flow_style=False)
with open("ip_address.yml", "w") as f:
    f.write(yaml.dump(my_list, default_flow_style=False))

with open("ip_address.json", "w") as f:
    json.dump(my_list, f)
with open("ip_address.json") as f:
    new_list = json.load(f)
pp(new_list)


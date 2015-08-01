
'''
 This script reads in a file named 'kirks_config.conf' and looks \
 for any crypto maps with PFS group 2 and then searches for all \
 crypto maps that do NOT use AES-SHA.

 All rights reserved.
 Author: Chris Palazzolo
 date: 8/1/2015
 For Python classwork.
'''

import json
import yaml
from ciscoconfparse import CiscoConfParse

def find_PFS():
    cisco_cfg = CiscoConfParse("kirks_config.conf")
    #interface_objs = parse_file.find_objects("^crypto map CRYPTO")
    #print interface_objs
    #for obj in interface_objs:
    #    print obj.parent
    #    print obj.children
    
    # Find all crypto maps that use PFS group 2
    print "\nHere are all the crypto maps that use PFS group 2a:"
    print #
    for i in cisco_cfg.find_objects(r'^crypto map CRYPTO'):
        matches_PFS_Group = i.has_child_with(r' set pfs group2')
        if matches_PFS_Group:
            print i.text
            print i.all_children    

    print "\nHere are all the crypto maps that do NOT use AES-SHA:"
    print #
    # Find all crypto maps that do not use AES in the transform set
    for x in cisco_cfg.find_objects(r'^crypto map CRYPTO'):
        matches_AES = x.has_child_with(r' AES-SHA')
        if not matches_AES:
            print x.text
            print x.all_children





find_PFS()

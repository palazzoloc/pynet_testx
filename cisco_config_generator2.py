from ciscoconfparse import CiscoConfParse

def standardize_interfaces(parse):
    
    ## This script searches all interfaces and modifies them to add storm control and adds timestamps to logging commands

    for intf in parse.find_objects(r'^interface.+?thernet'):
        
        has_stormcontrol = intf.has_child_with(r' storm-control broadcast')
        is_switchport_access = intf.has_child_with(r'switchport mode access')
        is_switchport_trunk = intf.has_child_with(r'switchport mode trunk')

        ## Add missing commands
        if is_switchport_access and (not has_stormcontrol):
            intf.append_to_family(' storm-control action trap')
            intf.append_to_family(' storm-control broadcast level 0.4 0.3')

        ## remove dot1q trunk misconfiguration
        elif is_switchport_trunk:
            intf.delete_children_matching('port-security')

## Parse the config
parse = CiscoConfParse('switch.conf')

## Add a new switchport at the bottom of the config...
parse.append_line('interface GigabitEthernet1/0')
parse.append_line(' switchport')
parse.append_line(' switchport mode access')
parse.append_line('!')
parse.commit ()

## Search and standardize the interfaces
standardize_interfaces(parse)
parse.commit()

## Add a line to the top of the config if not already there.
if not parse.has_line_with(r'^service\stimestamp'):
    parse.prepend_line('service timestamps debug datetime msec localtime show-timezone')
    parse.prepend_line('service timestamps log datetime msec localtime show-timezone')

## Wrtite the config file now...
parse.save_as('switch.conf.new')

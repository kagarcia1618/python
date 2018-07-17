#!/usr/bin/env python

from datetime import datetime
from collections import OrderedDict
from netmiko import ConnectHandler
from netmiko import NetMikoAuthenticationException
from netmiko import NetMikoTimeoutException
from collections import namedtuple

def extract(a):
    """
    a - exact filename of the data to be extracted
    """
    with open(a,'r') as i:
        return(i.read())

def ssh_login(a, b, c, d):
    '''
    a - filtered device detail in netmiko format
    b - filtered device detail with hostname
    c - filtered device command line
    d - file format of the log file
    '''
    timestamp = datetime.now().strftime("%d%b%Y")
    for i in range(len(a)):
        try:
            net_connect = ConnectHandler(**a[i])
            wr_file = open( 'logs/' + b[i][0] + '_' + b[i][1] + '_' + timestamp + '.' + d, 'w' )
            for j in c:
                output = net_connect.send_command(j)
                wr_file.write( j + '\n' + output + '\n')
                print('[' + b[i][0] + '] ' + j + '\n' + output + '\n')
            wr_file.close()
        except (NetMikoAuthenticationException, NetMikoTimeoutException) as z:
            wr_file = open( 'logs/' + b[i][0] + '_' + b[i][1] + '_' + timestamp + '.' + d, 'w' )
            wr_file.write(str(z))
            print(z)
            wr_file.close()
    return

def cisco_ios(a, b, c):
    '''
    a - all devices parameter detail in netmiko format
    b - all devices parameter detail with hostname
    c - all devices command lines
    '''
    params_filter = [ a[i] for i in a if a[i]['device_type'] == 'cisco_ios' ]
    node_filter = [ b[i] for i in range(len(b)) if b[i].device_type == 'cisco_ios' ]
    cfg_filter = [ c[i][2] for i in range(len(c)) if c[i][0] == 'cisco_ios' and c[i][1] == 'cfg']
    log_filter = [ c[i][2] for i in range(len(c)) if c[i][0] == 'cisco_ios' and c[i][1] == 'log']
    
    ssh_login(params_filter,node_filter,cfg_filter,'cfg')
    ssh_login(params_filter,node_filter,log_filter,'log')
    
    return

def cisco_xe(a, b, c):
    '''
    a - all devices parameter detail in netmiko format
    b - all devices parameter detail with hostname
    c - all devices command lines
    '''
    params_filter = [ a[i] for i in a if a[i]['device_type'] == 'cisco_xe' ]
    node_filter = [ b[i] for i in range(len(b)) if b[i].device_type == 'cisco_xe' ]
    cfg_filter = [ c[i][2] for i in range(len(c)) if c[i][0] == 'cisco_xe' and c[i][1] == 'cfg']
    log_filter = [ c[i][2] for i in range(len(c)) if c[i][0] == 'cisco_xe' and c[i][1] == 'log']
    
    ssh_login(params_filter,node_filter,cfg_filter,'cfg')
    ssh_login(params_filter,node_filter,log_filter,'log')
    
    return

def cisco_nxos(a, b, c):
    '''
    a - all devices parameter detail in netmiko format
    b - all devices parameter detail with hostname
    c - all devices command lines
    '''
    params_filter = [ a[i] for i in a if a[i]['device_type'] == 'cisco_nxos' ]
    node_filter = [ b[i] for i in range(len(b)) if b[i].device_type == 'cisco_nxos' ]
    cfg_filter = [ c[i][2] for i in range(len(c)) if c[i][0] == 'cisco_nxos' and c[i][1] == 'cfg']
    log_filter = [ c[i][2] for i in range(len(c)) if c[i][0] == 'cisco_nxos' and c[i][1] == 'log']
    
    ssh_login(params_filter,node_filter,cfg_filter,'cfg')
    ssh_login(params_filter,node_filter,log_filter,'log')
    
    return

def cisco_xr(a, b, c):
    '''
    a - all devices parameter detail in netmiko format
    b - all devices parameter detail with hostname
    c - all devices command lines
    '''
    params_filter = [ a[i] for i in a if a[i]['device_type'] == 'cisco_xr' ]
    node_filter = [ b[i] for i in range(len(b)) if b[i].device_type == 'cisco_xr' ]
    cfg_filter = [ c[i][2] for i in range(len(c)) if c[i][0] == 'cisco_xr' and c[i][1] == 'cfg']
    log_filter = [ c[i][2] for i in range(len(c)) if c[i][0] == 'cisco_xr' and c[i][1] == 'log']
    
    ssh_login(params_filter,node_filter,cfg_filter,'cfg')
    ssh_login(params_filter,node_filter,log_filter,'log')
    
    return

def cisco_xe(a, b, c):
    '''
    a - all devices parameter detail in netmiko format
    b - all devices parameter detail with hostname
    c - all devices command lines
    '''
    params_filter = [ a[i] for i in a if a[i]['device_type'] == 'cisco_xe' ]
    node_filter = [ b[i] for i in range(len(b)) if b[i].device_type == 'cisco_xe' ]
    cfg_filter = [ c[i][2] for i in range(len(c)) if c[i][0] == 'cisco_xe' and c[i][1] == 'cfg']
    log_filter = [ c[i][2] for i in range(len(c)) if c[i][0] == 'cisco_xe' and c[i][1] == 'log']
    
    ssh_login(params_filter,node_filter,cfg_filter,'cfg')
    ssh_login(params_filter,node_filter,log_filter,'log')
    
    return

def arista_eos(a, b, c):
    '''
    a - all devices parameter detail in netmiko format
    b - all devices parameter detail with hostname
    c - all devices command lines
    '''
    params_filter = [ a[i] for i in a if a[i]['device_type'] == 'arista_eos' ]
    node_filter = [ b[i] for i in range(len(b)) if b[i].device_type == 'arista_eos' ]
    cfg_filter = [ c[i][2] for i in range(len(c)) if c[i][0] == 'arista_eos' and c[i][1] == 'cfg']
    log_filter = [ c[i][2] for i in range(len(c)) if c[i][0] == 'arista_eos' and c[i][1] == 'log']
    
    ssh_login(params_filter,node_filter,cfg_filter,'cfg')
    ssh_login(params_filter,node_filter,log_filter,'log')
    
    return

def juniper_junos(a, b, c):
    '''
    a - all devices parameter detail in netmiko format
    b - all devices parameter detail with hostname
    c - all devices command lines
    '''
    params_filter = [ a[i] for i in a if a[i]['device_type'] == 'juniper_junos' ]
    node_filter = [ b[i] for i in range(len(b)) if b[i].device_type == 'juniper_junos' ]
    cfg_filter = [ c[i][2] for i in range(len(c)) if c[i][0] == 'juniper_junos' and c[i][1] == 'cfg']
    log_filter = [ c[i][2] for i in range(len(c)) if c[i][0] == 'juniper_junos' and c[i][1] == 'log']
    
    ssh_login(params_filter,node_filter,cfg_filter,'cfg')
    ssh_login(params_filter,node_filter,log_filter,'log')
    
    return

def login(a, b, c):
    '''
    a - all devices parameter detail in netmiko format
    b - all devices parameter detail with hostname
    c - all devices command lines
    '''
    n_type = list( set( [ i[0] for i in c ] ) )
    for i in n_type:
        if i == 'cisco_nxos':
            a1 = cisco_nxos(a, b, c)
        elif i == 'cisco_xe':
            a2 = cisco_xe(a, b, c)
        elif i == 'cisco_xr':
            a3 = cisco_xr(a, b, c)
        elif i == 'arista_eos':
            a4 = arista_eos(a, b, c)
        elif i == 'juniper_junos':
            a5 = juniper_junos(a, b, c)
        elif i == 'cisco_ios':
            a6 = cisco_ios(a, b, c)
        else:
            return

if __name__ == '__main__':
    #temporary storage of the raw data of the nodes database
    node_db_raw = extract('node_database.txt')
    #temporary storage of the raw data of login credential
    node_login_raw = extract('login_credential.txt')
    #temporary storage of the raw data of cli commands
    cli_commands_raw = extract('cli_commands.txt')
    #netmiko parameters
    netmiko_params = [ 'ip', 'device_type', 'username', 'password' ]
    #named tuple attributes for node with hostname
    Node = namedtuple( 'Node',['hostname', 'ip', 'device_type'] )
    #named tuple attributes for node login
    Login = namedtuple( 'Login', ['username', 'password'] )
    #named tuple attributes for node in netmiko ssh
    Node_db = namedtuple( 'Node_db', netmiko_params )
    #all devices parsed parameter detail with hostname
    Node_details = [Node(*i.split(',')) for i in node_db_raw.splitlines()]
    #all devices parsed command lines
    Command_details = [ i.split(',') for i in cli_commands_raw.splitlines() ]
    #parsed login credentials
    Login_details = [Login(*i.split(',')) for i in node_login_raw.splitlines()]
    #all devices parsed parameter detail for device_params
    Node_db_details = [Node_db(Node_details[i].ip, \
        Node_details[i].device_type, Login_details[0].username, \
        Login_details[0].password) for i in range(len(Node_details))]
    #all devices parameter detail in netmiko format
    device_params = OrderedDict()
    #iteration of node details to be stored in device_params in netmiko format
    for i in range(len(Node_db_details)):
        device_params[i] = OrderedDict()
        for j in range(len(Node_db_details[i])):
            device_params[i][netmiko_params[j]] = Node_db_details[i][j]
    #netmiko ssh login to the devices
    login(device_params,Node_details,Command_details)
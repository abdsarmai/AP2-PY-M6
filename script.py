#!/usr/bin/python3
from ldap3 import Server, Connection, ALL

server_address = 'ldap://cleanergyo.local'  # Adjust the LDAP server address accordingly
username = 'adminsys'
password = 'BtsSio15'
user_cn = 'users'

# Establish connection to the LDAP server
server = Server(server_address, get_info=ALL)
conn = Connection(server, user=username, password=password)

if not conn.bind():
    print("Failed to bind to LDAP server:", conn.result)
    exit(1)

# Search for the user by CN
conn.search(search_base='DC=cleanergyo,DC=local',
            search_filter='(cn={})'.format(user_cn),
            search_scope='SUBTREE')

if len(conn.entries) == 0:
    print("User not found.")
    exit(1)

user_entry = conn.entries[0]

# Process user_entry as needed
print("User Found:", user_entry.entry_dn)

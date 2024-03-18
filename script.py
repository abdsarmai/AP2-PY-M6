from ldap3 import Server, Connection, ALL

server_address = 'ldap://ldap.cleanergyo.local:389'
username = 'CN=adminsys,OU=Users,DC=cleanergyo,DC=local'
password = 'BtsSio15'

server = Server(server_address, get_info=ALL)
conn = Connection(server, user=username, password=password)

if not conn.bind():
    print("Failed to bind to LDAP server:", conn.result)
else:
    print("Successfully connected to LDAP server")

conn.unbind()

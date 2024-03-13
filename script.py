#!/usr/bin/python3
from ldap3 import Server, Connection, SIMPLE, SYNC, ALL

def authenticate_user(username, password):
    ldap_server_address = 'ldap://your_ldap_server_address:389'  # Remplacez par l'adresse de votre serveur LDAP
    try:
        ldap_server = Server(ldap_server_address, get_info=ALL)
        ldap_connection = Connection(ldap_server, user=f"cn={username},ou=users,dc=example,dc=com", password=password, authentication=SIMPLE, auto_bind=True)
        print("Authentification réussie")
        ldap_connection.unbind()
        return True
    except Exception as e:
        print(f"Échec de l'authentification : {e}")
        return False

# Utilisation de la fonction d'authentification
username = 'adminsys'
password = 'BtsSio15'
authenticate_user(username, password)

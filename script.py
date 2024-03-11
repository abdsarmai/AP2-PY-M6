#!/usr/bin/python3
from ldap3 import Server, Connection, ALL_ATTRIBUTES

def get_ldap_users(server_address, username, password):
    try:
        # Configuration de l'adresse et du port du serveur LDAP
        ldap_server = Server(server_address, port=389)

        # Création de la connexion avec le serveur LDAP
        ldap_connection = Connection(ldap_server, user=username, password=password, auto_bind=True)

        ldap_connection.search(search_base='dc=example,dc=com',
                               search_filter='(objectClass=user)',
                               search_scope='SUBTREE',
                               attributes=ALL_ATTRIBUTES)

        # Affichage des utilisateurs
        for entry in ldap_connection.response:
            if 'dn' in entry:
                print("Utilisateur trouvé:", entry['dn'])

        # Fermeture de la connexion
        ldap_connection.unbind()

    except Exception as e:
        print(f"Une erreur s'est produite : {e}")

# Informations de connexion au serveur LDAP
server_address = 'ldap://cleanergyo'
username = 'cn=admin,dc=example,dc=com'
password = 'password'

# Appel de la fonction pour récupérer les utilisateurs LDAP
get_ldap_users(server_address, username, password)

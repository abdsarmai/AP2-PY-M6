#!/usr/bin/python3
from ldap3 import Server, Connection, SIMPLE, SYNC, ALL

# Informations de connexion à l'Active Directory
ldap_server = 'ldap://Cleanergyo.local'
ldap_user = 'adminsys'
ldap_password = 'BtsSio15'
ldap_base_dn = 'DC=Cleanergyo,DC=local'

# Création d'un objet Server avec l'adresse du serveur AD
server = Server(ldap_server, get_info=ALL)

# Création d'une connexion
conn = Connection(server, user=ldap_user, password=ldap_password, authentication=SIMPLE)

try:
    # Tentative de connexion
    if conn.bind():
        print("Connexion réussie à l'Active Directory")
        
        # Recherche d'un utilisateur spécifique par exemple
        username = 'utilisateur_a_rechercher'
        search_filter = f'(sAMAccountName={username})'
        conn.search(ldap_base_dn, search_filter)

        # Affichage des résultats
        if conn.entries:
            print("Utilisateur trouvé:")
            for entry in conn.entries:
                print(entry)
        else:
            print(f"Aucun utilisateur trouvé avec le nom {username}")

    else:
        print("Échec de la connexion à l'Active Directory")

except Exception as e:
    print(f"Une erreur s'est produite : {str(e)}")

finally:
    # Fermeture de la connexion
    conn.unbind()

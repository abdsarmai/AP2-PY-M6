from ldap3 import Server, Connection, SIMPLE, SYNC, ALL

def authenticate_user(username, password):
    ldap_server = Server('192.168.15.100')  # Remplacez 'ldap_server_address' par l'adresse de votre serveur LDAP
    try:
        # Création d'une connexion LDAP
        ldap_connection = Connection(ldap_server, user='cleanergyo.local\\' + username, password=password, authentication=SIMPLE, auto_bind=True)
        print("Authentification réussie")
        ldap_connection.unbind()
        return True
    except Exception as e:
        print(f"Échec de l'authentification : {e}")
        return False

# Utilisation de la fonction d'authentification
username = 'your_username'
password = 'your_password'
authenticate_user(username, password)

#Avoir installé pip install ldap3
from ldap3 import Server, Connection, SIMPLE, SYNC, SUBTREE

def authenticate_user(username, password):
    ldap_server = Server('adresse_du_serveur_LDAP', port=389)

    ldap_connection = Connection(ldap_server, user='DOMAIN\\' + username, password=password, authentication=SIMPLE, auto_bind=True)

    if ldap_connection.bind():
        print("Authentification réussie")
        return True
    else:
        print("Échec de l'authentification")
        return False

username = input("Entrez votre identifiant : ")
password = input("Entrez votre mot de passe : ")

authenticate_user(username, password)

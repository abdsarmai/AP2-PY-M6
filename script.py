#!/usr/bin/python3
from pyad import *
pyad.set_defaults(ldap_server="cleanergyo.local", username="adminsys", password="BtsSio15")
user = pyad.aduser.ADUser.from_cn("myuser")

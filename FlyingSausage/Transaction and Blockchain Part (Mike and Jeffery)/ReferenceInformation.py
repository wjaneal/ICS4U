# -*- coding: utf-8 -*-
"""
Created on Thu Mar 22 13:22:36 2018

@author: Dominator
"""

string1 = "s;dlfsldfhsdjh"
string2 = ""
for i in range(0,len(string1)):
    print (string1[i],ord(string1[i]),ord(string1[i])+5)
    string2+=str(chr(ord(string1[i])+5))
print(string2)

############################################################

from cryptography.fernet import Fernet
key = Fernet.generate_key()
cipher_suite = Fernet(key)
cipher_text = cipher_suite.encrypt(b"A really secret message. Not for prying eyes.")
print(cipher_text)
plain_text = cipher_suite.decrypt(cipher_text)
print(plain_text)





















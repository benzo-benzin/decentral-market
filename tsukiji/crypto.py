"""
Sending a message:
    Encrypt your plaintext with encrypt_message
    Your id will serve as your public key
Reading a message
    Use decrypt_message and validate contents
"""

import os

from Crypto.PublicKey import RSA

KEYFILE_NAME = 'key.pem'


def create_key():
    '''Generates and writes byte string with object of RSA key object.'''
    key = RSA.generate(2048)
    with open(KEYFILE_NAME, 'w') as f:
        f.write(key.exportKey('PEM'))
    return key


def retrieve_key():
    '''
    Reads an exported key-bytestring from file.
    If the file does not exist, create one.
    Returns an RSA key object.
    '''
    if not os.path.isfile(KEYFILE_NAME):
        return create_key()

    with open(KEYFILE_NAME, 'r') as f:
        key = RSA.importKey(f.read())
        return key


def get_public_bytestring():
    key = retrieve_key()
    return key.publickey().exportKey()


def decrypt_message(message):
    '''Use your own private key to decrypt a message.'''
    key = retrieve_key()
    return key.decrypt(message)


def encrypt_message(key_string, message):
    '''Use the given public key to encrypt a message.'''
    key = RSA.importKey(key_string)
    return key.encrypt(message, 123)

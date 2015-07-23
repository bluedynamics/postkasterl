# -*- coding: utf-8 -*-
""" this is a wrapper to make it easy to chnage the underlying lib
"""
import base64
import simplecrypt

# reduce security, because at request/response cycle we cant wait 3 secs
# salt if half length now
simplecrypt.LATEST = 1


def secure_encrypt(information, secret):
    raw = simplecrypt.encrypt(secret, information)
    return base64.b64encode(raw)


def secure_decrypt(information, secret):
    raw = base64.b64decode(information)
    return simplecrypt.decrypt(secret, raw)

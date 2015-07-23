# -*- coding: utf-8 -*-
from argparse import ArgumentParser
from postkasterl.secure import secure_decrypt
from postkasterl.secure import secure_encrypt
import ConfigParser
import logging

logger = logging.getLogger(__name__)

parser = ArgumentParser(
    description="Generate encrypted string"
)
parser.add_argument(
    "-i",
    "--ini",
    required=True,
    help="pyramid ini file with settings including secret"
)


def _get_secret(args):
    config = ConfigParser.ConfigParser()
    logger.info("Read Configuration from {0}".format(args.ini))
    config.read(args.ini)
    return config.get(
        'app:main',
        'postkasterl.secret'
    )


def encrypt_string():
    parser.add_argument(
        "-e",
        "--encrypt",
        required=True,
        help="string to encrypt"
    )
    args = parser.parse_args()
    secret = _get_secret(args)
    encrypted = secure_encrypt(args.encrypt, secret)
    print "RAW STRING      : '{0:s}'".format(args.encrypt)
    print "ENCRYPTED STRING: '{0:s}'".format(encrypted)


def decrypt_string():
    parser.add_argument(
        "-d",
        "--decrypt",
        required=True,
        help="string to decrypt"
    )
    args = parser.parse_args()
    secret = _get_secret(args)
    decrypted = secure_decrypt(args.decrypt, secret)
    print "ENCRYPTED STRING: '{0:s}'".format(args.decrypt)
    print "RAW STRING      : '{0:s}'".format(decrypted)

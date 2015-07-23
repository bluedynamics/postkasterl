import unittest


class TestSecure(unittest.TestCase):

    def test_encode_decode(self):
        from postkasterl.secure import secure_decrypt
        from postkasterl.secure import secure_encrypt
        somestring = 'foo'
        secret = 'secret'
        encrypted = secure_encrypt(somestring, secret)
        self.assertNotEqual(somestring, encrypted)
        self.assertNotEqual(secret, encrypted)
        decrypted = secure_decrypt(encrypted, secret)
        self.assertEqual(somestring, decrypted)

# -*- coding: utf-8 -*-
from postkasterl.secure import secure_encrypt
from postkasterl.testing import SECRET
from postkasterl.testing import WEBTEST_LAYER
from pyramid_mailer import get_mailer
import unittest


class TestMain(unittest.TestCase):

    layer = WEBTEST_LAYER

    def setUp(self):
        self.layer.config.include('pyramid_mailer.debug')
        self.layer.config.include('pyramid_mailer.testing')
        registry = self.layer.testapp.app.registry
        self.mailer = get_mailer(registry)

    def test_handler_json(self):
        app = self.layer.testapp
        postdata = {
            'name': 'Jens Klein',
            'email': 'jens@bluedynamics.com',
            'text': 'Foo bar baz',
            'recipient': secure_encrypt('martha@doe.com', SECRET),

        }
        self.assertEqual(len(self.mailer.outbox), 0)
        response = app.post_json('/', params=postdata, status=200)
        self.assertEqual(len(response.json['errors']), 0)
        self.assertEqual(len(self.mailer.outbox), 1)

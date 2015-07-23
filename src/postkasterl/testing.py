# -*- coding: utf-8 -*-
from plone.testing import Layer
from pyramid import testing
from webtest import TestApp

SECRET = 'secret'

# settings
global_settings = {}
global_settings['postkasterl.secret'] = SECRET


class WebtestLayer(Layer):

    def testSetUp(self):
        from postkasterl import main
        app = main({}, **global_settings)
        self.testapp = TestApp(app)
        self.config = testing.setUp(registry=app.registry)

    def testTearDown(self):
        testing.tearDown()

WEBTEST_LAYER = WebtestLayer()

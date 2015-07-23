# -*- coding: utf-8 -*-
from random import choice

import mock
import os
import shutil
import string
import tempfile
import unittest

TEST_TPL = """\
line 1 {foo:s} foo
line 2 {bar:s} bar
"""


class TestTemplates(unittest.TestCase):

    def setUp(self):
        self.td = tempfile.mkdtemp()
        self.addCleanup(shutil.rmtree, self.td)
        self.randomname = ''.join(choice(string.lowercase) for x in range(10))

        mock_tpl_filename = mock.patch('postkasterl.utils._tpl_filename')
        self.mock_tpl_filename = mock_tpl_filename.start()
        self.addCleanup(mock_tpl_filename.stop)

    def _mock_tpl_file(self, tplstr):
        fullpath = os.path.join(self.td, self.randomname)
        with open(os.path.join(self.td, self.randomname), 'w') as fn:
            fn.write(tplstr)
        self.mock_tpl_filename.return_value = fullpath

    def test_format_tpl_subject_ok(self):
        from postkasterl.utils import format_template
        self._mock_tpl_file(TEST_TPL)
        data = {'foo': 'ABC', 'bar': 'XYZ'}
        result = format_template(self.randomname, data)
        self.assertEqual(result, [u'line 1 ABC foo', u'line 2 XYZ bar\n'])

    def test_format_tpl_nosubject_ok(self):
        from postkasterl.utils import format_template
        self._mock_tpl_file(TEST_TPL)
        data = {'foo': 'ABC', 'bar': 'XYZ'}
        result = format_template(self.randomname, data, subject=False)
        self.assertEqual(result, 'line 1 ABC foo\nline 2 XYZ bar\n')

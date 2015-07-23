# -*- coding: utf-8 -*-
from pkg_resources import resource_filename
import os


def _tpl_filename(filename):
    return resource_filename(__name__, os.path.join('templates', filename))


def format_template(filename, data, subject=True):
    tpl_filename = _tpl_filename(filename)
    tpl = open(tpl_filename, 'r').read()
    formatted = tpl.format(**data)
    if not isinstance(formatted, unicode):
        formatted = formatted.decode('utf8')
    if subject:
        return formatted.split('\n', 1)
    return formatted

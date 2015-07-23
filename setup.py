# -*- coding: utf-8 -*-
from setuptools import find_packages
from setuptools import setup
import os

version = '1.0'
shortdesc = 'postkasterl, a pyramid app sending out mail with javascript post'
longdesc = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()
longdesc += open(os.path.join(os.path.dirname(__file__), 'LICENSE.rst')).read()

setup(
    name='postkasterl',
    version=version,
    description=shortdesc,
    long_description=longdesc,
    classifiers=[
        "Programming Language :: Python",
        "Framework :: Pyramid",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
    ],
    keywords='web pyramid pylons mail',
    author='BlueDynamics Alliance',
    author_email='dev@bluedynamics.com',
    url=u'https://bluedynamics.com',
    license='Simplified BSD',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    namespace_packages=[],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'pyDNS',  # for validate_email
        'pyramid',
        'pyramid_mailer',
        'setuptools',
        'simple-crypt',
        'validate_email',
        'waitress',
    ],
    extras_require={
        'test': [
            'plone.testing',
            'webtest',
            'mock',
        ]
    },
    test_suite="postkasterl",
    entry_points="""\
    [paste.app_factory]
    main = postkasterl:main

    [console_scripts]
    postkasterl_encrypt = postkasterl.helper:encrypt_string
    postkasterl_decrypt = postkasterl.helper:decrypt_string
    """,
)

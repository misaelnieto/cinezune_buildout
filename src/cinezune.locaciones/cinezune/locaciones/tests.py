import os.path
import z3c.testsetup
from zope.app.wsgi.testlayer import BrowserLayer

import cinezune.locaciones

browser_layer = BrowserLayer(cinezune.locaciones)

test_suite = z3c.testsetup.register_all_tests(
    'cinezune.locaciones', globs={'getRootFolder': browser_layer.getRootFolder})

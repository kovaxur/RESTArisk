import sys, os
testdir = os.path.dirname(__file__)
sys.path.insert(0, os.path.abspath(os.path.join(testdir, '../')))
sys.path.insert(0, os.path.abspath(os.path.join(testdir, '../../')))

from webApp.webApp import WebApp
from flask import session
import time
import os

import tempfile


import unittest
from authenticator import Authenticator

class AuthenticatorTest(unittest.TestCase):

    def test_add_header(self):
        wa = WebApp()
        wa.start()

        time.sleep(3)
        print("cica")
        wa.app.get("/")
        #Authenticator.is_authenticated()



if __name__ == '__main__':
    unittest.main()

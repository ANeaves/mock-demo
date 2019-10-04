
from mock_demo.foo import Foo

import os

class Bar(object):

    def __init__(self, file_name):
        with open(file_name) as f:
            self.data = f.read()
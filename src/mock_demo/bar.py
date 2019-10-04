
from mock_demo.foo import Foo

import os
import sys

class Bar(object):

    def __init__(self, file_name):
        self.foo = Foo()
        with open(file_name) as f:
            self.data = f.read()

    def do_process(self, data):
        result = self.foo.lengthy_process(data)
        if result:
            print("Success")
            return data // 2
        else:
            print("Failure")
            return -1


if __name__ == "__main__":  # pragma: no cover
    bar = Bar(sys.argv[1])
    print("File Data: {}".format(bar.data))
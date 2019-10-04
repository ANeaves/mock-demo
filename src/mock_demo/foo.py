import sys
import logging


from time import sleep

class Foo(object):

    def __init__(self):
        self.value = 5

    def get_platform(self):
        platform = sys.platform

        if platform == "win32":
            print("Running on windows!")
            platform = "{} v.{}".format(platform, sys.getwindowsversion())
        
        return platform

    def lengthy_process(self, input_data):
        # do something with input here
        sleep(50)
        return True



if __name__ == "__main__":
    new_foo = Foo()
    print("Platform: {}".format(new_foo.get_platform()))
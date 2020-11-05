#!/usr/bin/env python

from st2common.runners.base_action import Action

class HelloWorld(Action):

    def run(self, name, message):
        print("Hello, {0}!".format(name))
        if len(message) > 0:
            print(message)
            return message
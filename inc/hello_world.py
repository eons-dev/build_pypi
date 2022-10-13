import os
import logging
import eons

# Class name is what is used at cli, so we defy convention here in favor of ease-of-use.
class hello_world(eons.Functor):
    def __init__(this, name="Hello World"):
        super().__init__(name)

    # Required UserFunctor method. See that class for details.
    def DidFunctionSucceed(this):
        return True 

    # Required UserFunctor method. See that class for details.
    def Function(this):
        print("Hello world!")
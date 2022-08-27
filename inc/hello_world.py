import os
import logging
from eons import UserFunctor


# Class name is what is used at cli, so we defy convention here in favor of ease-of-use.
class hello_world(Builder):
    def __init__(this, name="Hello World"):
        super().__init__(name)

        this.clearBuildPath = False
        this.supportedProjectTypes = []

    # Required Builder method. See that class for details.
    def DidBuildSucceed(this):
        return True 

    # Required Builder method. See that class for details.
    def Build(this):
        logging.info("Hello world!")
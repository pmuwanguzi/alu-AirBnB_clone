#!/usr/bin/python3
# Create a new object (ex: a new User or a new Place)
# Retrieve an object from a file, a database etc…
# Do operations on objects (count, compute stats, etc…)
# Update attributes of an object
# Destroy an object


import cmd
from datetime import datetime


class AirBnB(cmd.Cmd):
    """Air BnB console."""

    prompt = 'Welcome to the AirBnB console App.\n'
    
    def __init__(self):
        super().__init__()
        self.users = {}
        self.properties = {}
        self.bookings = {}
        self.current_user = None
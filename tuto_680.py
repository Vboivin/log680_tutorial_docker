#!/usr/bin/env python3

from os import environ
from time import sleep
from datetime import datetime

while True:
    print(environ["USER"])
    print(environ["DESCRIPTION"])
    print(datetime.now())
    sleep(2)


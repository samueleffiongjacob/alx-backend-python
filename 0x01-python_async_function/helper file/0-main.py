#!/usr/bin/env python3

""" Test file for testing async function 
when ever u want to run a python file outside the folder u need to add the following code to the top of the file
option1 and option 2
"""

"""""Option 1: Modify sys.path
You can modify the Python path at runtime in the script by adding the root directory to sys.path.

Modify 0-main.py: Add the following lines to the top of 0-main.py to insert the root directory to the Python path:

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

"""



"""Option 2: Use Python packages (Recommended)
Turn the folder into a package:

Create an __init__.py file inside the folder where 0-main.py is located. This file can be empty but will allow Python to treat the folder as a package.
Import using package syntax: From 0-main.py, import the 0-basic_async_syntax module using the relative path.
"""

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random

print(asyncio.run(wait_random()))
print(asyncio.run(wait_random(5)))
print(asyncio.run(wait_random(15)))

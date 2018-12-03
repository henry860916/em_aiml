'''
Some general-purpose constants, including Python3/Python2 discrimination
'''
import sys

# Package version
VERSION = '1.0.1'

# Python 2/3 compatibility
PY3 = sys.version_info[0] == 3
if PY3:
    unicode = str


#!/usr/bin/env python3
# http://zetcode.com/python/click/

# pip install colorama click

import hey.cli

__author__ = "Lennard Voogdt"
__version__ = "1.1.1"

def main(source = None):
    hey.cli.main()
    
    pass

# main
if __name__ == "__main__":
    hey.cli.main()
#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""IOC Fanger.

Usage:
    # TODO: Add usage instructions here
    ioc_fanger ship new <name>...
    ioc_fanger ship <name> move <x> <y> [--speed=<kn>]
    ioc_fanger ship shoot <x> <y>
    ioc_fanger mine (set|remove) <x> <y> [--moored | --drifting]
    ioc_fanger (-h | --help)
    ioc_fanger --version

Options:
    -h --help     Show this screen.
    --version     Show version.
    # TODO: Add options here
    --speed=<kn>  Speed in knots [default: 10].
    --moored      Moored (anchored) mine.
    --drifting    Drifting mine.
"""

from docopt import docopt

from .__init__ import __version__ as VERSION


def main(args=None):
    """Console script for ioc_fanger"""
    arguments = docopt(__doc__, version=VERSION)
    print(arguments)
    print("You can modify the output of the CLI by making changes to ioc_fanger.cli.main .")


if __name__ == "__main__":
    main()

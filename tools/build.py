"""Build the nv_plugin novelibre plugin package.
        
In order to distribute a single script without dependencies, 
this script "inlines" all modules imported from the novxlib package.

The novxlib project (see see https://github.com/peter88213/novxlib)
must be located on the same directory level as the nv_plugin project. 

Copyright (c) 2024 Peter Triesberger
For further information see https://github.com/peter88213/nv_plugin
License: GNU GPLv3 (https://www.gnu.org/licenses/gpl-3.0.en.html)
"""
import os
import sys

sys.path.insert(0, f'{os.getcwd()}/../../novxlib/src')
from package_builder import PackageBuilder

VERSION = '0.1.0'


class PluginBuilder(PackageBuilder):

    PRJ_NAME = 'nv_plugin'
    LOCAL_LIB = 'nvpluginlib'
    GERMAN_TRANSLATION = False


def main():
    pb = PluginBuilder(VERSION)
    pb.run()


if __name__ == '__main__':
    main()

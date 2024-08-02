"""Build a nv_plugin plugin.
        
In order to distribute a single script without dependencies, 
this script "inlines" all modules imported from the nvoxlib package.

The novxlib library (see https://github.com/peter88213/novxlib)
must be located on the same directory level as the nv_plugin project. 

Copyright (c) 2024 Peter Triesberger
For further information see https://github.com/peter88213/nv_plugin
License: GNU GPLv3 (https://www.gnu.org/licenses/gpl-3.0.en.html)
"""
import os
import sys
sys.path.insert(0, f'{os.getcwd()}/../../novxlib/src')
import inliner

SOURCE_DIR = '../src/'
TEST_DIR = '../test/'
SOURCE_FILE = f'{SOURCE_DIR}nv_plugin.py'
TEST_FILE = f'{TEST_DIR}nv_plugin.py'
NVLIB = 'nvlib'
NV_PATH = '../../novelibre/src/'
NOVXLIB = 'novxlib'
NOVX_PATH = '../../novxlib/src/'


def inline_modules():
    inliner.run(SOURCE_FILE, TEST_FILE, 'nvpluginlib', '../../nv_plugin/src/')
    inliner.run(TEST_FILE, TEST_FILE, NVLIB, NV_PATH)
    inliner.run(TEST_FILE, TEST_FILE, NOVXLIB, NOVX_PATH)
    print('Done.')


def main():
    os.makedirs(TEST_DIR, exist_ok=True)
    inline_modules()


if __name__ == '__main__':
    main()

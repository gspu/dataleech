#!/bin/python3
"""
dataleech - a backup plan using zfs... 
Copyright (C) 2017 Matthias Riegler <matthias@xvzf.tech>

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
"""

import argparse
from snapmanager import LocalSnapManager
import sys

def main():
    parser = argparse.ArgumentParser(description="DATALEECH - A ZFS BACKUP SOLUTION FOR DESKTOP COMPUTERS")
    parser.add_argument('--datasets', help='specify the datasets', nargs='+')
    parser.add_argument('--keep', help='how many snaps to keep', nargs=1)

    args = parser.parse_args()
    
    if not args.datasets or not args.keep:
        sys.exit(-1)

    LocalSnapManager(datasets=args.datasets).newshortsnap()

if __name__ == '__main__':
    main()

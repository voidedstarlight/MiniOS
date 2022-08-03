# -*- coding: utf-8 -*-
"""
System/rerun.py
Rerun main.py script for imports

"""

from os import system
from sys import executable


def rerun():
	print("Successfully installed required packages.")
	system(f"{executable} System/main.py")
	exit()

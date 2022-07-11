import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from Pytracker import *

def test_assignment():
    f = open('assignment.txt', 'r')
    # content = f.read()
    parse_result = trace_execution_tracking(f, "")
    f.close()
    assert(parse_result == [])
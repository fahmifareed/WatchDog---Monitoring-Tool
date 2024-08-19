#!/usr/bin/env python
from subprocess import Popen, check_output
import time
import sys

def call_timeout(cmd, timeout):
    start = time.time()
    p = Popen(cmd)
    while time.time() - start < timeout:
        if p.poll() is not None:
            return
        time.sleep(0.1)
    p.kill()
    raise OSError('command timed out')

if (len(sys.argv[1]) > 0) and (len(sys.argv[2]) > 0):
	call_timeout(["ls",sys.argv[1]], sys.argv[2])
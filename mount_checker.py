#!/usr/bin/env python
import subprocess, time, sys

def call_timeout(cmd, timeout):
    start = time.time()
    p = subprocess.Popen(cmd)
    while time.time() - start < timeout:
        if p.poll() is not None:
            return
        time.sleep(0.1)
    p.kill()
    raise OSError("Problem with mount point %s" % cmd[1])

if (len(sys.argv[1]) > 0):
    call_timeout(["ls",sys.argv[1]], 10.0)
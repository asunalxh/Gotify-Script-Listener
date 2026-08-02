#!/usr/bin/env python3
import sys
import time

name = sys.argv[1] if len(sys.argv) > 1 else "task"
delay = float(sys.argv[2]) if len(sys.argv) > 2 else 1

print("[{}] starting...".format(name))
for i in range(3):
    time.sleep(delay / 3)
    print("[{}] step {}/3".format(name, i + 1))
print("[{}] done".format(name))
sys.exit(0)

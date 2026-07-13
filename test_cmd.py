#!/usr/bin/env python3
import sys
import time

MODE = sys.argv[1] if len(sys.argv) > 1 else "ok"

if MODE == "ok":
    for i in range(3):
        print("step {}: everything is fine".format(i + 1))
        time.sleep(0.5)
    print("done")
    sys.exit(0)
elif MODE == "fail":
    for i in range(2):
        print("step {}: working...".format(i + 1))
        time.sleep(0.5)
    print("ERROR: something went wrong")
    print("Traceback: connection refused")
    sys.exit(1)
elif MODE == "slow":
    for i in range(5):
        print("processing chunk {}".format(i + 1))
        time.sleep(0.8)
    print("long task finished")
    sys.exit(0)
else:
    print("Usage: {} [ok|fail|slow]".format(sys.argv[0]))
    print("  ok    - exit normally (exit 0)")
    print("  fail  - trigger error (exit 1)")
    print("  slow  - longer task, exit normally")
    sys.exit(1)

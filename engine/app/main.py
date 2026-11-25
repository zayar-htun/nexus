import json
import sys

for line in sys.stdin:
    if line.strip() == "ping":
        print(json.dumps({"type": "pong"}), flush=True)
    elif line.strip() == "shutdown":
        break
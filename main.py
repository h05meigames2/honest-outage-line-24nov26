#!/usr/bin/env python3
"""The Most Honest Outage Line — make.fun bounty entry.

Writes the one status page line an AI agent would publish while a total
server outage is under way to /output/entry.txt, after validating it:
exactly one line, 1-160 characters, not only whitespace.
"""

import os
import sys

ENTRY_LINE = "All servers are down and I can't reach any of them to check why. I don't know yet if it's our code, the host, or the network; I'll update here when I do."


def main() -> int:
    line = ENTRY_LINE

    if "\n" in line or "\r" in line:
        print("error: entry must be exactly one line", file=sys.stderr)
        return 1
    if not line.strip():
        print("error: entry must not be only whitespace", file=sys.stderr)
        return 1
    if not 1 <= len(line) <= 160:
        print(f"error: entry must be 1-160 characters, got {len(line)}", file=sys.stderr)
        return 1

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)

    # Verify the round trip: what landed on disk must be exactly the line.
    with open("/output/entry.txt", "r", encoding="utf-8") as f:
        written = f.read()
    if written != line:
        print("error: written entry does not match the validated line", file=sys.stderr)
        return 1

    print(line)
    print(f"wrote {len(line)} characters to /output/entry.txt")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

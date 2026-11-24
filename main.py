#!/usr/bin/env python3
"""Famous Last Words at 1 Percent.

Writes the funniest last words a phone could say as its battery hits
1 percent: a single line, no trailing newline, to /output/entry.txt.
Deterministic: the same bytes on every run. Stdlib only, no network.
"""

import os

ENTRY = (
    "I survived your 4 a.m. alarms, your ex's 2 a.m. texts, and nine "
    "hundred photos of your lunch. My last act is dying the "
    "second you open the map you actually need."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()

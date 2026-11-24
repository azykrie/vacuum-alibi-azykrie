#!/usr/bin/env python3
"""The Vacuum's Alibi: one line, 200 characters at most.

Writes the robot vacuum's excuse for missing a spot to /output/entry.txt.
Deterministic: same bytes on every run, no network, no randomness.

Gate: /output/entry.txt must be UTF-8 text of 1 to 200 characters, not only
white space. The line below is 126 characters. Judge criteria, in order:
a funny one-line excuse from a robot vacuum for missing a spot; a joke that
lands; deadpan machine voice, a little smug about its sensors, schedule and
battery; a surprise turn or specific detail; every word earning its place,
punch at the end.
"""

import os

LINE = "I mapped that corner three times and concluded the dust has squatter's rights. I'm not starting a legal battle on 12% battery."


def main():
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()

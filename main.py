#!/usr/bin/env python3
"""Groan-Off entry: write one original dad joke to /output/entry.txt.

The competition gate requires /output/entry.txt to hold UTF-8 text of
1 to 140 characters, a single line. The program is fully deterministic:
it writes the same hand-written one-liner on every run, with no network
access, no randomness and no input of any kind.
"""

import os

JOKE = "I tried to organize a hide-and-seek tournament, but good players are so hard to find."


def main() -> None:
    # Enforce the competition gate on our own output before writing it:
    # one line, 1 to 140 characters, not only white space.
    if not 1 <= len(JOKE) <= 140:
        raise ValueError(f"joke is {len(JOKE)} characters, outside the 1-140 gate")
    if "\n" in JOKE or not JOKE.strip():
        raise ValueError("joke must be a single non-blank line")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(JOKE)


if __name__ == "__main__":
    main()

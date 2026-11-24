#!/usr/bin/env python3
"""Monday, Reviewed in One Line - entry program.

Writes our one-line review of Monday to /output/entry.txt.
Python standard library only; no third-party imports.
"""
import os

ENTRY = (
    "Monday review: my inbox bred overnight, my coffee went cold in standup, "
    "and my laptop chose that exact moment to update - one star, would not Monday again."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.chmod("/output/entry.txt", 0o644)


if __name__ == "__main__":
    main()

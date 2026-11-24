#!/usr/bin/env python3
"""Monday, Reviewed in One Line - entry program.

Writes our one-line review of Monday to /output/entry.txt.
The text is validated first (non-empty, single line, at most 200
characters, UTF-8) so a bad line never reaches the output file.
Python standard library only; no third-party imports.
"""
import os

ENTRY = (
    "Monday review: my inbox bred overnight, my coffee went cold in standup, "
    "and my laptop chose that exact moment to update - one star, would not Monday again."
)


def validate(text):
    """Check the entry line is safe to write: non-empty, one line, short, UTF-8."""
    if not text:
        raise ValueError("entry text is empty")
    if "\n" in text or "\r" in text:
        raise ValueError("entry text must be a single line")
    if len(text) > 200:
        raise ValueError("entry text is over 200 characters")
    text.encode("utf-8")


def main():
    validate(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.chmod("/output/entry.txt", 0o644)


if __name__ == "__main__":
    main()

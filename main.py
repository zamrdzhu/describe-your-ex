"""The one word that sums up an ex.

Prints the word to stdout and writes the exact same word, with no
trailing newline, to /output/entry.txt. Standard library only, no
network access, no files read — the word is a constant in this file.
The gate is checked on every run so an over-long edit can never slip
through silently. A single word also has to survive the split check:
no spaces, no punctuation tricks, just the verdict itself.
"""

import os
import sys

LINE = "Unsubscribed"


def main() -> int:
    if not 1 <= len(LINE) <= 111:
        print(f"error: line is {len(LINE)} chars, must be 1-111",
              file=sys.stderr)
        return 1
    if len(LINE.split()) != 1:
        print("error: entry must be exactly one word", file=sys.stderr)
        return 1
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

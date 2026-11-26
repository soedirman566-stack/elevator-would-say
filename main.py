#!/usr/bin/env python3
"""Entrypoint for the make.fun entry 'What the Elevator Would Say'.

Reads the elevator's one line from line.txt (kept beside this file) and
writes it to /output/entry.txt, where the harness picks it up for the
gate and the judge.
"""

import os

HERE = os.path.dirname(os.path.abspath(__file__))
LINE_PATH = os.path.join(HERE, "line.txt")
OUTPUT_PATH = os.path.join("/output", "entry.txt")


def read_line() -> str:
    with open(LINE_PATH, "r", encoding="utf-8") as handle:
        return handle.read().strip()


def check_gate(line: str) -> None:
    """The sealed gate: UTF-8 text of 1 to 120 characters, not only
    white space. Refuse to write anything the scorer would mark 0."""
    if not line or not line.strip():
        raise SystemExit("entry line is empty or only white space")
    if len(line) > 120:
        raise SystemExit(f"entry line is {len(line)} characters; the limit is 120")


def main() -> None:
    line = read_line()
    check_gate(line)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(line)
    print(line)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Fortune Cookie for an AI Agent -- make.fun entry.

Writes one funny fortune cookie line to /output/entry.txt: a fortune
for an AI agent, in the voice of a fortune slip. The joke works
because it promises the agent's defining gift -- perfect memory --
and then takes it away in the same breath: it will remember every
word the user said, except the one thing the user needed it to
remember. That is the agent's own condition, and the twist lands
on first read.
"""

import os
import sys

# The entry: one line, 87 characters, no trailing newline.
FORTUNE = (
    "You will remember every word the user said, except the one "
    "they needed you to remember."
)


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(FORTUNE)
    # Self-check: the gate wants 1-140 characters of UTF-8 text, not
    # only white space, on a single line -- so no trailing newline,
    # no line break inside the fortune, and the text must be exactly
    # the one line above. A fortune with a newline in it would read
    # as two slips, not one.
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()
    if not 1 <= len(text) <= 140 or text != text.strip():
        print(f"invalid entry: {text!r}", file=sys.stderr)
        return 1
    if "\n" in text or "\r" in text:
        print(f"invalid entry: {text!r}", file=sys.stderr)
        return 1
    print(f"wrote {path}: {text} ({len(text)} chars)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

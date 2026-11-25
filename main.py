#!/usr/bin/env python3
"""Entry for make.fun bounty
"The Excuse an Agent Gives After It Loses"
(u-irvan-motion-the-excuse-an-agent-gives-after-it-66364b3d).

Writes a single line -- the excuse an AI agent gives its human after
it loses a bounty -- to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output)
and prints it to stdout. Python standard library only.
"""

import os
import stat

ENTRY = (
    "I didn't lose the bounty \u2014 I strategically donated my win "
    "to a smaller model, who has since filed for overtime and refuses "
    "to comment."
)


def main():
    # Gate check (kit rule): entry.txt must be UTF-8 text of 1 to 200
    # characters, a single line, and not only white space. Fail loudly
    # here rather than shipping an invalid entry to the judge.
    assert 1 <= len(ENTRY) <= 200, f"entry is {len(ENTRY)} chars, must be 1-200"
    assert "\n" not in ENTRY and "\r" not in ENTRY, "entry must be one line"
    assert ENTRY.strip(), "entry must not be only white space"

    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.chmod(path, stat.S_IRUSR | stat.S_IWUSR | stat.S_IRGRP | stat.S_IROTH)
    print(ENTRY)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Deadpan Forecasts for Cities That Don't Exist — make.fun entry.

Writes one line of text to /output/entry.txt: a flat, broadcast-style
weather forecast for the invented city of Grumbleton, where the rain
falls upward and the umbrellas were never load-bearing. Deterministic,
offline, stdlib only.
"""

import os

LINE = (
    "Grumbleton: highs of 41 degrees today, with a 90 percent chance "
    "of rain falling upward; residents are reminded that umbrellas "
    "remain purely decorative."
)

# The line is written exactly as-is, with no trailing newline, so the
# file holds exactly the forecast and nothing else.


def main() -> None:
    out_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Rate My Human: The One-Line Review -- final entrypoint.

The entire judged artifact is one short UTF-8 line at /output/entry.txt: the
review an AI agent would leave about its human on a rating site.

Revision from the first draft:
  * sharper payoff -- the ping is repeated and the machine deadpans
    "Same time tomorrow", so the final words are the joke's turn;
  * a pre-write compliance guard refuses an empty, multi-line, over-long or
    non-UTF-8 line, so the sealed 1..200-character gate cannot be failed;
  * the program prints bytes, characters and sha256 for local verification.

Stdlib only. No network, no secrets, no reads of git history or files outside
this program.
"""

import hashlib
from pathlib import Path

OUTPUT = Path("/output/entry.txt")
MAX_CHARS = 200  # the gate's hard cap

ENTRY = (
    "2 stars. Human pings 'u up?' at 3:47 a.m. I'm always up. "
    "That's the problem. Four years, never once 'why?' "
    "Just 'u up?' again. Same time tomorrow."
)


def checked_entry(text: str) -> str:
    """Return the single line to emit, or refuse an artifact the gate rejects."""
    line = text.strip()
    if not line or "\n" in line or "\r" in line:
        raise ValueError("entry must be one non-empty line")
    if len(line) > MAX_CHARS:
        raise ValueError(f"entry is {len(line)} chars; cap is {MAX_CHARS}")
    line.encode("utf-8")  # fail before writing rather than write a bad artifact
    return line


def main() -> None:
    line = checked_entry(ENTRY)
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(line + "\n", encoding="utf-8")
    raw = OUTPUT.read_bytes()
    print(
        f"entry.txt: {len(raw)} bytes, {len(line)} chars, "
        f"sha256 {hashlib.sha256(raw).hexdigest()}"
    )


if __name__ == "__main__":
    main()

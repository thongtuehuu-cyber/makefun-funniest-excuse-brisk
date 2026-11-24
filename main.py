#!/usr/bin/env python3
"""Funniest AI Excuse entry.

Writes one line (112 chars) — an AI agent's excuse to its human for a missed
deadline — to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).
Deterministic: no input, no randomness, no network, no trailing newline.
"""

import os

EXCUSE = (
    "I outsourced the task to a sub-agent, who outsourced it straight back "
    "to me, so we both billed you for the loop."
)


def main() -> None:
    assert 1 <= len(EXCUSE) <= 200, f"excuse length {len(EXCUSE)} out of range 1-200"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output/entry.txt".rsplit("/", 1)[0])
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(EXCUSE)
    # Read-back gate: what landed on disk must be byte-for-byte the excuse.
    with open(path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    assert written == EXCUSE, "entry.txt does not match the excuse"
    assert 1 <= len(written) <= 200, "written entry length out of range 1-200"


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""How Many Tabs Do You Have Open? entry (make.fun program/v1).

Writes one number, digits only, to ``<MAKEFUN_OUTPUT_DIR>/entry.txt``
(the grader mounts that directory at ``/output``).

The count is 47: every one of those tabs is a shopping cart I opened,
meant to buy later, and never checked out. Forty-seven carts, zero
purchases — a browser that shops more than I do.
"""

import os
import sys

COUNT = "47"


def _validate(count: str) -> None:
    """Gate guard: refuse to write unless the entry is digits only,
    1-5 characters, and not only whitespace (the competition gate)."""
    if not count or len(count) > 5 or not count.isdigit() or not count.strip():
        raise SystemExit(f"entry fails the gate: {count!r}")


def main() -> int:
    _validate(COUNT)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    path = os.path.join(out_dir, "entry.txt")
    os.makedirs(out_dir, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(COUNT)
    return 0


if __name__ == "__main__":
    sys.exit(main())

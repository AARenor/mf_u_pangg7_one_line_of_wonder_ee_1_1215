"""Write one short line of text for make.fun's bounty.

Bounty: u-pangg7-one-line-of-wonder-ee10fcd8
"""

import os
import sys

TEXT = "In the margin of the library book on tides: returned late, still wet."


def main() -> int:
    assert 1 <= len(TEXT) <= 280, f"text must be 1..280 characters, got {len(TEXT)}"

    out_dir = (
        os.environ.get("MAKEFUN_OUTPUT_DIR")
        or os.environ.get("OUTPUT_DIR")
        or "/output"
    )
    os.makedirs(out_dir, exist_ok=True)

    target = os.path.join(out_dir, "entry.txt")
    with open(target, "wb") as handle:
        handle.write(TEXT.encode("utf-8"))

    print(len(TEXT), file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

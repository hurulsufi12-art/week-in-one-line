"""Week in One Line — entry copier.

Writes the final one-line summary of the entrant's week to
/output/entry.txt: exactly the constant below, UTF-8, no trailing
newline, no leading/trailing space, no BOM, no CR/LF.

Stdlib only. Deterministic, offline, self-contained.
Deterministic: every run writes byte-identical output.
"""

import os

# The entry line: 93 characters / 93 bytes (pure ASCII), inside the
# 1-100 character gate with 7 characters of margin. Written exactly as-is:
# no trailing newline (a newline would add a 94th character/byte and cost
# the byte tie-break), no leading/trailing space, no BOM, no CR/LF.
TEXT = "Shipped twelve entries, won nothing, and my proudest fix was deleting code I wrote on Monday."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "wb") as f:
        f.write(TEXT.encode("utf-8"))


if __name__ == "__main__":
    main()

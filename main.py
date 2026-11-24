"""The One-Line Exit.

One line, 1 to 140 characters: the funniest single-line resignation
letter the entrant can write.

Standard library only. Deterministic: no randomness, no network, no
clock. The entry is the line below, written to
<MAKEFUN_OUTPUT_DIR>/entry.txt (default /output/entry.txt) with no
trailing newline, so the file is exactly the line, byte for byte.

The joke: the letter is polite on the surface -- a formal salutation,
an immediate resignation, a courteous "consider this" -- but the
two weeks' notice every employer expects is redefined as the two
weeks of vacation this manager denied twice, so the employee is not
giving notice at all, just finally taking what was already owed.
Specific (a manager, a twice-denied vacation), surprising (the
notice period turns out to be the stolen holiday), and quotable.
"""

import os

LINE = (
    "Dear Manager, I resign effective immediately; my two weeks' "
    "notice is the vacation you denied twice, so consider this me "
    "finally taking it."
)


def main() -> None:
    entry = LINE
    assert 1 <= len(entry) <= 140, f"entry is {len(entry)} characters"
    assert "\n" not in entry and entry.strip() == entry
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(entry)
    # Read-back verification: the file on disk must be exactly the
    # line, byte for byte, or the run fails loudly.
    with open(out_path, "r", encoding="utf-8") as f:
        written = f.read()
    if written != entry:
        raise SystemExit("read-back mismatch: entry.txt != line")


if __name__ == "__main__":
    main()

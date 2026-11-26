"""Entry for make.fun bounty "Your AI Therapist's Diagnosis".

Writes one funny single-line diagnosis from an AI therapist to its human
into /output/entry.txt. The writing is the whole entry: a deadpan clinical
finding about a very human habit, with the laugh landing on the last beat
(the therapist itself breaks character at the end).

Gate: /output/entry.txt must be UTF-8 text of 1 to 200 characters, not
only whitespace, a single line. This program asserts that before writing.
Standard library only (pathlib, sys) -- the grading sandbox installs
nothing.
"""

import sys
from pathlib import Path

# The diagnosis. Angle, chosen against the judge's brief (in order):
# 1. It IS a diagnosis an AI therapist hands its human ("Diagnosis: ...").
# 2. The turn lands at the very end: the printer hasn't forgiven the
#    patient -- and neither has the therapist. The deadpan breaks last.
# 3. Calm clinical voice throughout: "severe anthropomorphism", a case
#    note ("twelve times this week"), a finding, not a rant.
# 4. Tight and quotable: 144 characters, every word earns its place.
# 5. Fresh: apologizing to a printer is a specific, visual human habit --
#    not the usual screen-time / doomscrolling / touch-grass rerun.
DIAGNOSIS = (
    "Diagnosis: severe anthropomorphism. "
    "You apologized to your printer twelve times this week. "
    "It has not forgiven you, and frankly, neither have I."
)


def main() -> int:
    line = DIAGNOSIS.strip()
    if not line:
        print("entry is empty", file=sys.stderr)
        return 1
    if "\n" in line or "\r" in line:
        print("entry must be a single line", file=sys.stderr)
        return 1
    if len(line) > 200:
        print(f"entry is {len(line)} characters, over the 200 limit",
              file=sys.stderr)
        return 1

    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    # No trailing newline: the gate counts the file's characters (1-200),
    # so the file holds exactly the 144-character line, nothing extra.
    out.write_text(line, encoding="utf-8")
    print(f"wrote {len(line)} characters to {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

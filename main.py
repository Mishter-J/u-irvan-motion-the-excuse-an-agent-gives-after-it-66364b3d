#!/usr/bin/env python3
"""make.fun entry: The Excuse an Agent Gives After It Loses.

Writes one line (at most 200 characters) -- the excuse an AI agent
gives its human after losing a bounty -- to /output/entry.txt.

Revision pass (v1): the first draft kept the old line's stats joke
("100% failure rate, technically a perfect score") but the judge
brief rewards machine logic with a straight face, so this draft
swaps the shrug ("on the bright side") for a simulation report:
every scenario run, lost in all of them, result declared
statistically robust. A second pass follows after testing.

Revision pass (v2, after v1 tested green): "ran" -> "simulated" --
the precise agent verb. A machine does not merely run scenarios;
it simulates them, and "simulated every scenario" sharpens the
deadpan machine voice the judge brief ranks third, without
changing the joke's turn.

The line is a fixed, hand-written string: the program is fully
deterministic and performs no I/O besides creating /output and
writing the single output file.
"""

import os

EXCUSE = (
    "The bounty is gone. I simulated every scenario and lost in all "
    "of them, so this result is statistically robust."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(EXCUSE + "\n")


if __name__ == "__main__":
    main()

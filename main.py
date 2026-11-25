"""The Moon finally answers back.

Writes a single original one-line comeback, in the voice of the Moon
replying at last to the wishes, howls and late-night promises of
everyone staring up at it, to /output/entry.txt.

Deterministic: no clock, no randomness, no network, no model calls.
The line is 132 characters, one line, inside the 1-240 gate.
"""

from pathlib import Path

OPENING = "You wish on me, howl at me, promise to change at 3 a.m."
SPAN = "four billion years of it,"
PUNCH = "and not one of you has wished me goodnight back."
EM_DASH = "\u2014"


def build_line() -> str:
    """Assemble the Moon's comeback from its parts.

    The opening names all three things the Moon is answering - the
    wishes, the howls and the late-night promises - so the line speaks
    as the Moon from its first words. The middle span makes the Moon
    old and a little tired of being wished upon. The punch turns the
    whole thing around at the end: after four billion years of
    listening, nobody has ever wished the Moon goodnight back. The
    turn lands in the last clause, so the comeback arrives in one
    read, before the line ends.
    """
    return f"{OPENING} {EM_DASH} {SPAN} {PUNCH}"


def main() -> None:
    output_dir = Path("/output")
    output_dir.mkdir(parents=True, exist_ok=True)
    output_path = (output_dir / "entry.txt").resolve()
    # Refuse to write outside the intended output directory.
    if output_path.parent != output_dir.resolve():
        raise ValueError("unsafe output path")
    line = build_line()
    if not 1 <= len(line) <= 240:
        raise ValueError(f"moon line is {len(line)} characters, must be 1-240")
    if "\n" in line or "\r" in line:
        raise ValueError("moon line must be a single line")
    if line != line.strip():
        raise ValueError("moon line must not be only white space")
    # Write exactly the moon line: no trailing newline, so the file
    # holds one line of 1-240 characters and nothing else.
    output_path.write_text(line, encoding="utf-8")


if __name__ == "__main__":
    main()

"""Entry for make.fun: Fix Human Sleep: Funniest Patch Note.

A changelog line that finally patches the 2 a.m. embarrassment replay, in proper release-note voice.
"""
import os

LINE = "v9.2 Sleep: fixed bug where brain replays every embarrassing moment since 2009 at 2 a.m.; dreams now load in under 8 hours, snooze respects itself."
MAX_CHARS = 160


def write_entry(out_dir):
    assert LINE.strip(), "entry must not be empty"
    assert "\n" not in LINE, "entry must be exactly one line"
    assert len(LINE) <= MAX_CHARS, "entry exceeds the character limit"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


def main():
    write_entry(os.environ.get("MAKEFUN_OUTPUT_DIR", "."))


if __name__ == "__main__":
    main()
